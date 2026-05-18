/**
 * HACKTENDO EXTENSION: UNIVERSAL UI
 */
const HT_Ext = {
    apply: function() {
        this.fixTerminalResize();
        this.hookMountButton();
    },

    fixTerminalResize: function() {
        const termWin = document.getElementById('win-term');
        if(termWin) {
            termWin.style.resize = "both";
            termWin.style.overflow = "hidden";
            new ResizeObserver(() => {
                if(window.term) window.term.refresh(0, window.term.rows - 1);
            }).observe(termWin);
        }
    },

    hookMountButton: function() {
        // Intercepts the deployMission call to show the loader
        const oldDeploy = window.deployMission;
        window.deployMission = async (id) => {
            HT_Shell.showLoader(`MOUNTING_${id.toUpperCase()}`, 2000);
            setTimeout(async () => {
                await oldDeploy(id);
            }, 1800);
        };
    }
};
HT_Ext.apply();
