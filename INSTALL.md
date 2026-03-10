# 安装指南

## 方式一：作为 Copaw 技能安装（推荐）

```bash
copaw skill install https://github.com/miaouai/memory-skill-framework
```

安装后，技能将自动加载到 `/app/working/active_skills/memory-skill-framework/`

### 验证安装

```bash
ls -la /app/working/active_skills/memory-skill-framework/
cat /app/working/active_skills/memory-skill-framework/SKILL.md
```

---

## 方式二：手动集成

```bash
cd /app/working/mycopaw/projects
git clone https://github.com/miaouai/memory-skill-framework.git
cd memory-skill-framework
```

### 初始化记忆目录

```bash
# 创建记忆目录结构
mkdir -p memory/{data,episodic,working,index}

# 初始化基础数据文件
cat > memory/data/apis.json << 'EOF'
{
  "version": "1.0",
  "apis": {}
}
EOF

cat > memory/data/profiles.json << 'EOF'
{
  "version": "1.0",
  "user": {}
}
EOF
```

---

## 方式三：作为 Python 模块使用

```python
from pathlib import Path
import json

def load_module(module_name: str, base_path: str = "memory/data"):
    """加载记忆模块"""
    p = Path(base_path) / f"{module_name}.json"
    if not p.exists():
        raise FileNotFoundError(f"模块不存在：{module_name}")
    return json.load(p.open('r', encoding='utf-8'))

# 使用示例
try:
    apis = load_module("apis")
    print(f"已加载 API 配置：{list(apis.keys())}")
except FileNotFoundError as e:
    print(f"错误：{e}")
```

---

## 故障排查

### 问题 1: 技能安装失败

**症状**: `copaw skill install` 报错

**解决方案**:
```bash
# 1. 检查网络连接
curl -I https://github.com/miaouai/memory-skill-framework

# 2. 验证 SKILL.md 格式
curl -s https://raw.githubusercontent.com/miaouai/memory-skill-framework/main/SKILL.md | head -20

# 3. 手动复制到 active_skills
cp -r /app/working/mycopaw/projects/memory-skill-framework \
      /app/working/active_skills/
```

### 问题 2: 记忆目录不存在

**症状**: 读取记忆文件时抛出 FileNotFoundError

**解决方案**:
```bash
# 运行初始化脚本
cd /app/working/mycopaw/projects/memory-skill-framework
bash scripts/setup_env.sh

# 或手动创建
mkdir -p memory/{data,episodic,working,index}
```

### 问题 3: GitHub Pages 无法访问

**症状**: https://miaouai.github.io/memory-skill-framework/ 返回 404

**解决方案**:
1. 等待 1-2 分钟（GitHub Pages 构建需要时间）
2. 检查分支设置：仓库 Settings → Pages → Source 应为 `main` 分支
3. 确认 `index.html` 存在于根目录

---

## 卸载

```bash
# Copaw 技能卸载
copaw skill uninstall memory-skill-framework

# 或手动删除
rm -rf /app/working/active_skills/memory-skill-framework
```

---

## 系统要求

- Python 3.8+
- CoPaw Framework 1.0+
- Git (用于版本控制)
- 读写权限：`memory/` 目录

---

## 获取帮助

- 📖 文档：https://miaouai.github.io/memory-skill-framework/
- 💬 Issues: https://github.com/miaouai/memory-skill-framework/issues
- 📧 作者：miaouai
