# HiFiTi 自动签到脚本
# 最新内容访问:blog.smlin0513.asia
## 如果感觉可以点个star⭐！！！

这是一个用于 HiFiTi 音乐论坛的自动签到脚本。通过模拟浏览器请求实现自动签到功能。

## 功能特点

- 自动签到
- 详细的日志记录
- 跨平台支持（Windows/Mac/Linux）
- 支持定时任务

## 环境要求

- Python 3.6 或更高版本
- requests 库

## 安装步骤

1. 克隆或下载本项目到本地

2. 安装依赖：
   ```bash
   # Windows
   pip install requests

   # Mac/Linux
   pip3 install requests
   ```

## 使用方法

### 1. 获取 Cookie

1. 打开浏览器访问 https://www.hifiti.com 并登录
2. 打开开发者工具：
   - Windows: 按 F12 或 Ctrl+Shift+I
   - Mac: 按 Command+Option+I
3. 切换到 "Network" 标签
4. 刷新页面
5. 在请求列表中找到任意请求
6. 在请求头(Headers)中找到 "Cookie" 字段
7. 复制整个 cookie 字符串

### 2. 配置脚本

1. 打开 cookie.txt
2. 把cookie复制进去

### 3. 运行脚本

```bash
# Windows
python hifiti_sign.py

# Mac/Linux
python3 hifiti_sign.py
```

### 4. 设置自动运行（可选）

#### Windows 任务计划程序
1. 打开任务计划程序
2. 创建基本任务
3. 设置触发器（如每天特定时间）
4. 操作选择"启动程序"
5. 程序路径填写 Python 解释器路径
6. 参数填写脚本完整路径

#### Mac/Linux Crontab
```bash
# 编辑 crontab
crontab -e

# 添加定时任务（例如每天早上 8 点运行）
0 8 * * * /usr/bin/python3 /完整路径/hifiti_sign.py
```

## 日志说明

脚本运行日志保存在 `hifiti_sign.log` 文件中，包含：
- 时间戳
- 日志级别（INFO/ERROR）
- 详细消息

## 注意事项

1. Cookie 会定期过期，需要及时更新
2. 请勿分享你的 Cookie，它包含你的登录凭证
3. 建议定期检查日志文件，确保签到正常进行

## 常见问题

1. **Cookie 过期**
   - 重新获取 Cookie 并更新到脚本中

2. **运行报错**
   - 检查 Python 版本是否满足要求
   - 确认 requests 库已正确安装
   - 查看日志文件了解详细错误信息

## 更新日志

### v1.0.0 (2025-03-11)
- 初始版本发布
- 实现基本签到功能
- 添加日志记录

## 许可证

MIT License 