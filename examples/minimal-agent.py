#!/usr/bin/env python3
"""Minimal Agent Example - Demonstrates basic memory system usage"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
import uuid

class MinimalAgentWithMemory:
    """A tiny agent that demonstrates loading and writing memory modules."""
    
    def __init__(self, memory_base_path: str = "memory"):
        self.memory_base = Path(memory_base_path)
        self.data_dir = self.memory_base / "data"
        self.episodic_dir = self.memory_base / "episodic"
        self.working_dir = self.memory_base / "working"
        
        # Ensure directories exist
        for d in [self.data_dir, self.episodic_dir, self.working_dir]:
            d.mkdir(parents=True, exist_ok=True)
        
        print(f"[+] Memory base initialized at {self.memory_base.resolve()}")
    
    def load_module(self, module_name: str) -> Dict[str, Any]:
        """Load a JSON module from data/ directory."""
        path = self.data_dir / f"{module_name}.json"
        if not path.exists():
            raise FileNotFoundError(f"Module not found: {path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_episode(
        self,
        title: str,
        category: str,
        details: Dict[str, Any],
        outcome_status: str = "completed"
    ) -> str:
        """Write a new episodic memory record."""
        episode_id = f"ep-{uuid.uuid4().hex[:12]}"
        today = datetime.now().strftime("%Y-%m-%d")
        
        record = {
            "event_id": episode_id,
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "title": title,
            "details": details,
            "outcome": {
                "status": outcome_status,
                "metrics": {}
            }
        }
        
        # Date-sharded file name
        filename = f"{today}-{len(details)}.json"
        output_path = self.episodic_dir / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(record, f, ensure_ascii=False, indent=2)
        
        print(f"[✓] Episode saved: {output_path}")
        return episode_id
    
    def get_session_state(self) -> Dict[str, Any]:
        """Retrieve current working memory."""
        state_file = self.working_dir / "current_session.json"
        if state_file.exists():
            return json.load(open(state_file, 'r'))
        return {"session_id": str(uuid.uuid4()), "tasks": []}
    
    def set_session_state(self, data: Dict[str, Any]) -> None:
        """Update working memory."""
        state_file = self.working_dir / "current_session.json"
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[✓] Session state updated")


# ============ DEMO USAGE ============

if __name__ == "__main__":
    # 1. Initialize the agent
    agent = MinimalAgentWithMemory("/app/working/memory")
    
    # 2. Load an existing module (if available)
    try:
        api_config = agent.load_module("apis")
        print(f"\n[📊] Loaded apis.json (version {api_config.get('version', '?')})")
        print(f"   Available APIs: {list(api_config.get('apis', {}).keys())}")
    except FileNotFoundError:
        print("\n[!] No apis.json found - skipping demo load step")
    
    # 3. Simulate an episodic event
    print("\n[🔄] Creating test episode...")
    ep_id = agent.save_episode(
        title="Minimal Agent Demo Run",
        category="testing",
        details={
            "what_we_did": "Instantiate MinimalAgentWithMemory class",
            "modules_loaded": ["apis"],
            "notes": "This is a demonstration of the memory framework"
        },
        outcome_status="success"
    )
    print(f"   Episode ID: {ep_id}")
    
    # 4. Check session state
    state = agent.get_session_state()
    print(f"\n[📝] Current session ID: {state.get('session_id', 'N/A')}")
    
    print("\n✅ Demo completed successfully!")
