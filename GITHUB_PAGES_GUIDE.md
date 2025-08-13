# 🚀 GitHub Pages 部署指南

## 快速部署到GitHub Pages

### 1. 创建GitHub仓库

1. 登录GitHub
2. 创建新仓库，命名为 `Papers` 或 `Papers-Reading`
3. 保持仓库为公开（Public）状态

### 2. 上传文件

将以下文件上传到仓库根目录：

```
Papers/
├── index.html          # 主要网页文件
├── _config.yml         # Jekyll配置文件
├── GITHUB_PAGES_GUIDE.md
└── README.md
```

### 3. 启用GitHub Pages

1. 进入仓库的 **Settings** 页面
2. 滚动到 **Pages** 部分
3. 在 **Source** 中选择 **Deploy from a branch**
4. 选择 **main** 分支和 **/ (root)** 目录
5. 点击 **Save**

### 4. 访问你的网页

等待几分钟后，你的网页将在以下地址可用：
```
https://yourusername.github.io/Papers
```

## 📁 文件夹结构要求

为了正确显示PDF文件，你需要保持以下结构：

```
Papers/
├── index.html
├── AutoML/
│   ├── paper1.pdf
│   └── paper2.pdf
├── benchmark/
├── LLM4CO/
├── SOH forecasting/
├── Surveys/
├── Security/
└── embodied/
```

## ⚠️ 重要注意事项

### GitHub Pages限制
- **文件大小限制**：单个文件不能超过100MB
- **仓库大小限制**：建议总大小不超过1GB
- **带宽限制**：每月100GB带宽

### PDF文件处理
由于GitHub Pages的限制，PDF文件需要通过Git LFS或CDN托管：

#### 方法1：使用Git LFS（推荐）
```bash
# 安装Git LFS
git lfs install

# 追踪PDF文件
git lfs track "*.pdf"

# 添加并提交
git add .
git commit -m "Add PDF files with LFS"
git push origin main
```

#### 方法2：使用CDN托管
将PDF文件上传到云存储（如Google Drive、OneDrive），然后更新文件链接。

### 文件链接更新
如果使用CDN，需要修改 `index.html` 中的文件加载逻辑：

```javascript
// 替换原有的文件加载逻辑
const categories = {
    'AutoML': {
        icon: 'fas fa-robot',
        description: '自动化机器学习相关文献',
        baseUrl: 'https://your-cdn.com/papers/AutoML/'
    },
    // ... 其他分类
};
```

## 🎨 自定义配置

### 修改网站标题
编辑 `index.html` 中的：
```html
<title>📚 文献阅读室</title>
```

### 添加新分类
在 `index.html` 的 `categories` 对象中添加：

```javascript
const categories = {
    '新分类名': {
        icon: 'fas fa-icon-name',
        description: '分类描述'
    }
};
```

### 修改主题颜色
编辑CSS中的渐变背景：
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## 🔧 本地测试

在部署前，可以在本地测试：

```bash
# 使用Python HTTP服务器
python -m http.server 8000

# 访问 http://localhost:8000
```

## 📊 性能优化

### 图片压缩
- 使用TinyPNG压缩图标
- 优化Font Awesome加载

### 缓存设置
- 利用GitHub Pages的CDN缓存
- 考虑使用Service Worker

## 🐛 故障排除

### PDF无法加载
1. 检查文件路径是否正确
2. 确认PDF文件已上传到对应目录
3. 检查浏览器控制台错误

### 页面样式异常
1. 清除浏览器缓存
2. 检查网络连接
3. 确认所有资源文件已正确上传

### 移动端适配问题
1. 使用Chrome DevTools测试响应式设计
2. 调整CSS媒体查询

## 📞 支持

如有问题，请：
1. 检查GitHub Pages状态页面
2. 查看仓库的Actions日志
3. 在Issues中提交问题报告