#!/usr/bin/env python3
"""
demo_state.py - Demo script to simulate main agent state transitions

This script periodically updates the state.json file with random states.
It simulates the agent being in different phases like "idle", "writing", 
or "researching", and is used for verifying displays in external tools 
and dashboards.
"""

import time
import json
import os
import sys
import random
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(ROOT_DIR, "state.json")

# List of states for the main agent (Star)
DEMO_STATES = [
    {"state": "idle",        "detail": "Idle, ready to work"},
    {"state": "writing",     "detail": "Organizing documents..."},
    {"state": "researching", "detail": "Researching latest information..."},
    {"state": "executing",   "detail": "Executing tasks..."},
    {"state": "syncing",     "detail": "Syncing backups..."},
    {"state": "error",       "detail": "Error detected, investigating..."},
]

def save_state(state_dict):
    """Save the state to state.json"""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state_dict, f, ensure_ascii=False, indent=2)

def run_demo_loop(interval=5):
    """Continuously update the main agent's state randomly"""
    print("=" * 50)
    print("  Star Office UI - Demo Mode Started (Random Update)")
    print("=" * 50)
    print(f"  Switching states randomly every {interval} seconds")
    print("  Press Ctrl+C to stop")
    print()

    while True:
        s = random.choice(DEMO_STATES)
        now = datetime.now().isoformat()

        state_dict = {
            "state": s["state"],
            "detail": s["detail"],
            "progress": random.randint(0, 100),
            "updated_at": now,
            "ttl_seconds": 300
        }
        save_state(state_dict)

        print(f"[{now}] State: {s['state']} (Progress: {state_dict['progress']}%) - {s['detail']}")
        time.sleep(interval)

if __name__ == "__main__":
    # Update interval (seconds) can be specified via command line argument (default: 5s)
    interval = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    try:
        run_demo_loop(interval)
    except KeyboardInterrupt:
        print("\n  Demo mode stopped.")
