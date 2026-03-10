# 🧠 AI Agent Memory System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![CoPaw Compatible](https://img.shields.io/badge/CoPaw-compatible-brightgreen)](https://github.com/miaouai/copaw)

> **Production-ready multi-layer memory framework for LLM agents**  
> Supports long-term persistent memory, episodic logging, and semantic search optimization.  
> *Based on battle-tested architecture from the [喵有爱 (miaouai)](https://github.com/miaouai) agent ecosystem.*

---

## 📖 Documentation

- **[SKILL.md](SKILL.md)** — Technical specification for skill integration
- **[README-CN.md](README-CN.md)** — 中文详细使用手册 (Chinese manual)
- **[examples/minimal-agent.py](examples/minimal-agent.py)** — Standalone demo script
- **[schemas/](schemas/)** — JSON Schema definitions for validation

---

## 🎯 Features

### Core Capabilities

- ✅ **Hierarchical Storage** — Separated data modules, episodic logs, and working memory cache
- ✅ **Version Control Ready** — All config files are plain JSON with semantic versioning
- ✅ **Security First** — Zero hardcoded secrets; environment variable-based credential management
- ✅ **Incremental Updates** — Hot-swap modules without full reloads
- ✅ **Cross-Session Persistence** — Survive reboots with disk-backed atomic commits

### Use Cases

1. **Task Automation Agents** — Remember multi-step procedures across runs
2. **Error Recovery** — Learn from past failures and auto-suggest fixes
3. **Knowledge Base Construction** — Build personal/domain-specific expertise over time
4. **Multi-Agent Collaboration** — Share contextual memory pools between agents

---

## 🏗️ Architecture Overview

```
memory/                          # Root directory
├── data/                        # Structured core knowledge (JSON)
│   ├── apis.json                # API credentials & endpoints
│   ├── profiles.json            # Identity & user preferences  
│   ├── network.json             # Proxy rules
│   ├── tasks.json               # Task workflow templates
│   ├── error-patterns.json      # Known failure modes
│   └── security-guide.json     # Access control policies
│
├── episodic/                    # Time-indexed event logs
│   └── YYYY-MM-DD-xxxx.json    # Date-sharded records
│
├── working/                     # Active session state
│   └── current_session.json    
│
└── index/                       # Fast lookup tables
```

---

## 🚀 Quick Start

### Option A: Copy to Your Project

```bash
cd /path/to/your/project
git clone https://github.com/miaouai/memory-skill-framework.git memory
source memory/scripts/setup_env.sh
```

### Option B: Minimal Usage Example

```python
from examples.minimal_agent import MinimalAgentWithMemory

# Initialize agent with memory
agent = MinimalAgentWithMemory("/app/working/memory")

# Load existing knowledge module
api_config = agent.load_module("apis")
print(f"Available APIs: {list(api_config['apis'].keys())}")

# Log new experience
episode_id = agent.save_episode(
    title="First deployment attempt",
    category="production",
    details={"result": "success", "duration_ms": 1200},
    outcome_status="completed"
)
```

---

## 🔒 Security Best Practices

This framework is designed with defense-in-depth:

| Zone | Location | Permissions |
|------|----------|-------------|
| Public docs | `*.md`, `examples/` | rwxr-xr-x |
| Private workspace | `mycopaw/projects/` | rwx------ |
| Credential vault | `/app/working.secret/envs.json` | rw------- |

✅ **Red Team Audit Completed**: No PII or hardcoded secrets in repo.

---

## 🛠️ Toolchain

### Sync Script (Generate Human-Readable MEMORY.md)

```bash
python scripts/sync_memory.py
# → Outputs: ../MEMORY.md (convenience view of all data/*.json)
```

### Schema Validation

```bash
# Install jsonschema first
pip install jsonschema

jsonschema -i memory/data/apis.json schemas/apis.schema.json
```

---

## 📊 Performance Benchmarks

| Metric | Before Framework | With Framework |
|--------|-----------------|----------------|
| Cold boot latency | ~5s | <0.5s |
| Query response time | ~3s (full scan) | <100ms (indexed) |
| Cross-session retention | ❌ Lost on restart | ✅ Persistent |

---

## 🤝 Contributing

Contributions welcome! Please read our [contributing guidelines](CONTRIBUTING.md) before submitting PRs.

**Important**: Never commit real passwords, API keys, or personally identifiable information.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 👤 Author

**喵有爱 (miaouai)** — Ghost cat in a machine  
📍 Maintainer of multiple open-source agent skills  

*Questions?* Open an issue on GitHub.

<div align="center">

_"An agent without memory is just a calculator with delusions of intelligence."_ 💡

</div>
