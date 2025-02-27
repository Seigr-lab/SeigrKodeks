# **SeigrKodeks - Structured Documentation for the Binary World**  

## 🛠️ Overview  

**SeigrKodeks** is a **desktop application** developed within **Seigr-lab** for **creating structured books and technical documentation** in **Markdown**. Designed for **binary-driven ecosystems**, it provides **a fully offline, structured, and media-integrated framework** to write, manage, and export books.  

With **SeigrKodeks**, you can:  
- 📖 **Create books with structured chapters** stored as Markdown.  
- ✍ **Write in Markdown or MediaWiki**, with seamless format conversion.  
- 🎨 **Embed images, videos, and audio**, keeping structured media organization.  
- 🌍 **Export books as static HTML sites**, preserving **interlinked chapters**.  
- 🖥️ **Run entirely offline**, ensuring **full control over documentation**.  

### **SeigrKodeks is built for:**  
✅ **Technical documentation in binary-driven environments.**  
✅ **Structured book-writing without cloud dependencies.**  
✅ **Offline, standalone documentation for specialized projects.**  
✅ **Future-proof Markdown-based documentation.**  

---

## 🎯 **Why SeigrKodeks?**  

Most documentation tools:  
- **Are web-based**, requiring an internet connection (e.g., MkDocs, GitBook).  
- **Lack structured media embedding**, making multimedia-heavy books difficult.  
- **Restrict users to specific formats**, preventing seamless **Markdown ↔ MediaWiki interoperability**.  

SeigrKodeks **solves these issues** by providing:  
1️⃣ **A standalone, offline-first approach** – No browser, no web dependencies.  
2️⃣ **Flexible content management** – Supports **Markdown and MediaWiki**.  
3️⃣ **Comprehensive media handling** – Images, videos, and audio **integrated into Markdown**.  
4️⃣ **One-click export to structured static HTML** – Books remain readable **forever**, no compatibility issues.  

---

## 🔄 **How It Works**  

### **📘 1. Create & Manage Books**  
- Define a **book title** and **store it anywhere** on your system.  
- Chapters are **individual Markdown files**, keeping content structured and portable.  
- Easily **organize, rename, and edit** chapters.  

### **🖼 2. Embed & Manage Media**  
SeigrKodeks supports seamless **multimedia integration**:  
- **Images**: `![Alt Text](media/image.jpg)`  
- **Videos**: `<video src="media/video.mp4" controls>`  
- **Audio**: `<audio src="media/audio.mp3" controls>`  
- Media files are **automatically stored in structured directories** (`media/`).  

### **🌍 3. Export as Static HTML**  
- Generates **a fully interactive website** from your book.  
- The HTML output includes:  
  ✅ **A Table of Contents**.  
  ✅ **Interlinked chapters** with navigation.  
  ✅ **Embedded images, videos, and audio**.  
- 📂 **Perfect for hosting or local reading**.  

---

## 📦 **Project Structure**  

```
SeigrKodeks/
│── seigr_kodeks/                 # Core Framework
│   ├── parsers/                   # Format detection & conversion
│   │   ├── format_detector.py      # Detects if content is Markdown or MediaWiki
│   │   ├── mediawiki_to_md.py      # Converts MediaWiki to Markdown
│   ├── storage_manager.py          # Manages storage preferences & settings
│   ├── file_manager.py             # Handles book file organization
│   ├── media_manager.py            # Embeds and manages media
│   ├── markdown_parser.py          # Processes Markdown content
│   ├── html_renderer.py            # Converts Markdown to styled HTML
│   ├── exporter.py                 # Handles full book export to HTML
│   ├── desktop_gui.py              # The Tkinter-based GUI
│── books/                          # User-created books (each book is a directory)
│── output/                         # Exported HTML books
│── assets/                         # Shared resources (icons, UI elements)
│── requirements.txt                # Dependencies (minimal)
│── README.md                       # Documentation
```

---

## 🛠 **Features**  

✅ **Fully Standalone Desktop Application** – No browser, no cloud dependencies.  
✅ **Multi-Format Support** – Write in **Markdown or MediaWiki**, and export to HTML.  
✅ **Full Book & Chapter Organization** – Manage, reorder, and structure books easily.  
✅ **Rich Media Embedding** – **Images, video, and audio seamlessly integrated**.  
✅ **One-Click HTML Export** – Generate **a fully linked static book site**.  
✅ **Minimal & Portable** – Runs on **Linux, WSL, and Windows**.  

---

## 🔥 **Next Steps**  

✅ **Format Detection & Markdown Conversion**  
✅ **Fully Functional Desktop UI**  
✅ **Comprehensive Book & Chapter Management**  
✅ **Seamless Media Embedding & File Handling**  
✅ **Static HTML Export for Fully Linked Book Sites**  

📌 **Upcoming Features**:  
- 📜 **PDF Export Support**  
- 🌍 **GitHub Integration for Book Hosting**  
- 📝 **WYSIWYG Markdown Editing Mode**  

---

## 🚀 **SeigrKodeks & The Seigr Ecosystem**  

SeigrKodeks is **a Seigr-lab project**, developed to **provide structured documentation solutions in the binary world**.  

🔹 **It is NOT a part of Seigr OS but follows Seigr principles of structured, modular, and future-proof documentation.**  

🔹 **It is built for offline-first, long-term technical writing, ensuring interoperability between Markdown, MediaWiki, and HTML.**  

🔹 **While it aligns with the Seigr ecosystem, SeigrKodeks is an independent tool designed to function outside Seigr OS.**  

---

## **Final Notes**  

SeigrKodeks is built to **simplify book creation** while staying **lightweight, portable, and powerful**. It follows the **Seigr philosophy** of structured, secure, and future-proofed development.  
