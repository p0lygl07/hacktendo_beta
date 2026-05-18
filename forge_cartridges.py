import os
import zipfile

def forge_mission(mission_id, script_content):
    os.makedirs(mission_id, exist_ok=True)
    setup_path = os.path.join(mission_id, "setup.py")
    with open(setup_path, "w") as f: f.write(script_content)
    zip_name = f"{mission_id}.zip"
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(setup_path, arcname=f"{mission_id}/setup.py")
    print(f"[+] Forged Cartridge: {zip_name}")
    os.remove(setup_path)
    os.rmdir(mission_id)

chen_logic = """
import time
def run_mission():
    print("\\n\\033[96m[>>>] BYPASSING QUANTUM ROUTER [<<<]\\033[0m")
    time.sleep(1.0)
    print(">> CHEN: 'Someone is probing the Sector 7 perimeter. I am deploying the Aegis countermeasures.'")
    print(">> SYSTEM: Aegis bypassed. Workstation accessed.")
    print("\\n\\033[92m[+] MISSION COMPLETE. FLAG GENERATED.\\033[0m")
    print("\\033[93m[ FLAG{CHEN_AEGIS_BYPASS_99} ]\\033[0m\\n")
if __name__ == "__main__": run_mission()
"""

vance_logic = """
import time
def run_mission():
    print("\\n\\033[95m[>>>] DECRYPTING INTERROGATION LOGS [<<<]\\033[0m")
    time.sleep(1.0)
    print(">> VANCE: 'The Rebel operator wouldn't talk, but their deck had coordinates to the Orek Nexus.'")
    print(">> SYSTEM: Encrypted payload intercepted.")
    print("\\n\\033[92m[+] MISSION COMPLETE. FLAG GENERATED.\\033[0m")
    print("\\033[93m[ FLAG{VANCE_INTEL_EXTRACT_01} ]\\033[0m\\n")
if __name__ == "__main__": run_mission()
"""

forge_mission("pack_sarah_chen", chen_logic)
forge_mission("pack_elena_vance", vance_logic)
