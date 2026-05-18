// File: v3_patch.js
function applyV3Substrate() {
    // 1. Force the Balance Beam into the Sidebar
    const sidebar = document.getElementById('sidebar');
    if (sidebar && !document.getElementById('ht-balance-beam')) {
        const beam = document.createElement('div');
        beam.id = "ht-balance-beam";
        beam.style = "margin-top:20px; padding:15px 5px; border-top:1px solid #1a1b1e;";
        beam.innerHTML = `
            <div style="font-size:8px; color:#8a8d91; display:flex; justify-content:space-between; margin-bottom:8px;">
                <span>BLACKHAT</span><span>WHITEHAT</span>
            </div>
            <div style="height:4px; background: linear-gradient(to right, #ff003c, #111, #00ff41); position:relative; border-radius:2px;">
                <div id="alignment-marker" style="width:6px; height:10px; background:#fff; position:absolute; left:50%; top:-3px; transition:1s;"></div>
            </div>
        `;
        sidebar.appendChild(beam);
    }
}

function triggerP0LYIntro() {
    const overlay = document.createElement('div');
    overlay.style = "position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:9999; display:flex; justify-content:center; align-items:center;";
    overlay.innerHTML = `
        <div style="width:400px; padding:40px; border:1px solid #ff003c; background:#050505; text-align:center; box-shadow: 0 0 30px #ff003c22;">
            <h1 style="color:#ff003c; letter-spacing:10px;">P0LYGL07</h1>
            <p style="font-size:12px; color:#ccc;">Welcome to the Hacktendo Substrate. I am your admin and opportunity coach. Demo Term (Level 1-5) initialized.</p>
            <button onclick="this.parentElement.parentElement.remove()" style="padding:12px 30px; background:#ff003c; border:none; color:#fff; cursor:pointer; font-weight:bold;">INITIALIZE</button>
        </div>
    `;
    document.body.appendChild(overlay);
}
