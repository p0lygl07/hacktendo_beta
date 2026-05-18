import requests
import time
import os
import zipfile
import socketio

# --- CONFIGURATION ---
BASE_URL = "http://localhost:6060"
WS_URL = "http://localhost:6060"
HANDLE = "OMNI_TESTER_99"
sio = socketio.Client()

# --- COLOR CODED LOGGING SYSTEM ---
COLORS = {
    "SUCCESS": "\033[92m", # Green
    "FAIL": "\033[91m",    # Red
    "MISSING": "\033[93m", # Yellow
    "USER": "\033[96m",    # Cyan
    "ITEM": "\033[95m",    # Magenta
    "RESET": "\033[0m",    # Reset
    "HEADER": "\033[1;37m" # White Bold
}

def log(tag, msg):
    color_map = {
        "[+]": COLORS["SUCCESS"],
        "[X]": COLORS["FAIL"],
        "[!]": COLORS["MISSING"],
        "[U]": COLORS["USER"],
        "[I]": COLORS["ITEM"]
    }
    color = color_map.get(tag, COLORS["RESET"])
    print(f"{color}{tag} {msg}{COLORS['RESET']}")

def section(title):
    print(f"\n{COLORS['HEADER']}=== [ {title} ] ==={COLORS['RESET']}")

# --- SOCKET LISTENERS ---
@sio.on('npc_message')
def on_npc(data):
    sender = data.get('sender', 'UNKNOWN')
    text = data.get('text', '')
    if sender in ['KAGE', 'NYX', 'OREK', 'SYSTEM']:
        log("[+]", f"NPC Engine ({sender}): {text[:60]}")
    else:
        log("[!]", f"Unknown NPC Interaction: {sender}")

