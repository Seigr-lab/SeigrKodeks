# SeigrKodeks - The Seigr Markdown Book Framework

## 🛠️ Overview
SeigrKodeks is a **fully standalone desktop application** for **creating structured books** using **Markdown**. It provides an efficient, flexible, and portable way to write, manage, and export documentation or books without relying on a web browser or external servers.

The tool allows users to:
- **Create books with multiple chapters**.
- **Write in Markdown or MediaWiki format**, with automatic conversion to Markdown.
- **Embed images, videos, and audio** within the Markdown files.
- **Export books as static HTML sites**, ready for hosting or local reading.

SeigrKodeks is:
- **Standalone**: Runs as a desktop application with **no web dependencies**.
- **Portable**: Works on **Linux, WSL, and Windows**.
- **Future-Proof**: Supports **extending to other formats** in the future.
- **Minimalist**: Avoids unnecessary dependencies and bloated frameworks.

---

## 🎯 Motivation
### **Why SeigrKodeks Instead of Existing Tools?**
Most book/documentation tools either:
1. **Are web-based** (MkDocs, GitBook, Docusaurus) and depend on browsers.
2. **Have limited support for media** in structured Markdown books.
3. **Force users to work in a single format** instead of allowing MediaWiki and Markdown interoperability.

SeigrKodeks addresses these problems by providing:

### 🔹 **1. A Full Book Creation Framework**
- Users can **define a book title**, add **chapters**, and **organize content**.
- Every **chapter is a separate `.md` file**, linked into a structured book.
- Books can be saved, edited, and reloaded for long-term project management.

### 🔹 **2. A Markdown-Centric, Desktop-First Approach**
- Unlike online tools, **everything runs locally**.
- Books and chapters are **saved as Markdown** (portable & future-proof).
- Supports **editing, media embedding, and file-based organization**.

### 🔹 **3. Automatic Format Detection & Conversion**
- Users can enter **Markdown or MediaWiki**, and the tool **automatically converts** to Markdown.
- Legacy documentation in MediaWiki format is seamlessly transitioned to Markdown.

### 🔹 **4. Export to Static HTML for Easy Hosting**
- Users can **generate a static website** from the book.
- Each **chapter becomes a linked HTML page**, forming an interactive book site.
- **Supports images, audio, and video embedding**.

---

## 🔄 How It Works
### **1️⃣ Create & Manage Books**
- Users **name their book** and define where to save it.
- Chapters can be **created, edited, and linked together**.
- Markdown and MediaWiki **can be used interchangeably**, ensuring easy migration.

### **2️⃣ Embed Media in Markdown**
- Users can insert:
  - **Images**: `![alt text](image.jpg)`
  - **Videos**: `<video src="video.mp4" controls>`
  - **Audio**: `<audio src="audio.mp3" controls>`
- Media files are stored in the **`assets/` directory** for organization.

### **3️⃣ Export to Static HTML**
- Books can be **converted to HTML** with:
  - A **Table of Contents**.
  - **Interlinked chapters**.
  - **Embedded media support**.
- The **output can be uploaded to any web server** or viewed locally.

---

## 📦 Features
✅ **Standalone Desktop App** – No browser, no web dependencies.
✅ **Multi-Format Input** – Write in **Markdown or MediaWiki**.
✅ **Automatic Format Detection** – Converts **MediaWiki to Markdown** seamlessly.
✅ **Full Book Organization** – Manage chapters, edit them, and structure books.
✅ **Media Embedding** – Supports **images, video, and audio in Markdown**.
✅ **Export as Static Website** – Generate a **lightweight, hostable book site**.
✅ **Minimal & Portable** – Works on **Linux, WSL, and Windows**.

---

## 📂 Project Structure
```
SeigrKodeks/
│── seigr_kodeks/
│   ├── parsers/            # Format detection and conversion
│   │   ├── format_detector.py   # Detects whether text is Markdown or MediaWiki
│   │   ├── mediawiki_to_md.py   # Converts MediaWiki syntax to Markdown
│   ├── markdown_parser.py   # Processes Markdown files
│   ├── desktop_gui.py       # The Tkinter-based desktop application
│── books/                   # User-created books (each book is a directory)
│── assets/                  # Images, videos, audio for the books
│── output/                  # Exported HTML versions of books
│── requirements.txt         # Dependencies (minimal)
│── .gitignore               # Git ignore file
│── README.md                # Documentation
```

---

## 🔥 Next Steps
- ✅ **Implement Format Detection & Conversion** (Done!)
- ✅ **Develop the Desktop UI** (Done!)
- ⏳ **Expand UI with Book & Chapter Management**
- ⏳ **Add Media Upload & Embedding Features**
- ⏳ **Implement Static HTML Export for Books**

SeigrKodeks is designed to **simplify book creation** while remaining flexible and **future-proof**. 🚀