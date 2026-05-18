import os, sys, shutil

def deploy(path):
    os.makedirs(path, exist_ok=True)
    
    # 1. Provision the Submission Tool
    # Copies the tool from the root directory into this specific mission folder
    if os.path.exists("submit_flag.py"):
        shutil.copy("submit_flag.py", os.path.join(path, "submit_flag.py"))
        os.chmod(os.path.join(path, "submit_flag.py"), 0o755)

    # 2. User Flag (Plain sight)
    with open(os.path.join(path, "readme.txt"), "w") as f:
        f.write("Welcome to Demo 01. Your first flag is FLAG{NAV_USER_99}.\n")

    # 3. Task Flag (RCE Simulation)
    with open(os.path.join(path, "vulnping.sh"), "w") as f:
        f.write("#!/bin/bash\necho 'Executing ping...'\nif [ \"$1\" == \"; cat secret.txt\" ]; then\n  echo 'FLAG{RCE_TASK_01}'\nfi\n")
    os.chmod(os.path.join(path, "vulnping.sh"), 0o755)

    # 4. Connect Flag (Hidden File)
    with open(os.path.join(path, ".nyx_intel"), "w") as f:
        f.write("Nyx Intel: You found the hidden file. Submit FLAG{NYX_CONN_XX} to verify.\n")

    # 5. The Mission Briefing (Guidance & Instructions)
    briefing = """
================================================
MISSION 01: NAVIGATION & RCE (Demo Term)
================================================
HANDLER: Nyx
OBJECTIVE: Recover 3 Flags to advance.

[GUIDANCE & TACTICS]:
1. USER FLAG: Use the 'cat' command to read files in plain sight.
   Example: cat readme.txt
   
2. TASK FLAG: The file 'vulnping.sh' simulates an RCE (Remote Code Execution) vulnerability.
   Execute the script and inject a command to trick it into reading the secret.
   Example: ./vulnping.sh "; cat secret.txt"
   
3. CONNECT FLAG: Some files are hidden by the system. Use 'ls -la' to reveal 
   files that start with a dot (.), then read them.

[SUBMISSION PROTOCOL]:
We have provisioned the 'submit_flag.py' tool in this directory for you.
To submit a flag, run it using Python 3:

Usage: python3 submit_flag.py FLAG{YOUR_FLAG_HERE}
================================================
"""
    with open(os.path.join(path, "briefing.txt"), "w") as f:
        f.write(briefing)

if __name__ == "__main__":
    deploy(sys.argv[1])
