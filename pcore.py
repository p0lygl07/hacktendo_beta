# HACKTENDO // pcore.py - Identity-Aware Resilient Sync Engine
import os, json
from flask import jsonify, request

# Absolute path locking to prevent directory desync
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILE_DIR = os.path.join(BASE_DIR, "profiles")

def get_profile_path(handle):
    if not handle: return None
    os.makedirs(PROFILE_DIR, exist_ok=True)
    return os.path.join(PROFILE_DIR, f"{handle}.json")

def safe_num(val, as_int=False):
    try:
        num = float(str(val).replace(',', '').strip())
        return int(num) if as_int else num
    except:
        return 0 if as_int else 0.0

def load_profile(handle=None):
    DATA_PATH = get_profile_path(handle)
    
    # Baseline Template
    profile = {
        "handle": handle, "level": 1, "xp": 0, "xp_to_next": 100, 
        "karma": 0, "ledger": 1000.0, "rank": "Operator", "total_xp": 0,
        "specialization": "Neutral", "inventory": []
    }
    
    if DATA_PATH and os.path.exists(DATA_PATH):
        try:
            with open(DATA_PATH, 'r') as f:
                data = json.load(f)
            
            profile['ledger'] = safe_num(data.get('ledger', data.get('currency', 1000.0)))
            profile['karma'] = safe_num(data.get('karma', data.get('alignment', 0)), as_int=True)
            profile['total_xp'] = safe_num(data.get('total_xp', data.get('xp', 0)), as_int=True)
            
            # --- GEOMETRIC SCALING ---
            temp_xp = profile['total_xp']
            calc_level, next_tier = 1, 100
            while temp_xp >= next_tier:
                calc_level += 1
                temp_xp -= next_tier
                next_tier = int(next_tier * 1.5)
            
            profile['level'], profile['xp'], profile['xp_to_next'] = calc_level, temp_xp, next_tier
            
            # --- ROLE PERSISTENCE LOGIC ---
            profile['rank'] = "Vanguard" if profile['level'] >= 10 else "Operator"
            
            if profile['karma'] >= 50: 
                profile['specialization'] = "Sentinel"
            elif profile['karma'] <= -50: 
                profile['specialization'] = "Spectre"
            else:
                profile['specialization'] = "Neutral"
            
            # Merge dynamic keys (inventory, nodes, etc.)
            for k, v in data.items():
                if k not in ['ledger', 'karma', 'total_xp', 'xp', 'level', 'rank', 'specialization']:
                    profile[k] = v
        except: pass
    return profile

def save_profile(data, handle=None):
    if not handle: return
    DATA_PATH = get_profile_path(handle)
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, 'w') as f: json.dump(data, f, indent=4)

def add_progress(handle=None, xp_gain=0, karma_change=0, hxt_gain=0, hxt_cost=0):
    profile = load_profile(handle)
    profile['total_xp'] += safe_num(xp_gain, as_int=True)
    profile['karma'] += safe_num(karma_change, as_int=True)
    profile['ledger'] = profile['ledger'] + safe_num(hxt_gain) - safe_num(hxt_cost)
    save_profile(profile, handle)
    return load_profile(handle)

def p_logic_init(app, bind_route):
    print("[+] P-CORE: Identity-Aware Sync Engine Mounted.")

    @app.route('/api/p/profile', methods=['GET', 'POST'])
    def p_api_get_profile():
        handle = request.args.get('handle')
        if request.method == 'POST':
            handle = (request.json or {}).get('handle', handle)
        if not handle: return jsonify({"error": "IDENTITY_MISSING"}), 400
        return jsonify(load_profile(handle))

    @app.route('/api/p/report', methods=['POST'])
    def p_api_report_action():
        data = request.json or {}
        handle = data.get('handle')
        if not handle: return jsonify({"error": "IDENTITY_MISSING"}), 400
        new_stats = add_progress(handle=handle, xp_gain=data.get('xp', 0), 
                                 karma_change=data.get('karma', 0), 
                                 hxt_gain=data.get('hxt_gain', 0), hxt_cost=data.get('hxt_cost', 0))
        return jsonify({"success": True, "stats": new_stats})
