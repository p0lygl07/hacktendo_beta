# HACKTENDO MINER MODULE
# Usage: run miner --target OMNI_CLOUD

def execute(socketio, chain, handle):
    socketio.emit('response', {"text": ">>> INITIALIZING HXT MINER... CONNECTING TO LEDGER."})
    
    # Simulate a "Proof of Exploit"
    socketio.emit('response', {"text": "[*] Injecting entropy into Target Node..."})
    
    # Call the chain.mine() function
    block_id = chain.mine(difficulty=4)
    
    if block_id:
        socketio.emit('response', {
            "text": f"[+] BLOCK CONFIRMED. Index: {block_id}. Reward: 50 HXT credited to {handle}."
        })
        # Logic to update user balance in pcore goes here
    else:
        socketio.emit('response', {"text": "[!] Mining failed: No pending transactions in the pool."})
