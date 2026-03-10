# 🧠 AI Agent 记忆系统

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![CoPaw 兼容](https://img.shields.io/badge/CoPaw-兼容-brightgreen)](https://github.com/miaouai/copaw)

> 生产级的 LLM 代理多层记忆框架 — 基于 [喵有爱 (miaouai)](https://github.com/miaouai) 代理生态系统的实战架构

---

## 📖 快速开始

### 作为 Copaw 技能安装

```bash
copaw skill install https://github.com/miaouai/memory-skill-framework
```

### 作为独立模块集成

```bash
git clone https://github.com/miaouai/memory-skill-framework.git memory
source memory/scripts/setup_env.sh
```

详细使用说明请查看 **[SKILL.md](SKILL.md)**

---

## 🎯 核心功能

- ✅ **分层存储** — 数据模块、情境日志、工作记忆缓存
- ✅ **持久化** — 磁盘原子提交，重启不丢失状态
- ✅ **安全第一** — 零硬编码密钥，环境变量管理凭据
- ✅ **版本友好** — 纯 JSON 配置，支持 Git 版本控制

---

## 📂 项目结构

```
memory-skill-framework/
├── SKILL.md              # ← Copaw 技能规格书（必读）
├── README.md             # 本文档
├── LICENSE               # MIT 许可证
├── examples/             # 示例代码
│   └── minimal-agent.py  # 最小可运行示例
├── scripts/              # 辅助脚本
│   ├── sync_memory.py    # 同步工具
│   └── build_index.py    # 索引构建器
└── schemas/              # JSON Schema 定义
```

---

## 🤝 贡献指南

欢迎社区贡献！提交 PR 前请注意：

1. **切勿提交**真实密码、API 密钥或个人身份信息
2. 新增测试用例确保向后兼容
3. 遵循现有文档风格

---

## 📄 许可证

采用 **MIT 许可证** 发布。

---

<div align="center">

💡 *"没有记忆的代理只是一个有智力幻觉的计算器。"* 💡

</div>
