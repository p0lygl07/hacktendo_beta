/**
 * HACKTENDO SUBSTRATE BRIDGE v5.0
 * The Master System that ties components together.
 */
const SubstrateBridge = {
    init: function() {
        console.log("%c[ORCHESTRATOR]: MONITORING SUBSTRATE INIT...", "color: #ff003c; font-weight: bold;");
        this.bindEvents();
    },

    bindEvents: function() {
        // Listen for the custom "IdentitySynced" event we'll trigger in system_patcher
        window.addEventListener('HT_IdentitySynced', (e) => {
            const profile = e.detail.profile;
            this.injectNarrativeLayer(profile);
            this.syncLedger(profile);
        });
    },

    injectNarrativeLayer: function(profile) {
        // 1. Initialize Balance Beam based on alignment
        const marker = document.getElementById('align-marker');
        if(marker) {
            const position = 50 + (profile.alignment / 2); // -100 to 100 mapped to 0-100%
            marker.style.left = position + "%";
        }

        // 2. Trigger P0LYGL07 Welcome
        if(profile.level === 1 && profile.xp === 0) {
            this.showPopup("P0LYGL07", "Welcome to the Genesis. I am your admin. Level 1-5 is the Demo Term. Choice is the only variable.");
        }
    },

    syncLedger: function(profile) {
        const hxt = document.getElementById('ui-hxt');
        if(hxt) hxt.innerText = profile.currency.toFixed(2);
    },

    showPopup: function(npc, text) {
        const overlay = document.createElement('div');
        overlay.style = "position:fixed; inset:0; background:rgba(0,0,0,0.9); z-index:9999; display:flex; justify-content:center; align-items:center;";
        overlay.innerHTML = `
            <div style="width:400px; padding:40px; border:1px solid #ff003c; background:#050505; text-align:center;">
                <h1 style="color:#ff003c">${npc}</h1>
                <p style="font-size:12px; color:#ccc;">${text}</p>
                <button onclick="this.parentElement.parentElement.remove()" style="padding:10px 20px; background:#ff003c; color:#fff; border:none; cursor:pointer;">ACKNOWLEDGE</button>
            </div>
        `;
        document.body.appendChild(overlay);
    }
};

SubstrateBridge.init();
