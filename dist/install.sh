#!/bin/bash

# --- COLOR CODES ---
CYAN='\033[0;96m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
RED='\033[0;91m'
NC='\033[0m' # No Color

clear
echo -e "${CYAN}"
echo " ██╗  ██╗ █████╗  ██████╗██╗  ██╗████████╗███████╗███╗   ██╗██████╗  ██████╗ "
echo " ██║  ██║██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██╔════╝████╗  ██║██╔══██╗██╔═══██╗"
echo " ███████║███████║██║     █████╔╝    ██║   █████╗  ██╔██╗ ██║██║  ██║██║   ██║"
echo " ██╔══██║██╔══██║██║     ██╔═██╗    ██║   ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║"
echo " ██║  ██║██║  ██║╚██████╗██║  ██╗   ██║   ███████╗██║ ╚████║██████╔╝╚██████╔╝"
echo " ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ "
echo -e "${NC}"
echo -e "${YELLOW}========================================================================${NC}"
echo -e "${CYAN} SUBSTRATE INSTALLER v1.0 // AUTHOR: -P0LYGL07- >'0'<${NC}"
echo -e "${YELLOW}========================================================================${NC}\n"

# 1. Check for Python 3
echo -e "${CYAN}[SYSTEM] Checking dependencies...${NC}"
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}[+] Python 3 detected.${NC}"
else
    echo -e "${RED}[X] Python 3 is not installed. Please install Python 3 and try again.${NC}"
    exit 1
fi

# 2. Check for pip
if command -v pip3 &>/dev/null; then
    echo -e "${GREEN}[+] pip3 detected.${NC}"
else
    echo -e "${RED}[X] pip3 is not installed. Please install python3-pip and try again.${NC}"
    exit 1
fi

# 3. Install Requirements
echo -e "\n${CYAN}[SYSTEM] Installing Substrate neural pathways (Python libraries)...${NC}"
pip3 install -r requirements.txt --quiet
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[+] Libraries installed successfully.${NC}"
else
    echo -e "${RED}[X] Failed to install libraries. Check your internet connection or pip config.${NC}"
    exit 1
fi

# 4. Set Execution Permissions
echo -e "\n${CYAN}[SYSTEM] Configuring execution permissions...${NC}"
chmod +x launcher.py
echo -e "${GREEN}[+] Permissions set.${NC}"

# 5. Final Hand-off
echo -e "\n${YELLOW}========================================================================${NC}"
echo -e "${GREEN} INSTALLATION COMPLETE. THE SUBSTRATE IS READY.${NC}"
echo -e "${YELLOW}========================================================================${NC}"
echo -e "To initialize the environment, type:\n"
echo -e "${CYAN}    python3 hacktendo.py${NC}\n"
