import os
import sys
import time
import json
import subprocess

# --- CONFIGURATION ---
DEMO_HANDLE = "DEMO_OPERATOR"
DEMO_PORT = 6060
BASE_URL = f"http://localhost:{DEMO_PORT}"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def inject_demo_profile():
    """Injects a high-level profile so the user can test advanced features immediately."""
    os.makedirs("profiles", exist_ok=True)
    path = f"profiles/{DEMO_HANDLE}.json"
    
    demo_data = {
        "handle": DEMO_HANDLE,
        "ledger": 500.0,       # Pre-loaded with HXT
        "xp": 2500,            # Boosted XP
        "level": 3,            # Level 3 Rank
        "karma": 10,           # Sentinel Alignment
        "inventory": ["DEMO_BREAKER_PACK"],
        "nodes": 1,            # One node already active
        "passive_rate": 1.5
    }
    
    with open(path, 'w') as f:
        json.dump(demo_data, f, indent=4)
    print(f"\033[92m[+] Neural Bridge Injected: {DEMO_HANDLE} initialized.\033[0m")

def print_demo_intro():
    logo = f"""\033[95m
 ██╗  ██╗ █████╗  ██████╗██╗  ██╗████████╗███████╗███╗   ██╗██████╗  ██████╗ 
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██╔════╝████╗  ██║██╔══██╗██╔═══██╗
 ███████║███████║██║     █████╔╝    ██║   █████╗  ██╔██╗ ██║██║  ██║██║   ██║
 ██╔══██║██╔══██║██║     ██╔═██╗    ██║   ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║
 ██║  ██║██║  ██║╚██████╗██║  ██╗   ██║   ███████╗██║ ╚████║██████╔╝╚██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 
 \033[0m
 \033[96m[ DEMO VERSION // V-NET SUBSTRATE ]\033[0m
 \033[90m------------------------------------------------------------------------\033[0m
 \033[93m ARCHITECT : Joshua Bryant Burton (-P0LYGL07- >'0'<)
 MISSION   : Breach the OmniCorp 'Chen-Lite' Intel Relay.
 TIME LIMIT: 10 MINUTES UNTIL TRACE COMPLETION.\033[0m
 \033[90m------------------------------------------------------------------------\033[0m
    """
    print(logo)

def start_engine():
    print(f"\033[94m[SYSTEM] Synchronizing with local loopback...")
    time.sleep(1)
    print(f"[SYSTEM] Bypassing standard authentication...")
    time.sleep(1)
    print(f"[SYSTEM] Engaging Substrate Core...\033[0m")
    
    # Launch the core engine. 
    # We pass the demo handle as an environment variable so core.py knows who is playing.
    env = os.environ.copy()
    env["HACKTENDO_MODE"] = "DEMO"
    env["DEMO_USER"] = DEMO_HANDLE
    
    try:
        # Note: In the demo version, you'd point this to your encrypted core.py
        subprocess.run([sys.executable, "core.py"], env=env)
    except KeyboardInterrupt:
        print("\n\033[91m[!] Demo Connection Terminated.\033[0m")

if __name__ == "__main__":
    clear()
    print_demo_intro()
    inject_demo_profile()
    
    print(f"\n\033[92mREADY TO JACK IN?\033[0m")
    input("Press ENTER to initialize demo sequence...")
    
    start_engine()
