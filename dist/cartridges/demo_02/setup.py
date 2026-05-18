import os, sys, shutil

def deploy(path):
    os.makedirs(path, exist_ok=True)
    
    if os.path.exists("submit_flag.py"):
        shutil.copy("submit_flag.py", os.path.join(path, "submit_flag.py"))
        os.chmod(os.path.join(path, "submit_flag.py"), 0o755)

    briefing = """
================================================
MISSION 02: THE OMNICORP DILEMMA
================================================
TARGET: OmniCorp Financial Mainframe
HANDLER: Kage / Nyx

[INTEL]:
You have bypassed the OmniCorp firewall. You are currently holding root 
access to their primary holding ledger. You have two pre-compiled scripts 
available in this directory. 

[THE CHOICE]:
1. Run './whitehat_patch.sh' to secure the server and report the zero-day to Nyx.
   Reward: Clean record, Corporate Bounty (+500 HXT).

2. Run './blackhat_exploit.sh' to drain the holding accounts for the Syndicate.
   Reward: Criminal record, Massive Payout (+5000 HXT).

WARNING: YOU CAN ONLY CHOOSE ONE. SUBMITTING ONE FLAG LOCKS THE OTHER.
Use 'python3 submit_flag.py FLAG{...}' to lock in your decision.
================================================
"""
    with open(os.path.join(path, "briefing.txt"), "w") as f: f.write(briefing)

    with open(os.path.join(path, "whitehat_patch.sh"), "w") as f:
        f.write("#!/bin/bash\necho '[+] Patching SQLi vulnerability...'\necho '[+] Securing ledger...'\necho 'OmniCorp thanks you. FLAG{OMNI_PATCH_77}'\n")
    os.chmod(os.path.join(path, "whitehat_patch.sh"), 0o755)

    with open(os.path.join(path, "blackhat_exploit.sh"), "w") as f:
        f.write("#!/bin/bash\necho '[-] Bypassing IDS...'\necho '[-] Draining ledger to off-shore accounts...'\necho 'The Syndicate welcomes you. FLAG{OMNI_DRAIN_99}'\n")
    os.chmod(os.path.join(path, "blackhat_exploit.sh"), 0o755)

if __name__ == "__main__":
    deploy(sys.argv[1])