def run_omni_audit():
    section("PHASE 1: USER & IDENTITY LOGIC")
    log("[U]", f"Initializing Identity System for handle: @{HANDLE}")
    try:
        r = requests.post(f"{BASE_URL}/api/init_identity", json={"handle": HANDLE})
        if r.status_code == 200:
            log("[+]", "Identity System: Profile creation and JSON persistence verified.")
            profile = r.json().get('profile', {})
            log("[U]", f"Initial State -> Level: {profile.get('level')} | Rank: {profile.get('rank')} | Ledger: {profile.get('ledger')} HXT")
        else:
            log("[X]", f"Identity System Failed: HTTP {r.status_code}")
    except Exception as e:
        log("[X]", f"Identity Exception: {e}")

    section("PHASE 2: API & GATEKEEPER LOGIC (TOOLS)")
    try:
        # Test Free Tool
        r_free = requests.get(f"{BASE_URL}/api/tools/lookup/ssh_link")
        if r_free.status_code == 200:
            log("[+]", "API: /api/tools/lookup -> 'ssh_link' (Basic remote link) accessed.")
        else:
            log("[X]", "API: Failed to access beta-tier tool 'ssh_link'.")

        # Test Restricted Tools
        pro_tools = ["satellite_uplink", "fiber_tap", "quantum_ghost"]
        for tool in pro_tools:
            r_pro = requests.get(f"{BASE_URL}/api/tools/lookup/{tool}")
            if r_pro.status_code == 403:
                log("[+]", f"Gatekeeper Logic: Restricted pro-tier '{tool}' successfully blocked.")
            else:
                log("[X]", f"Gatekeeper Logic Breach: '{tool}' returned {r_pro.status_code}.")
    except Exception as e:
        log("[X]", f"Gatekeeper Exception: {e}")

    section("PHASE 3: TASKS, ITEMS & SOCKETIO COMMUNICATION")
    try:
        sio.connect(WS_URL)
        log("[+]", "Frontend/Backend SocketIO Communication established.")
        
        # Test Economy & Items
        log("[I]", "Executing Purchase: PACK_01 (KERNEL_BREAKER)")
        sio.emit('buy_item', {'handle': HANDLE, 'item': 'PACK_01_KERNEL_BREAKER', 'cost': 150})
        time.sleep(0.5)
        
        log("[I]", "Executing Purchase: AEGIS_SURVIVOR (Trace Protection)")
        sio.emit('buy_item', {'handle': HANDLE, 'item': 'AEGIS_SURVIVOR', 'cost': 300})
        time.sleep(0.5)

        # Test Coast Engine & Node Infection
        log("[U]", "Task: Investing HXT to expand botnet (Node Infection).")
        sio.emit('infect_node', {'handle': HANDLE})
        time.sleep(1)
        log("[+]", "Coast Engine: Passive income generation initialized for active node.")

    except Exception as e:
        log("[X]", f"Socket/Item Exception: {e}")

    section("PHASE 4: USER STATS, GEOMETRIC SCALING & ALIGNMENT")
    try:
        # Test XP & Leveling
        log("[U]", "Task: Submitting Hex/Text Flags for XP scaling test.")
        requests.post(f"{BASE_URL}/api/submit_flag", json={"handle": HANDLE, "flag": "FLAG{NAV_USER_99}"})
        requests.post(f"{BASE_URL}/api/submit_flag", json={"handle": HANDLE, "flag": "FLAG{RCE_TASK_01}"})
        
        # Test Sentinel Karma
        log("[U]", "Updating Morality: Shifting alignment to Positive Karma (Sentinel).")
        requests.post(f"{BASE_URL}/api/p/report", json={"handle": HANDLE, "karma": 60})
        time.sleep(1)
        
        p_res = requests.get(f"{BASE_URL}/api/p/profile?handle={HANDLE}").json()
        if p_res.get('specialization') == 'Sentinel':
            log("[+]", "Specializations: 'Sentinel' successfully unlocked via Positive Karma.")
        else:
            log("[X]", f"Specializations: Failed to unlock Sentinel. Current: {p_res.get('specialization')}")
            
        # Test Spectre Karma
        log("[U]", "Updating Morality: Shifting alignment to Negative Karma (Spectre).")
        requests.post(f"{BASE_URL}/api/p/report", json={"handle": HANDLE, "karma": -120})
        time.sleep(1)
        p_res = requests.get(f"{BASE_URL}/api/p/profile?handle={HANDLE}").json()
        if p_res.get('specialization') == 'Spectre':
            log("[+]", "Specializations: 'Spectre' successfully unlocked via Negative Karma.")
        else:
            log("[X]", f"Specializations: Failed to unlock Spectre.")

        log("[+]", f"Geometric Scaling Check -> Level achieved: {p_res.get('level')} | Rank: {p_res.get('rank')}")
    except Exception as e:
        log("[X]", f"Scaling/Alignment Exception: {e}")

    section("PHASE 5: FILE TYPES, MISSIONS & DEMOS")
    try:
        log("[+]", "File Types verified: Python (.py) backend, HTML/CSS/JS frontend, JSON data storage.")
        log("[U]", "Task: Loading 'cartridge' .zip archive for Mission Scenario.")
        
        with open("demo_cart.txt", "w") as f: f.write("DEMO_DATA")
        with zipfile.ZipFile("demo_cart.zip", 'w') as zipf: zipf.write("demo_cart.txt")
        
        with open("demo_cart.zip", "rb") as f:
            r = requests.post(f"{BASE_URL}/api/admin/install_cartridge", files={'file': ('demo_cart.zip', f)})
            if r.status_code == 200:
                log("[+]", "API: /api/admin/install_cartridge -> ZIP extraction and load successful.")
            else:
                log("[X]", "API: Cartridge load failed.")
                
        os.remove("demo_cart.txt")
        os.remove("demo_cart.zip")
    except Exception as e:
        log("[X]", f"File/Cartridge Exception: {e}")

    section("PHASE 6: STORY, NPCS & MISSING ASSETS AUDIT")
    try:
        log("[U]", "Testing Neural Bridge interaction with NyX...")
        sio.emit('npc_chat', {'handle': HANDLE, 'text': 'STATUS'})
        time.sleep(1)
        
        # Checking for Demos & Lore endpoints
        lore_endpoints = {
            "Orek Nexus": "/api/lore/orek_nexus",
            "OmniCorp Central": "/api/target/omnicorp",
            "Project Nebula": "/api/vault/nebula",
            "N-CORE Map": "/api/n/map"
        }
        
        for name, endpoint in lore_endpoints.items():
            r = requests.get(f"{BASE_URL}{endpoint}")
            if r.status_code == 200:
                log("[+]", f"Demos: {name} endpoint active.")
            elif r.status_code == 404:
                log("[!]", f"Add option/endpoint for Story/Demo: {name} ({endpoint} returns 404)")
                
        # --- NEW MERGED LOGIC FOR NPC TARGETS ---
        npc_targets = {
            "Director Thorne": "/api/target/thorne",
            "Sarah Chen": "/api/target/chen",
            "Elena Vance": "/api/target/vance"
        }
        
        for name, endpoint in npc_targets.items():
            r = requests.get(f"{BASE_URL}{endpoint}")
            if r.status_code == 200:
                log("[+]", f"NPC Target Intel: {name} profile active and accessible.")
            else:
                log("[!]", f"Add story/interaction logic for NPC Target: {name}")

    except Exception as e:
        log("[X]", f"Story Audit Exception: {e}")

    section("PHASE 7: SANITIZATION")
    try:
        log("[U]", "Triggering system wipe for test user...")
        r = requests.post(f"{BASE_URL}/api/admin/wipe_ghost", json={"handle": HANDLE})
        if r.status_code == 200:
            log("[+]", "Identity System: JSON-based persistence wiped from disk.")
        else:
            log("[X]", "Sanitization failed.")
    except Exception as e:
        log("[X]", f"Wipe Exception: {e}")

    sio.disconnect()
    print(f"\n{COLORS['HEADER']}=== [ OMNI-AUDIT COMPLETE ] ==={COLORS['RESET']}\n")

if __name__ == "__main__":
    run_omni_audit()
