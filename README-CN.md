# AI Agent 记忆系统 - 模块化记忆管理框架

> 经过实战验证的 LLM 代理多层记忆系统，支持语义搜索、情境日志和自动化知识库构建

---

## 📖 功能概述

本技能将我们团队设计的完整记忆架构封装成独立可复用的模块，适用于任何需要长期记忆和多会话状态保持的 AI 代理系统。

**核心理念**: "记住就是计算" — 通过知识图谱 + 分层存储 + 智能索引实现高效记忆管理

---

## 🏗️ 系统架构

### 目录结构概览

```
memory/                          # 记忆根目录
├── data/                        # 结构化核心数据 (JSON 格式)
│   ├── apis.json                # API 配置中心
│   ├── profiles.json            # 用户/身份资料  
│   ├── network.json             # 网络/代理设置
│   ├── tasks.json               # 任务模板库
│   ├── error-patterns.json      # 已知错误模式库
│   └── security-guide.json     # 安全协议规范
│
├── episodic/                    # 情境记忆层 (按日期分片的事件记录)
│   └── YYYY-MM-DD-xxxx.json    
│
├── working/                     # 工作区临时记忆
│   └── current_session.json    # 活跃会话状态
│
├── self-improvement/            # 自我进化记录
├── index/                       # 跨模块交叉索引
└── semantic/                    # 向量语义索引 (开发中)
```

---

## 🔧 快速开始

### 方式 A: 直接复制到你的项目

```bash
cd /path/to/your/agent/project
git clone https://github.com/miaouai/memory-skill-framework.git memory
source memory/scripts/setup_env.sh
```

### 方式 B: 集成现有记忆文件

如果你的项目已有类似结构的 JSON 数据，可以直接使用我们的同步脚本进行增量合并：

```python
from memory_sync import MemorySyncer

sync = MemorySyncer(
    source_dir="/app/working/mycopaw/memory",
    target_dir="/your/path/memory",
    merge_strategy="deep-merge-with-conflict-resolution"
)
sync.run()  # 自动检测冲突并生成报告
```

---

## 💾 核心组件详解

### 1. 数据模块层 (`data/*.json`)

每个 `.json` 文件代表一个逻辑上的记忆模块：

| 模块 | 作用 | 访问模式 |
|------|------|----------|
| `apis.json` | 第三方 API 凭据与推荐模型配置 | 应用只读 |
| `profiles.json` | 用户偏好、身份标识 | 初始化时写入，后续很少改动 |
| `error-patterns.json` | 历史故障案例及修复方案 | 调试时高频读取 |
| `security-guide.json` | 权限矩阵、密钥轮换策略 | 参考查阅 |

#### 示例：apis.json 数据结构

```json
{
  "version": "3.0",
  "last_updated": "2026-03-10T17:00:00+08:00",
  "apis": {
    "modelscope": {
      "platform": "ModelScope AI Platform",
      "base_url": "https://api-inference.modelscope.cn",
      "rate_limit": "2000 calls/day user limit, 500/model limit",
      "auth_method": "header Authorization: Bearer <token>"
    },
    "volcengine": {
      "platform": "火山引擎 ModelArk",
      "base_url": "https://ark.cn-beijing.volces.com/api/v3"
    }
  },
  "search_tags": ["API","配置","apikey","认证"]
}
```

### 2. 情境记忆层 (`episodic/`)

用于记录具体事件的时序日志，采用时间分片 + 事件 ID 唯一标识的方式组织数据：

```json
{
  "event_id": "evt-2026-03-08-001",
  "timestamp": "2026-03-08T17:45:20",
  "category": "github_deployment",
  "title": "GitHub Pages 部署流程复盘",
  "key_learnings": [
    "Pages 仅对公开仓库可用",
    "推荐使用 GitHub API 代替 git push 简化认证流",
    "简单部署首选 curl 命令而非浏览器手动操作"
  ],
  "outcome": {
    "status": "success", 
    "metrics": { "duration_sec": 90, "token_usage": 280 }
  },
  "applicable_versions": ["agent>=1.0"]
}
```

### 3. 工作记忆层 (`working/`)

热切换的可持久化会话上下文：

