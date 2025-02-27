# **SeigrKodeks - The Seigr Markdown Book Framework**

## 🛠️ Overview

**SeigrKodeks** is a **desktop application** designed for **creating structured books** in **Markdown**, featuring media support and **exporting capabilities to static HTML** for easy sharing.

With SeigrKodeks, you can:
- 📖 **Create books with multiple chapters** in a structured format.
- ✍ **Write using Markdown** (supports MediaWiki conversion).
- 🎨 **Embed images, videos, and audio** seamlessly into your books.
- 🌍 **Export books as static HTML sites**, making them ready for hosting or local reading.
- 🖥️ **Run entirely offline** without web dependencies.

---

## 🎯 Why SeigrKodeks?

Many existing tools either:
- **Are web-based**, requiring an internet connection (e.g., MkDocs, GitBook).
- **Lack proper media integration** for books using Markdown.
- **Do not support both Markdown and MediaWiki**, limiting format choices.

SeigrKodeks addresses these limitations with:
1. **A standalone, offline-first approach** – No browser or server required.
2. **Flexible content management** – Supports **Markdown and MediaWiki**.
3. **Comprehensive media handling** – Images, videos, and audio **integrated into Markdown**.
4. **One-click export to static HTML** – No extra tools needed to publish books.

---

## 🔄 How It Works

### **📘 1. Create & Manage Books**
- Define a **book title** and **save it anywhere** on your system.
- Chapters are **separate Markdown files**, keeping everything modular.
- Load, edit, and organize chapters **easily**.

### **🖼 2. Embed Media**
SeigrKodeks supports:
- **Images**: `![Alt Text](media/image.jpg)`
- **Videos**: `<video src="media/video.mp4" controls>`
- **Audio**: `<audio src="media/audio.mp3" controls>`
- Media files are **organized automatically** inside the `media/` directory.

### **🌍 3. Export to Static HTML**
- Books can be **converted to fully linked HTML pages**.
- The output includes:
  - 📜 **A Table of Contents**.
  - 🔗 **Interlinked chapters**.
  - 🎥 **Embedded media support**.
- 📂 **Ready for hosting or local reading**.

---

## 📦 Project Structure

```
SeigrKodeks/
│── seigr_kodeks/
│   ├── parsers/              # Format detection & conversion
│   │   ├── format_detector.py  # Detects if content is Markdown or MediaWiki
│   │   ├── mediawiki_to_md.py  # Converts MediaWiki to Markdown
│   ├── storage_manager.py     # Manages storage preferences
│   ├── file_manager.py        # Organizes book files & media
│   ├── media_manager.py       # Handles inserting & deleting media files
│   ├── markdown_parser.py     # Processes Markdown chapters
│   ├── html_renderer.py       # Converts Markdown to styled HTML
│   ├── exporter.py            # Exports books to HTML
│   ├── desktop_gui.py         # The Tkinter-based GUI
│── books/                     # User-created books (each book is a directory)
│── output/                    # Exported HTML books
│── assets/                    # Shared resources
│── requirements.txt           # Dependencies (minimal)
│── README.md                  # Documentation
```

---

## 🛠 Features

✅ **Standalone Desktop App** – No browser, no web dependencies.  
✅ **Markdown & MediaWiki Support** – Write & convert between formats.  
✅ **Full Book Organization** – Manage chapters, structure books.  
✅ **Rich Media Embedding** – Images, videos, and audio in Markdown.  
✅ **Export to HTML** – Generate **a complete website** from your book.  
✅ **Minimal & Portable** – Works on **Linux, WSL, and Windows**.  

---

## 🔥 Next Steps

✅ **Format Detection & Conversion**  
✅ **Fully Functional Desktop GUI**  
✅ **Comprehensive Book & Chapter Management**  
✅ **Media Embedding & Handling**  
✅ **Static HTML Export for Books**  

📌 **Upcoming Features**:
- 📜 **PDF Export Support**
- 🌍 **GitHub Integration for Book Hosting**
- 📝 **WYSIWYG Markdown Editing Mode**

---

SeigrKodeks is built to **simplify book creation** while staying **lightweight, portable, and powerful**. 🚀
