# HACKTENDO // DEMO MODULE
def run_demo_sequence(socketio, handle):
    # 1. Trigger Intro
    socketio.emit('npc_message', {
        "sender": "KAGE", 
        "text": "LISTEN UP: This is a restricted demo link. You've got high-level access for a limited time.",
        "color": "var(--vanguard)"
    })
    
    # 2. Grant Demo Resources
    import pcore
    pcore.add_progress(handle=handle, xp_gain=1500, hxt_gain=500)
    
    # 3. Unlock a 'Demo Only' Target
    socketio.emit('npc_message', {
        "sender": "SYSTEM", 
        "text": "DEMO_NODE 'CHEN_LITE' APPEARED ON N-CORE MAP.",
        "color": "gold"
    })

def end_demo(socketio):
    # Trigger the glitch and shutdown
    glitch_text = "ERROR: TRACE_LEVEL_CRITICAL... CONNECTION TERMINATED BY OMNICORP."
    socketio.emit('npc_message', {"sender": "SYSTEM", "text": glitch_text, "color": "red"})
    # Redirect user to the itch.io page after 3 seconds
    socketio.emit('eval_js', {"code": "setTimeout(() => { window.location.href = 'https://hacktendo.itch.io'; }, 3000);"})
