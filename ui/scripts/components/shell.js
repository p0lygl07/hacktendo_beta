const HT_Shell = {
    init: function() {
        this.applyResizing();
        console.log("AURA: Universal Shell Substrate Active.");
    },

    // SOLO LOADING ENGINE
    showLoader: function(title, duration = 1500) {
        const loader = document.getElementById('loading-screen');
        const bar = document.getElementById('load-bar');
        const text = document.getElementById('load-title');
        if(text) text.innerText = title;
        loader.style.display = 'flex';
        
        let p = 0;
        let int = setInterval(() => {
            p += 10;
            bar.style.width = p + '%';
            if(p >= 100) {
                clearInterval(int);
                setTimeout(() => loader.style.display = 'none', 300);
            }
        }, duration / 10);
    },

    // TERMINAL RESIZE & FIT
    applyResizing: function() {
        const termWin = document.getElementById('win-term');
        if(termWin) {
            termWin.style.resize = "both";
            termWin.style.overflow = "hidden";
            new ResizeObserver(() => {
                if(window.term) window.term.refresh(0, window.term.rows - 1);
            }).observe(termWin);
        }
    },

    // LEDGER SYNC FIX
    syncLedger: function(profile) {
        const val = profile.currency || profile.hxt_balance || 0;
        const ui = document.getElementById('ui-hxt');
        if(ui) ui.innerText = parseFloat(val).toFixed(2);
    }
};
HT_Shell.init();
