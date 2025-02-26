# SeigrKodeks - The Seigr Markdown Book Framework

## 🛠️ Overview
SeigrKodeks is a lightweight, structured, and modular **Markdown-based book framework** designed for the **Seigr ecosystem**. Unlike existing documentation solutions, SeigrKodeks provides a **flexible and format-agnostic approach**, allowing content to be written in multiple formats (Markdown, MediaWiki) and stored **consistently in Markdown**. 

The goal is to streamline **technical documentation, structured knowledge storage, and dynamic book rendering** in a clean and maintainable format. SeigrKodeks is designed to be:

- **Modular**: Supports multiple input formats but standardizes output to Markdown.
- **Lightweight**: Minimal dependencies, avoiding unnecessary external libraries.
- **Extensible**: Future-proof architecture to support additional text formats.
- **Portable**: Works across different environments, including WSL, Linux, and Windows.
- **Seigr-First**: Follows Seigr’s structured development ethos.

---

## 🎯 Motivation
### **Why Create SeigrKodeks Instead of Using Existing Tools?**
Most documentation and book frameworks fall into two categories:
1. **Markdown-focused frameworks** (MkDocs, GitBook) that lack flexibility.
2. **General-purpose wiki/documentation systems** (MediaWiki, Docusaurus) that introduce complexity.

SeigrKodeks aims to **bridge the gap**, providing:

### 🔹 **1. Multi-Format Support & Standardization**
- Existing tools force users to commit to a **single format** (Markdown, AsciiDoc, or MediaWiki).
- SeigrKodeks allows users to **write in different formats** and **automatically convert them to Markdown**.
- This is essential for migrating from **MediaWiki** (legacy Seigr documentation) to a **modern, structured format**.

### 🔹 **2. Lightweight & Portable**
- No bloated dependencies.
- Designed to **run locally** without requiring a server.
- Can be packaged as a **static web app** for viewing Markdown books.

### 🔹 **3. Structured for Seigr’s Needs**
- Documentation must be **clear, versioned, and modular**.
- Unlike traditional Markdown systems, SeigrKodeks integrates **format detection, auto-conversion, and clean book rendering**.
- The framework adheres to Seigr’s **standardized development guidelines**.

### 🔹 **4. Future-Proof & Extensible**
- Designed with a **modular parser system**, allowing **additional text formats** to be added in the future.
- As Seigr grows, the documentation system should be **scalable** and **adaptable**.

---

## 🔄 How It Works
### **1️⃣ Format Detection**
- SeigrKodeks can **automatically detect** whether the input text is written in:
  - **Markdown** (`#`, `-`, `*`, `[link](url)`, `![img](url)`).
  - **MediaWiki** (`== Headings ==`, `'''Bold'''`, `[[Links]]`).
- This detection enables seamless conversion of **existing MediaWiki documentation** into Markdown.

### **2️⃣ Unified Markdown Storage**
- Regardless of input format, all content is stored as **Markdown** for **consistency and long-term maintainability**.

### **3️⃣ Browser-Based Markdown Rendering**
- Instead of pre-converting Markdown to HTML, SeigrKodeks **displays raw Markdown in an interactive browser UI**.
- Uses **JavaScript rendering** (`marked.js`) to provide a **live preview** without server processing.

---

## 📦 Features
✅ **Multi-Format Input** – Write in either **Markdown or MediaWiki**.
✅ **Automatic Format Detection** – The system detects the input format and processes it accordingly.
✅ **Live Markdown Rendering** – View formatted Markdown directly in the browser.
✅ **Minimal Dependencies** – Avoids unnecessary external libraries.
✅ **Modular & Future-Proof** – Easily expandable to support new formats.
✅ **Portable & Local-First** – Can run **without internet access**.

---

## 📂 Project Structure
```
SeigrKodeks/
│── seigr_kodeks/
│   ├── parsers/            # Format detection and conversion
│   │   ├── format_detector.py   # Detects whether text is Markdown or MediaWiki
│   │   ├── mediawiki_to_md.py   # Converts MediaWiki syntax to Markdown (soon)
│   ├── markdown_parser.py   # Processes Markdown files
│   ├── html_renderer.py     # Displays Markdown as HTML in the browser
│   ├── server.py            # (Future) Serve as a local static site generator
│── chapters/                # User Markdown content
│── assets/                  # Images, videos, audio
│── static/                  # CSS, JS for frontend
│── templates/               # HTML templates for rendering
│── main.py                  # CLI interface (future expansion)
│── requirements.txt         # Dependencies (minimal)
│── .gitignore               # Git ignore file
│── README.md                # Documentation
```

---

## 🔥 Next Steps
- ✅ **Implement Format Detection** (Done!)
- ⏳ **Develop MediaWiki to Markdown Converter** (Next Priority)
- ⏳ **Expand UI with a File Selector & Enhanced Styling**
- ⏳ **Add Future Format Support (e.g., reStructuredText, AsciiDoc)**

SeigrKodeks is designed to **simplify documentation workflows** while remaining flexible and future-proof. 🚀
