# Hacktendo 👾 — Hacker Simulation Platform

> A browser-based cybersecurity simulation and education platform with a live terminal, RPG economy, mission system, and NPC-driven narrative. Built for operators who learn by doing.

---

## What Is Hacktendo?

Hacktendo is a self-hosted hacker simulation environment that runs in your browser. It combines a real Linux terminal, a gamified progression system, and a mission-based learning architecture into a single cohesive platform.

You play as an operator navigating a cyberpunk substrate — completing missions, earning HXT currency, building your tool arsenal, and advancing through factions. Every mechanic is grounded in real cybersecurity concepts.

---

## Features

- **Live Terminal** — Real PTY shell via SocketIO. Not simulated. Actual command execution in a sandboxed environment.
- **HXT Economy** — In-platform currency earned through missions, labs, and passive node income. Spend it on tools, upgrades, and cartridges.
- **Mission Cartridge System** — ZIP-based mission payloads. Drop a cartridge in and the platform ingests, validates, and deploys the challenge automatically.
- **XP & Progression** — Level up from Script Kiddie to Vanguard. Karma system tracks your alignment — Blackhat, Whitehat, or somewhere in between.
- **NPC Layer** — Characters with memory and faction logic. Kage and Nyx respond differently based on your karma and history.
- **Tool Marketplace** — Purchase, import, and register tools to your operator deck. Includes a Warefac payload factory and Hex Decompiler.
- **World Map** — Visual node map showing your botnet infrastructure and active targets.
- **HXT Blockchain** — Custom distributed ledger tracking operator transactions and asset transfers natively inside the platform.
- **Modular UI** — Draggable windows, a persistent dock, and a threat tracker HUD. Runs entirely in browser.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask, Flask-SocketIO |
| Frontend | HTML5, CSS3, Vanilla JS |
| Terminal | PTY via subprocess |
| Economy | Custom HXT ledger (chain_core.py) |
| Missions | ZIP cartridge ingestion engine |
| State | JSON flat files (GHOST.json, tool_library.json) |

---

## Installation

**Requirements:** Python 3.8+, pip, Linux or WSL recommended

```bash
# Clone the repo
git clone https://github.com/p0lygl07/hacktendo_beta.git
cd hacktendo_beta

# Install dependencies
pip install -r requirements.txt

# Or use the install script
chmod +x install.sh
./install.sh

# Launch
python3 core.py
```

Then open your browser to `http://localhost:5000`

---

## Project Structure

```
hacktendo_beta/
├── core.py              # Main Flask/SocketIO engine
├── ecore.py             # Terminal & radar engine
├── pcore.py             # Player profile & progression
├── tcore.py             # Tool registry & marketplace
├── chain_core.py        # HXT blockchain ledger
├── deck.html            # Main operator dashboard
├── edeck.html           # Terminal interface
├── tdeck.html           # Tool deck
├── profile.html         # Operator dossier
├── worldmap.html        # Node map
├── cartridges/          # Mission payloads
├── ui/                  # UI assets
└── v-net/               # Network layer
```

---

## Mission Cartridges

Missions are self-contained ZIP packages with a `manifest.json` defining objectives, flags, rewards, and story. Drop them into the cartridges directory or install via the in-platform loader.

An example cartridge structure:
```
pack_mission_name.zip
├── manifest.json        # Mission metadata, objectives, HXT reward
├── target.html          # Challenge environment
└── solution.py          # (Optional) solve script for operators
```

---

## Status

**Beta — Active Development**

Core systems are stable. Known areas in active development:
- Academy module (courses.html) — cybersecurity curriculum integration
- SQL migration — moving from JSON flat files to persistent database
- P2P connectivity — real-time operator coordination layer
- Shadow Browser — in-platform .ht domain navigation

---

## Operator

Built and maintained by **Joshua Burton (p0lygl07)**

- HackerDNA: [hackerdna.com/users/3xp07](https://hackerdna.com/users/3xp07)
- YouTube: [@p0lygl07](https://youtube.com/@p0lygl07)
- LinkedIn: [joshua-burton-02b1573ba](https://linkedin.com/in/joshua-burton-02b1573ba)

---

## License

Personal use and educational use permitted. Commercial redistribution requires written authorization from the author.

---

*The Substrate is live. Initialize your operator profile and begin.*
