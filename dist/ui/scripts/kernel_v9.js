const socket = io.connect('http://' + document.domain + ':' + location.port);

const Kernel = {
    handle: "",
    
    boot: async function() {
        const h = document.getElementById('handle-in').value || "GHOST";
        const res = await fetch('/api/init_identity', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ handle: h }) });
        const data = await res.json();
        
        this.showLoader("SYNCING_SUBSTRATE", 1500);
        setTimeout(() => {
            document.getElementById('boot-screen').style.display = 'none';
            document.getElementById('ui-handle').innerText = "@" + data.profile.handle;
            document.getElementById('ui-hxt').innerText = parseFloat(data.profile.hxt_balance || data.profile.currency).toFixed(2);
            this.initWindowManager();
            socket.emit('request_v9_tools', { handle: h });
        }, 1600);
    },

    showLoader: function(msg, dur) {
        const ov = document.getElementById('loading-overlay');
        const bar = document.getElementById('load-fill');
        document.getElementById('load-msg').innerText = msg;
        ov.style.display = 'flex'; bar.style.width = '0%';
        let p = 0;
        let inv = setInterval(() => {
            p += 10; bar.style.width = p + '%';
            if(p >= 100) { clearInterval(inv); setTimeout(()=>ov.style.display='none', 200); }
        }, dur / 10);
    },

    createWindow: function(id, title, contentHTML) {
        if(document.getElementById(`win-${id}`)) { this.toggleWindow(id); return; }
        const win = document.createElement('div');
        win.id = `win-${id}`; win.className = "window"; win.style.display = "flex";
        win.style.top = "100px"; win.style.left = "300px";
        win.innerHTML = `<div class="window-header"><span>${title}</span><i class="fa-solid fa-xmark" onclick="Kernel.toggleWindow('${id}')"></i></div><div class="window-content" id="content-${id}">${contentHTML}</div>`;
        document.getElementById('viewport').appendChild(win);
    },

    toggleWindow: function(id) {
        const win = document.getElementById(`win-${id}`);
        if(win) win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
    },

    toggleHub: function() {
        const h = document.getElementById('mission-hub');
        h.style.display = (h.style.display === 'block') ? 'none' : 'block';
    },

    deploy: async function(id) {
        this.showLoader(`MOUNTING_${id.toUpperCase()}`, 1500);
        const res = await fetch('/api/load_cartridge', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ cartridge_id: id, handle: this.handle }) });
        const data = await res.json();
        this.toggleHub();
        // Dynamic plugin loading
        data.manifest.plugins.forEach(p => {
            if(p === "term") this.initTerminal();
            else this.createWindow(p, p.toUpperCase(), `<div id='${p}-view'></div>`);
        });
    },

    initTerminal: function() {
        this.createWindow('term', 'TERMINAL_CORE', '<div id="term-box" style="height:100%;"></div>');
        window.term = new Terminal({ theme: { background: '#0a0a0c', foreground: '#00ff41' } });
        window.term.open(document.getElementById('term-box'));
        window.term.onData(d => socket.emit('terminal_input', { input: d }));
    },

    initWindowManager: function() {
        document.addEventListener('mousedown', e => {
            const h = e.target.closest('.window-header'); if(!h) return;
            const w = h.parentElement; w.style.zIndex = 1000;
            let sX = e.clientX, sY = e.clientY, sL = w.offsetLeft, sT = w.offsetTop;
            const mv = ev => { w.style.left = (sL + ev.clientX - sX) + "px"; w.style.top = (sT + ev.clientY - sY) + "px"; };
            const st = () => { document.removeEventListener('mousemove', mv); document.removeEventListener('mouseup', st); };
            document.addEventListener('mousemove', mv); document.addEventListener('mouseup', st);
        });
    }
};

socket.on('v9_inject_dock', data => {
    const dock = document.getElementById('dock');
    if(document.getElementById(`dock-${data.id}`)) return;
    const i = document.createElement('i');
    i.id = `dock-${data.id}`; i.className = `${data.icon} dock-item`;
    i.title = data.title; i.style.color = data.color || "#8a8d91";
    i.onclick = () => { if(data.url) window.open(data.url, '_blank'); else eval(data.action); };
    dock.appendChild(i);
});

socket.on('terminal_output', d => window.term && window.term.write(d.output));
