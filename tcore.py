# HACKTENDO // tcore.py - Tool Engine with Dynamic Identity & Feature Gating
import os, json
from flask import jsonify, request

try:
    import pcore
except ImportError:
    pcore = None

# Ensure the cartridges directory exists for the library
LIB_FILE = "cartridges/tool_library.json"
os.makedirs("cartridges", exist_ok=True)

# --- THE GATEKEEPER CONFIG ---
# Tools listed here will trigger the DEMO-VERSION alert
PRO_TOOLS = [
    "satellite_uplink", 
    "fiber_tap", 
    "auto_scrub_v2", 
    "quantum_ghost",
    "ncore_map",
    "white_arts_toolkit"
]

def get_lib():
    if os.path.exists(LIB_FILE):
        try:
            with open(LIB_FILE, 'r') as f: return json.load(f)
        except: return {}
    return {}

def save_lib(data):
    with open(LIB_FILE, 'w') as f: json.dump(data, f, indent=4)

def t_logic_init(app, bind_route):
    print("[+] T-CORE: Gatekeeper Protocol & Dynamic Identity Active.")

    # --- 1. LOGIC FUNCTIONS ---

    def t_api_manual_reg():
        data = request.json
        handle = data.get('handle')
        if not handle: return jsonify({"success": False, "msg": "IDENTITY_REQUIRED"}), 400
        
        lib = get_lib()
        name = data.get('name', 'unknown').lower()

        # BLOCK: Prevent manual registration of Pro tools in Beta
        if name in PRO_TOOLS:
            return jsonify({
                "success": False, 
                "msg": "DEMO-VERSION: Restricted Tool",
                "action": "UPGRADE_REQUIRED"
            }), 403

        lib[name] = {"desc": data.get('desc', "Local Tool"), "usage": f"{name} --help", "cat": "manual"}
        save_lib(lib)
        
        if pcore: 
            pcore.add_progress(handle=handle, xp_gain=50, karma_change=2)
            
        return jsonify({"success": True, "msg": f"Indexed {name} for @{handle}."})

    def t_api_lookup(name):
        tool_name = name.lower()
        
        # 1. CHECK THE PAYWALL FIRST
        if tool_name in PRO_TOOLS:
            return jsonify({
                "success": False, 
                "msg": "DEMO-VERSION: Access Restricted",
                "upgrade_path": "/paid-expansion"
            }), 403

        # 2. CHECK THE LOCAL LIBRARY SECOND
        lib = get_lib()
        tool = lib.get(tool_name)
        if tool:
            return jsonify({"success": True, "tool": tool})
        return jsonify({"success": False, "msg": "Tool not found"}), 404

    def t_api_purchase():
        data = request.json
        handle = data.get('handle')
        tool_id = data.get('id', '').lower()
        
        if not handle: return jsonify({"success": False, "msg": "IDENTITY_REQUIRED"}), 400
        
        # GATE: Prevent purchase of Pro tools
        if tool_id in PRO_TOOLS:
            return jsonify({
                "success": False, 
                "msg": "DEMO-VERSION: Expansion Required",
                "details": "Purchase the full HACKTENDO substrate to unlock Satellite-tier tools."
            }), 403

        if not pcore: return jsonify({"success": False, "msg": "P-CORE_OFFLINE"}), 500
        
        try:
            cost = float(str(data.get('cost', 0)).replace(',', '').strip())
            profile = pcore.load_profile(handle)
            
            # Check against the specific user's ledger
            user_balance = float(profile.get('ledger', 0) if 'ledger' in profile else profile.get('currency', 0))
            
            if user_balance >= cost:
                pcore.add_progress(handle=handle, hxt_cost=cost) 
                
                lib = get_lib()
                lib[tool_id] = {"desc": f"Purchased: {tool_id}", "usage": f"{tool_id} --run", "cat": "market"}
                save_lib(lib)
                
                return jsonify({"success": True, "msg": f"Verified for @{handle}."})
            
            return jsonify({"success": False, "msg": "INSUFFICIENT_HXT"})
        except Exception as e:
            return jsonify({"success": False, "msg": str(e)}), 500

    # --- 2. ROUTE BINDINGS ---
    bind_route('/api/tools/wiki', 't_api_get_wiki', lambda: jsonify(get_lib()))
    bind_route('/api/tools/register', 't_api_register', t_api_manual_reg, methods=['POST'])
    bind_route('/api/tools/purchase', 't_api_purchase', t_api_purchase, methods=['POST'])
    bind_route('/api/tools/lookup/<name>', 't_api_lookup', t_api_lookup, methods=['GET'])
