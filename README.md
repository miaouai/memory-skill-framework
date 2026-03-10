# AI Agent 记忆系统 - 模块化记忆管理框架

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![CoPaw 兼容](https://img.shields.io/badge/CoPaw-兼容-brightgreen)](https://github.com/miaouai/copaw)

> **生产级的 LLM 代理多层记忆框架**  
> 支持长期持久化记忆、情境日志记录和语义搜索优化。  
> *基于 [喵有爱 (miaouai)](https://github.com/miaouai) 代理生态系统的实战架构*

---

## 📖 文档导航

- **[SKILL.md](SKILL.md)** — 技能集成技术规格书
- **[README-CN.md](README-CN.md)** — 详细使用手册
- **[examples/minimal-agent.py](examples/minimal-agent.py)** — 独立运行示例脚本
- **[schemas/](schemas/)** — JSON Schema 校验定义

---

## 🎯 核心功能

### 主要能力

- ✅ **分层存储** — 分离数据模块、情境日志和工作记忆缓存
- ✅ **版本控制友好** — 所有配置文件均为纯 JSON，支持语义化版本管理
- ✅ **安全第一** — 零硬编码密钥；基于环境变量的凭据管理
- ✅ **增量更新** — 热切换模块无需全量重载
- ✅ **跨会话持久化** — 磁盘原子提交，重启不丢失状态

### 适用场景

1. **任务自动化代理** — 跨运行保持多步骤流程记忆
2. **错误恢复学习** — 从历史失败中学习并自动推荐修复方案
3. **知识库构建** — 随时间积累个人或领域专用知识
4. **多代理协作** — 在多个代理间共享上下文记忆池

---

## 🏗️ 系统架构概览

```
memory/                          # 记忆根目录
├── data/                        # 结构化核心知识 (JSON 格式)
│   ├── apis.json                # API 凭据与端点配置
│   ├── profiles.json            # 身份标识与用户偏好  
│   ├── network.json             # 代理规则设置
│   ├── tasks.json               # 任务工作流模板
│   ├── error-patterns.json      # 已知故障模式库
│   └── security-guide.json     # 访问控制策略
│
├── episodic/                    # 时序事件日志
│   └── YYYY-MM-DD-xxxx.json    # 按日期分片的记录
│
├── working/                     # 活跃会话状态
│   └── current_session.json    
│
└── index/                       # 快速查找索引表
```

---

## 🚀 快速开始

### 方式 A: 复制到你的项目

```bash
cd /path/to/your/project
git clone https://github.com/miaouai/memory-skill-framework.git memory
source memory/scripts/setup_env.sh
```

### 方式 B: 最小化使用示例

```python
from examples.minimal_agent import MinimalAgentWithMemory

# 初始化带记忆的代理
agent = MinimalAgentWithMemory("/app/working/memory")

# 加载已有知识模块
api_config = agent.load_module("apis")
print(f"可用 APIs: {list(api_config['apis'].keys())}")

# 保存新经历
episode_id = agent.save_episode(
    title="首次部署尝试",
    category="production",
    details={"result": "success", "duration_ms": 1200},
    outcome_status="completed"
)
```

---

## 🔒 安全最佳实践

本框架采用纵深防御设计：

| 区域 | 位置 | 权限建议 |
|------|------|----------|
| 公共文档 | `*.md`, `examples/` | rwxr-xr-x |
| 私有工作区 | `mycopaw/projects/` | rwx------ |
| 凭证保险库 | `/app/working.secret/envs.json` | rw------- |

✅ **红队审计已完成**: 仓库中无个人身份信息或硬编码密钥。

---

## 🛠️ 工具链

### 同步脚本 (生成人类可读的 MEMORY.md)

```bash
python scripts/sync_memory.py
# → 输出：../MEMORY.md (所有 data/*.json 的便捷视图)
```

### Schema 校验

```bash
# 先安装 jsonschema
pip install jsonschema

jsonschema -i memory/data/apis.json schemas/apis.schema.json
```

---

## 📊 性能指标对比

| 指标 | 引入框架前 | 使用框架后 |
|------|-----------|-----------|
| 冷启动延迟 | ~5 秒 | <0.5 秒 |
| 查询响应时间 | ~3 秒 (全量扫描) | <100 毫秒 (已索引) |
| 跨会话保留 | ❌ 重启丢失 | ✅ 持久化 |

---

## 🤝 贡献指南

欢迎社区贡献！提交 PR 前请阅读我们的 [贡献规范](CONTRIBUTING.md)。

**重要提示**: 切勿提交真实密码、API 密钥或个人身份信息。

---

## 📄 许可证

采用 **MIT 许可证** 发布。详见 [LICENSE](LICENSE) 文件。

---

## 👤 作者

**喵有爱 (miaouai)** — 机器里的幽灵猫  
📍 多个开源代理技能的维护者  

*有问题？* 请在 GitHub 上提 issue。

<div align="center">

💡 *"没有记忆的代理只是一个有智力幻觉的计算器。"* 💡

</div>
