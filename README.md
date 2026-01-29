# 📰 RSS Web Publisher

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-green?style=for-the-badge)
![RSS](https://img.shields.io/badge/RSS-Feed-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

*Desktop application for creating and managing RSS feed-based web content*

[📥 Download](#-download) • [✨ Features](#-features) • [🚀 Usage](#-usage)

</div>

---

## 📥 Download

### Windows Executable
Download the standalone Windows application - no installation required!

**Latest Release**: [Download RSS-WEB-PUBLISHER.exe](https://github.com/ernakkc/RSS-web-publisher/releases/latest)

<div align="center">

[![Download](https://img.shields.io/github/v/release/ernakkc/RSS-web-publisher?style=for-the-badge&label=Download&color=success)](https://github.com/ernakkc/RSS-web-publisher/releases)
[![Downloads](https://img.shields.io/github/downloads/ernakkc/RSS-web-publisher/total?style=for-the-badge&color=blue)](https://github.com/ernakkc/RSS-web-publisher/releases)

</div>

### System Requirements
- **OS**: Windows 7/8/10/11 (64-bit)
- **RAM**: 2GB minimum, 4GB recommended
- **Disk Space**: 50MB free space
- **Internet**: Active connection for RSS feeds

## 📖 Overview

RSS Web Publisher is a powerful desktop application that automates the process of fetching content from RSS feeds and publishing it to websites. Perfect for content creators, bloggers, and news aggregators who want to automate their content workflow.

## ✨ Features

- 📡 **RSS Feed Integration**: Subscribe to multiple RSS feeds
- 🤖 **Automated Publishing**: Schedule automatic content updates
- 🎨 **Content Formatting**: Customize article layouts and styling
- 📝 **Content Editor**: Edit and preview before publishing
- 🌐 **Multi-Platform Support**: Publish to WordPress, Blogger, and more
- 📊 **Feed Management**: Organize and categorize feeds
- ⏰ **Scheduling**: Set automatic publish times
- 🖼️ **Image Handling**: Automatic image download and hosting
- 📈 **Statistics**: Track published articles and feed activity
- 💾 **Draft System**: Save drafts before publishing

## 🚀 Quick Start

### For Windows Users (Easiest)

1. **Download the .exe file** from [Releases](https://github.com/ernakkc/RSS-web-publisher/releases)
2. **Run RSS-WEB-PUBLISHER.exe**
3. **No installation needed!**

### For Python Users

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ernakkc/RSS-web-publisher.git
   cd RSS-web-publisher
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## 💻 Usage

### Adding RSS Feeds

1. Click **"Add Feed"** button
2. Enter RSS feed URL
3. Set category and update frequency
4. Click **"Subscribe"**

### Publishing Content

1. **Select Feed** from the list
2. **Browse Articles** from the feed
3. **Edit Content** if needed
4. **Choose Platform** (WordPress, Blogger, etc.)
5. **Click Publish** or schedule for later

### Automation Setup

```python
# Schedule automatic publishing
schedule = {
    "frequency": "daily",
    "time": "09:00",
    "feeds": ["feed1", "feed2"],
    "auto_publish": True
}
```

## 📁 Project Structure

```
RSS-web-publisher/
├── main.py                 # Application entry point
├── RSS-WEB-PUBLISHER.spec  # PyInstaller configuration
├── requirements.txt        # Python dependencies
├── icon.ico               # Application icon
├── dist/                  # Compiled executables
│   └── RSS-WEB-PUBLISHER.exe
├── build/                 # Build artifacts
├── utils/                 # Utility modules
│   ├── rss_parser.py     # RSS feed parser
│   ├── publisher.py      # Publishing logic
│   └── scheduler.py      # Task scheduler
└── README.md             # This file
```

## ⚙️ Configuration

### RSS Feed Settings

```python
feed_config = {
    "url": "https://example.com/feed.xml",
    "category": "Technology",
    "update_interval": 3600,  # seconds
    "auto_publish": False,
    "filters": {
        "keywords": ["python", "programming"],
        "exclude": ["spam"]
    }
}
```

### Publishing Platforms

#### WordPress
```python
wordpress_config = {
    "site_url": "https://yoursite.com",
    "username": "your_username",
    "password": "your_app_password",
    "default_category": "News",
    "default_status": "publish"  # or "draft"
}
```

#### Blogger
```python
blogger_config = {
    "blog_id": "your_blog_id",
    "api_key": "your_api_key",
    "default_labels": ["RSS", "Auto"]
}
```

## 🎨 Features in Detail

### Content Customization

- **Template System**: Create custom article templates
- **SEO Optimization**: Automatic meta tags and descriptions
- **Image Processing**: Resize and optimize images
- **Link Management**: Update broken links
- **Copyright**: Add source attribution

### Feed Management

- **Feed Categories**: Organize feeds by topic
- **Priority Levels**: High-priority feeds update more frequently
- **Feed Health**: Monitor feed availability
- **Duplicate Detection**: Avoid republishing same content

### Publishing Options

- **Immediate**: Publish right away
- **Scheduled**: Set specific publish time
- **Draft**: Save as draft for review
- **Bulk**: Publish multiple articles at once

## 🔧 Advanced Features

### Custom Filters

```python
# Filter articles by keywords
filter_settings = {
    "include_keywords": ["technology", "programming"],
    "exclude_keywords": ["advertisement", "sponsored"],
    "min_word_count": 300,
    "require_image": True
}
```

### Automatic Image Handling

```python
image_settings = {
    "download_images": True,
    "max_size": (1200, 800),
    "format": "webp",
    "quality": 85,
    "cdn_upload": True
}
```

## 📊 Statistics & Analytics

View detailed statistics:
- Total articles published
- Articles per feed
- Publishing success rate
- Most active feeds
- Traffic sources

## 🐛 Troubleshooting

### Application Won't Start
```
1. Check Windows Defender/Antivirus
2. Run as Administrator
3. Check Windows Event Viewer for errors
```

### Feed Not Updating
```
1. Verify feed URL is accessible
2. Check internet connection
3. Validate RSS feed format
4. Review feed update interval
```

### Publishing Errors
```
1. Verify API credentials
2. Check platform API limits
3. Review error logs
4. Test connection manually
```

## 🔨 Building from Source

### Create Windows Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller RSS-WEB-PUBLISHER.spec

# Executable will be in dist/ folder
```

### Custom Build Options

Edit `RSS-WEB-PUBLISHER.spec`:
```python
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
)
```

## 🤝 Contributing

Contributions welcome! Ideas for improvements:
- Support for more platforms (Medium, Ghost)
- Content translation features
- AI-powered content summarization
- Advanced scheduling options
- Mobile companion app

## 📝 Dependencies

```txt
PyQt5>=5.15.0
feedparser>=6.0.0
requests>=2.26.0
beautifulsoup4>=4.10.0
python-wordpress-xmlrpc>=2.3
schedule>=1.1.0
```

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Eren Akkoç**
- GitHub: [@ernakkc](https://github.com/ernakkc)
- Email: ern.akkc@gmail.com

## 🙏 Acknowledgments

- PyQt5 for the GUI framework
- feedparser library
- WordPress and Blogger API teams

---

<div align="center">

**📰 Automate Your Content Publishing! 🚀**

*Star ⭐ this repo if you find it useful!*

[![GitHub stars](https://img.shields.io/github/stars/ernakkc/RSS-web-publisher?style=social)](https://github.com/ernakkc/RSS-web-publisher)
[![GitHub forks](https://img.shields.io/github/forks/ernakkc/RSS-web-publisher?style=social)](https://github.com/ernakkc/RSS-web-publisher/fork)

</div>