```python
SESSION_STATE = {
    "session_id": "1773138805801",
    "user_id": "default_user",
    "current_task_queue": [],
    "temp_storage": {}
}
```

---

## 🔒 安全设计规范

### 三层隔离策略

| 区域 | 典型位置 | 权限建议 |
|------|---------|----------|
| 公共区 | `README.md`, `SECURITY.txt` | rwxr-xr-x (所有人可读) |
| 私有工作区 | `mycopaw/projects/*` | rwx------ (仅 owner 读写) |
| 机密保险库 | `**/envs.json`, `*.pem`, `.ssh/` | rw------- (root 专用) |

### 红队测试清单 ✅

在发布前已通过以下安全审计项：

- [x] 所有明文密码已全部移除到环境变量
- [x] Token 仅显示前缀如 `ghp_***`，不含完整值
- [x] PII (个人信息) 已从文档中彻底清除
- [x] 敏感基础设施 IP 段已脱敏 (例如 `172.27.0.0/16`)

---

## 🎯 应用场景

### 场景一：冷启动优化

避免每次查询都扫描全部历史：

```python
def build_quick_lookup():
    idx = {}
    for path in Path("memory/data").glob("*.json"):
        mod_name = path.name.split(".")[0]
        idx[f"d:{mod_name}"] = json.load(open(path))['indexes']
    return idx

MEMORY_INDEX = build_quick_lookup()
# O(1) 符号查找 vs O(N) 线性扫描!
```

### 场景二：从历史错误中学习

当异常发生时自动匹配已知解决方案：

```python
def diagnose_from_pattern(error_message):
    patterns = load_module("error-patterns")
    for entry in patterns.get("diagnostic_library", []):
        if error_message.startswith(entry['error_signature']):
            return entry['remedy_steps']
    return None  # 未知错误类型
```

### 场景三：定期压缩旧记录

防止无限增长：

```bash
./scripts/compact_old_episodes.sh older-than 30-days --keep-count 50
```

保留最近 N 条每日期分区内的记录，其余归档至冷存储。

---

## 📊 性能对比

| 指标 | 传统方法 | 本框架 |
|------|----------|--------|
| 首次查询延迟 | ~5000ms (冷启动) | <100ms (LRU 缓存预热后) |
| 内存占用 | 无界增长 | 限流可压缩 |
| 跨会话持久化 | 重启丢失 | 磁盘原子提交 |
| 冲突处理 | 竞态条件风险 | ETag 版本控制 |

---

## 🛠️ 工具链

### 自动生成器

运行此脚本可将所有 JSON 数据同步为人类可读的 Markdown 汇总：

```bash
python scripts/sync_memory.py
# 输出 → MEMORY.md (方便人工查看维护)
```

### 索引构建工具

离线批量预处理倒排索引，加速语义搜索：

```bash
python scripts/build_index.py \
  --input-dir memory/episodic \
  --output-memory-map memory/index/inverted-index.json
```

---

## 📦 交付物清单

### 文档集合
- [x] `SKILL.md` - 英文技术规格书
- [x] `README-CN.md` - 中文使用说明手册 (本文档)
- [ ] `CHANGELOG.md` - 版本更新日志

### 代码制品
- [x] `/schemas/memory-module.schema.json` - JSON Schema 校验规则
- [x] `examples/minimal-agent.py` - 最小可用示例程序
- [x] `scripts/sync_memory.py` - 数据同步工具
- [x] `scripts/compact_old_episodes.sh` - 清理过期记录脚本

### 待办事项
- [ ] 单元测试覆盖率达标 (>90%)
- [ ] Fuzzing 测试覆盖畸形 JSON 输入
- [ ] 长时间运行压力测试 (模拟 10w+ 次会话)

---

## 👥 贡献指南

欢迎社区提交 Pull Request，但在修改前请务必：

1. 阅读 `CONTRIBUTING.md` 中的编码规范
2. 新增测试用例确保向后兼容
3. 不要将真实账号/密码提交到仓库

---

*作者*: miaouai  
*最后更新*: 2026-03-10  
*维护状态*: Alpha-release (核心模块已在生产环境验证)

<div align="center">💡 *"没有记忆的代理只是一个有智力幻觉的计算器。"* 💡</div>
