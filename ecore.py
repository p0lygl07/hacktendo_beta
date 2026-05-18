# HACKTENDO // ecore.py - Intelligence Multiplexer (Beta v1.0)
import os, json
from flask import jsonify, request, send_from_directory
import pcore

def init_expansion(app, socketio, ledger):
    print("[+] E-CORE: Initializing Intelligence Multiplexer...")

    def bind_route(url, name, func, methods=['GET']):
        app.add_url_rule(url, name, func, methods=methods)

    # --- 1. STATUS MONITOR ---
    @app.route('/api/e/status', methods=['GET', 'POST'])
    def e_api_status():
        # Check for user handle to provide a personalized status
        data = request.json if request.is_json else {}
        handle = data.get('handle', 'UNKNOWN_OPERATOR')
        return jsonify({
            "status": "ONLINE",
            "operator": handle,
            "cores": {
                "P-CORE": "ACTIVE",
                "T-CORE": "ACTIVE",
                "X-CORE": "RESTRICTED",
                "M-CORE": "RESTRICTED"
            }
        })

    # --- 2. EXPANSION ATTEMPTS (The Paywall Logic) ---
    
    # X-CORE (Stealth)
    try:
        import xcore
        xcore.x_logic_init(app, bind_route)
    except ImportError:
        print("[!] X-CORE: Restricted (Requires Expansion Pack)")

    # M-CORE (World Map)
    try:
        import mcore
        mcore.m_logic_init(app, bind_route)
    except ImportError:
        @app.route('/ncore')
        def ncore_beta():
            return "<h3>[!] M-CORE ACCESS DENIED</h3><p>Satellite Uplink requires HACKTENDO Pro Subscription.</p>", 403
        print("[!] M-CORE: Restricted (Requires Expansion Pack)")

    # --- 3. IDENTITY VERIFICATION ---
    if pcore:
        print("[+] E-CORE: P-Core Handshake Verified.")
