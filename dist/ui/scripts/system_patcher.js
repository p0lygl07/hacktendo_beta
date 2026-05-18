const socket = io.connect('http://' + document.domain + ':' + location.port);
const term = new Terminal({ theme: { background: '#000', foreground: '#00ff41' } });
let userHandle = "";

document.getElementById('boot-btn').onclick = async () => {
    userHandle = document.getElementById('handle-in').value || "";
    const res = await fetch('/api/init_identity', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ handle: userHandle })
    });
    const data = await res.json();
    document.getElementById('boot-screen').style.display = 'none';
    document.getElementById('ui-hxt').innerText = data.profile.currency.toFixed(2);
    document.getElementById('ui-handle').innerText = "@" + data.profile.handle;
    toggleWindow('term');
};

term.open(document.getElementById('terminal-view'));
term.onData(data => socket.emit('terminal_input', { input: data }));
socket.on('terminal_output', data => term.write(data.output));

function toggleWindow(id) {
    const win = document.getElementById(`win-${id}`);
    win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
}

function updateLedger(val) {
    document.getElementById('ui-hxt').innerText = val.toFixed(2);
}
