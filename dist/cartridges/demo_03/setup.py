import os, sys, shutil

def deploy(path):
    os.makedirs(path, exist_ok=True)
    
    if os.path.exists("submit_flag.py"):
        shutil.copy("submit_flag.py", os.path.join(path, "submit_flag.py"))
        os.chmod(os.path.join(path, "submit_flag.py"), 0o755)

    briefing = """
================================================
MISSION 03: THE AEGIS PROTOCOL
================================================
TARGET: Unknown Assailant

[INTEL]:
Someone is probing your system. They followed your digital footprint 
after your last op. We don't know who they are, but they are elite.

[YOUR DIRECTIVE]:
1. Run './probe_signal.sh' to ping the assailant and figure out what they want.
2. WARNING: This will likely trigger an aggressive counter-attack.
3. If they drop malware on your system, use your new OS DECOMPILER to reverse 
   engineer the signature and find the killswitch flag before the trace finishes.
================================================
"""
    with open(os.path.join(path, "briefing.txt"), "w") as f: f.write(briefing)

    # The probe script that triggers the API attack event
    probe = """#!/bin/bash
echo '[*] Initiating counter-probe on unknown signal...'
sleep 1
curl -s -X POST http://127.0.0.1:6060/api/trigger_attack > /dev/null
echo '[!] PROBE DETECTED. ENEMY FIREWALL ENRAGED.'
"""
    with open(os.path.join(path, "probe_signal.sh"), "w") as f: f.write(probe)
    os.chmod(os.path.join(path, "probe_signal.sh"), 0o755)

if __name__ == "__main__":
    deploy(sys.argv[1])
