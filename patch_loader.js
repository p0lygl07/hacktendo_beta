// Add this to a new file: patch_loader.js
// It will be called by deck.html to inject new features
function injectNewSystems() {
    // 1. Inject the Shop Button to the Dock
    const dock = document.getElementById('dock');
    const shopBtn = document.createElement('i');
    shopBtn.className = "fa-solid fa-cart-shopping dock-item";
    shopBtn.title = "H-Browser (Store)";
    shopBtn.onclick = () => window.open('https://p7wl.lemonsqueezy.com/', '_blank');
    dock.appendChild(shopBtn);

    // 2. Inject the Warefac Icon to the Start Menu
    const startMenu = document.getElementById('start-menu');
    const warefacBtn = document.createElement('div');
    warefacBtn.className = "tool-link";
    warefacBtn.innerHTML = `<i class="fa-solid fa-industry"></i> WAREFAC_FACTORY`;
    warefacBtn.onclick = () => alert("Warefac Engine Initializing...");
    startMenu.appendChild(warefacBtn);

    // 3. Inject the Alignment Beam to the Sidebar
    const sidebar = document.getElementById('sidebar');
    const beam = document.createElement('div');
    beam.innerHTML = `
        <div style="font-size:9px; color:var(--text); margin-top:10px;">BALANCE_BEAM</div>
        <div style="height:4px; background: linear-gradient(to right, #ff003c, #8a8d91, #00ff41); margin-top:5px;">
            <div id="alignment-marker" style="width:2px; height:10px; background:#fff; margin: -3px auto 0 auto;"></div>
        </div>
    `;
    sidebar.insertBefore(beam, sidebar.childNodes[4]);
}
