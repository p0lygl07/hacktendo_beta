const socket = io.connect('http://' + document.domain + ':' + location.port);

const Kernel = {
    handle: "",
    windows: {},
    
    boot: async function() {
        const input = document.getElementById('handle-in').value || "GHOST";
        const res = await fetch('/api/init_identity', {
            method: 'POST', headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ handle: input })
        });
        const data = await res.json();
        
        this.handle = data.profile.handle;
        this.showLoader("BOOTING_VPU_v7.0", 2000);
        
        setTimeout(() => {
            document.getElementById('boot-screen').style.display = 'none';
            document.getElementById('ui-handle').innerText = "@" + this.handle;
            this.syncLedger(data.profile.hxt_balance);
            this.initWindowManager();
            // Tell backend we are ready for tool injection
            socket.emit('request_v7_tools', { handle: this.handle });
        }, 2200);
    },

    showLoader: function(msg, duration) {
        const overlay = document.getElementById('loading-overlay');
        const bar = document.getElementById('load-bar-fill');
        document.getElementById('load-msg').innerText = msg;
        overlay.style.display = 'flex';
        bar.style.width = '0%';
        let p = 0;
        let int = setInterval(() => {
            p += 5; bar.style.width = p + '%';
            if(p >= 100) { clearInterval(int); setTimeout(() => overlay.style.display='none', 200); }
        }, duration / 20);
    },

    syncLedger: function(val) {
        document.getElementById('ui-hxt').innerText = parseFloat(val).toFixed(2);
    },

    createWindow: function(id, title, contentHTML, options = {}) {
        if(document.getElementById(`win-${id}`)) { this.toggleWindow(id); return; }

        const win = document.createElement('div');
        win.id = `win-${id}`;
        win.className = "window";
        win.style.left = (options.x || 100) + "px";
        win.style.top = (options.y || 100) + "px";
        win.style.display = "flex";
        
        win.innerHTML = `
            <div class="window-header">
                <span>${title.toUpperCase()}</span>
                <i class="fa-solid fa-xmark" onclick="Kernel.toggleWindow('${id}')" style="cursor:pointer;"></i>
            </div>
            <div class="window-content" id="content-${id}">${contentHTML}</div>
        `;
        document.getElementById('viewport').appendChild(win);
        this.windows[id] = win;
    },

    toggleWindow: function(id) {
        const win = document.getElementById(`win-${id}`);
        if(win) win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
    },

    initWindowManager: function() {
        document.addEventListener('mousedown', (e) => {
            const header = e.target.closest('.window-header');
            if(!header) return;
            const win = header.parentElement;
            win.style.zIndex = 1000;
            // Handle movement
            let startX = e.clientX, startY = e.clientY;
            let startL = win.offsetLeft, startT = win.offsetTop;
            const move = (ev) => {
                win.style.left = (startL + ev.clientX - startX) + "px";
                win.style.top = (startT + ev.clientY - startY) + "px";
            };
            const stop = () => { document.removeEventListener('mousemove', move); document.removeEventListener('mouseup', stop); };
            document.addEventListener('mousemove', move);
            document.addEventListener('mouseup', stop);
        });
    }
};

// Listen for Tool Injections from Extensions
socket.on('v7_inject_tool', (data) => {
    const dock = document.getElementById('dock');
    if(document.getElementById(`dock-${data.id}`)) return;
    const btn = document.createElement('i');
    btn.id = `dock-${data.id}`;
    btn.className = `${data.icon} dock-item`;
    btn.title = data.title;
    btn.style.color = data.color || "#8a8d91";
    btn.onclick = () => {
        if(data.type === "url") window.open(data.action, '_blank');
        else if(data.type === "window") Kernel.createWindow(data.id, data.title, data.action);
        else eval(data.action);
    };
    dock.appendChild(btn);
});

// Setup Terminal specifically when injected
socket.on('v7_init_term', () => {
    Kernel.createWindow('term', 'Terminal', '<div id="xterm-container" style="height:100%;"></div>');
    window.term = new Terminal({ theme: { background: '#0a0a0c', foreground: '#00ff41' }, cursorBlink: true });
    window.term.open(document.getElementById('xterm-container'));
    window.term.onData(data => socket.emit('terminal_input', { input: data }));
});

socket.on('terminal_output', data => window.term && window.term.write(data.output));

function sendHubChat() {
    const input = document.getElementById('hub-input');
    const text = input.value;
    if(!text) return;
    
    // Display our message in log locally
    const log = document.getElementById('comms-log');
    log.innerHTML += `<div style="margin-bottom:10px; font-size:11px; opacity:0.7;"><b>[@${Kernel.handle}]</b>: ${text}</div>`;
    
    // Send to Narrative Engine
    socket.emit('hub_chat_message', { handle: Kernel.handle, text: text });
    input.value = "";
    log.scrollTop = log.scrollHeight;
}

// Allow Enter key to send
document.addEventListener('keypress', (e) => {
    if(e.key === 'Enter' && document.activeElement.id === 'hub-input') sendHubChat();
});
