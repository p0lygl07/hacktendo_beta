/**
 * HACKTENDO UI ORCHESTRATOR v6.1
 * Handles Drag-and-Drop, Dynamic Tools, and Module Loading
 */
const HT_UI = {
    init: function() {
        this.setupDragManager();
        this.registerInternalTools();
    },

    // 1. UNIVERSAL DRAG MANAGER (Fixed Movability)
    setupDragManager: function() {
        document.addEventListener('mousedown', (e) => {
            const header = e.target.closest('.window-header');
            if (!header) return;

            const win = header.parentElement;
            win.style.zIndex = 1000; // Bring to front
            
            let shiftX = e.clientX - win.getBoundingClientRect().left;
            let shiftY = e.clientY - win.getBoundingClientRect().top;

            function moveAt(pageX, pageY) {
                win.style.left = pageX - shiftX + 'px';
                win.style.top = pageY - shiftY + 'px';
            }

            function onMouseMove(event) { moveAt(event.pageX, event.pageY); }

            document.addEventListener('mousemove', onMouseMove);
            document.onmouseup = function() {
                document.removeEventListener('mousemove', onMouseMove);
                document.onmouseup = null;
            };
        });
    },

    // 2. TOOL MODULE FACTORY (Solo Operation)
    registerTool: function(config) {
        // config = { id, title, icon, color, action }
        const dock = document.getElementById('dock');
        if (document.getElementById(`dock-${config.id}`)) return;

        const btn = document.createElement('i');
        btn.id = `dock-${config.id}`;
        btn.className = `${config.icon} dock-item`;
        btn.style.color = config.color || "var(--text)";
        btn.title = config.title;
        btn.onclick = config.action;
        dock.appendChild(btn);
    },

    registerInternalTools: function() {
        // Re-injecting the lost modules independently
        this.registerTool({
            id: 'chat', title: 'GLOBAL_CHAT', icon: 'fa-solid fa-comments',
            action: () => window.open('https://hack.chat/?hacktendo', '_blank')
        });
        this.registerTool({
            id: 'store', title: 'H-BROWSER', icon: 'fa-solid fa-cart-shopping', color: 'gold',
            action: () => window.open('https://p7wl.lemonsqueezy.com/', '_blank')
        });
    }
};

HT_UI.init();
