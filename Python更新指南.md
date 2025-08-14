# 🐍 Python版论文网站更新指南

## 🚀 快速开始

### 方法1：双击运行（推荐）
1. 将新的PDF文件放入对应目录
2. 双击 `update.bat` 即可
3. 按提示操作完成更新

### 方法2：命令行运行
```bash
# 在Papers文件夹中打开命令行
python update_papers.py

# 跳过GitHub同步
python update_papers.py --no-git
```

## 📋 文件说明

| 文件 | 功能 | 使用方法 |
|------|------|----------|
| `update_papers.py` | 主更新脚本 | 核心功能 |
| `run_update.py` | 简化运行器 | 检查环境并运行 |
| `update.bat` | 双击运行 | Windows双击 |

## ✨ 功能特点

### 🔄 自动化流程
1. **智能重命名**：自动将PDF文件名转换为"This Kind Of Style"格式
2. **网站索引**：自动更新index.html中的文件列表
3. **GitHub同步**：自动提交并推送到GitHub仓库
4. **进度显示**：实时显示更新进度和统计信息

### 📊 支持的文件名格式
```
原始文件名 → 转换结果
2023_automl_survey.pdf → Automl Survey.pdf
AI-Security-Fundamentals.pdf → Ai Security Fundamentals.pdf
deep_learning_methods.pdf → Deep Learning Methods.pdf
```

## 🔧 系统要求

### 必需软件
- **Python 3.6+**（推荐Python 3.8+）
- **Git**（已安装并配置）

### 检查安装
```bash
# 检查Python
python --version

# 检查Git
git --version
```

## 🎯 使用方法

### 日常更新步骤
1. **添加论文**：将PDF文件放入对应分类目录
2. **运行更新**：双击 `update.bat`
3. **等待完成**：2-5分钟后网站自动更新

### 批量更新
可以一次性放入多个PDF文件，脚本会自动处理所有文件。

### 验证更新
1. 查看终端输出确认更新成功
2. 检查GitHub仓库是否有新提交
3. 访问网站确认新论文已显示

## 🛠️ 故障排除

### 常见问题

#### 1. Python未找到
```bash
# 解决方法1：使用完整路径
C:\Python39\python.exe update_papers.py

# 解决方法2：添加到系统PATH
# 在系统环境变量中添加Python路径
```

#### 2. Git配置问题
```bash
# 配置Git用户信息
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"
```

#### 3. 权限问题
- 以管理员身份运行命令行
- 检查文件夹写入权限

#### 4. 编码问题
脚本已处理UTF-8编码，支持中英文文件名。

## 📊 更新统计示例

运行后显示：
```
🚀 Starting paper website update...
==================================================

📁 Step 1: Renaming PDF files...
  Processing: AutoML
  Renamed: 2023_automl_survey.pdf -> Automl Survey.pdf
  ✅ Renamed 1 files

📝 Step 2: Updating website index...
  ✅ index.html updated successfully

📊 Statistics:
------------------------------
  AutoML: 25 papers
  AI4Science: 3 papers
  LLM4CO: 3 papers
  Security: 4 papers
  Surveys: 11 papers
  benchmark: 3 papers
  embodied: 0 papers
  Total: 49 papers
------------------------------

🔄 Step 3: Syncing to GitHub...
  ✅ Successfully pushed to GitHub

🎉 Update completed!
Website will update in 2-5 minutes
URL: https://fendss.github.io/Papers-Reading
```

## 🚀 高级用法

### 自定义运行
```python
# 从其他目录运行
python C:\Users\Administrator\Desktop\Papers\update_papers.py

# 跳过GitHub同步
python update_papers.py --no-git
```

### 集成到其他工具
可以将此脚本集成到文件管理器的右键菜单，实现一键更新。

## 📞 技术支持

如有问题：
1. 检查Python和Git是否正确安装
2. 确认网络连接正常
3. 查看错误信息并搜索解决方案
4. 重新运行脚本

## 🎯 下一步

现在您只需要：
1. 确保已安装Python 3.6+
2. 将新PDF放入对应目录
3. 双击 `update.bat` 即可完成更新！