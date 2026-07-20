# 🤖 Single-Agent AI Research Assistant

> A production-ready AI-powered research assistant built with **FastAPI**, **LangGraph**, **Groq LLM**, **DuckDuckGo**, and **Wikipedia**, capable of generating professional research reports with Markdown and PDF exports.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-orange)
![Groq](https://img.shields.io/badge/Groq-LLM-red)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_Demo-ff4b4b)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)
![License](https://img.shields.io/badge/License-MIT-success)

---

## 🌐 Live Demo

### 🖥️ Web Application

**Live App**

https://single-agent-ai-research-assistant-2ndvplhb4q76b9drunp5s6.streamlit.app

---

### 📄 API Documentation

**Swagger UI**

https://single-agent-ai-research-assistant.onrender.com/docs

---

## 📌 Overview

The Single-Agent AI Research Assistant is an end-to-end AI application that performs automated web research and generates structured research reports.

It combines modern Agentic AI workflows with a production-ready backend and interactive frontend. Users can submit research topics, automatically gather information from trusted online sources, generate comprehensive reports using an LLM, and export the results as Markdown or PDF documents.

The application is designed following modern AI engineering practices including modular architecture, workflow orchestration, Docker support, REST APIs, and cloud deployment.

---

# ✨ Features

- 🔎 **AI-powered Research Generation**
  - Generates structured research reports using Groq LLM.

- 🌍 **Multi-source Information Retrieval**
  - Searches DuckDuckGo.
  - Retrieves trusted summaries from Wikipedia.

- 🧠 **LangGraph Workflow**
  - Planner Node
  - Search Node
  - Report Generator
  - Evaluator
  - Report Improver
  - Memory Lookup

- 📄 **Professional Reports**
  - Executive Summary
  - Key Findings
  - Detailed Analysis
  - Conclusion

- 📥 **Export Options**
  - Markdown (.md)
  - PDF (.pdf)

- 📚 **Research History**
  - Stores previous research in SQLite.
  - View and download previous reports.

- 🌐 **REST API**
  - Fully documented using Swagger UI.

- 🖥️ **Interactive Frontend**
  - Built with Streamlit.
  - One-click report generation.

- 🐳 **Production Ready**
  - Docker support
  - Render deployment
  - Streamlit Cloud deployment
  - GitHub Actions ready

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.13 |
| Backend | FastAPI |
| Frontend | Streamlit |
| AI Workflow | LangGraph |
| LLM | Groq (Llama 3.3 70B Versatile) |
| Search | DuckDuckGo |
| Knowledge Source | Wikipedia |
| Database | SQLite + SQLAlchemy |
| Report Export | Markdown, ReportLab PDF |
| API Documentation | Swagger UI |
| Deployment | Render |
| Frontend Hosting | Streamlit Community Cloud |
| Containerization | Docker |
| Version Control | Git & GitHub |

# 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │       Streamlit UI      │
                    │   (Frontend - Cloud)    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      FastAPI API        │
                    │    (Render Backend)     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     LangGraph Agent     │
                    └────────────┬────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          ▼                      ▼                      ▼
   Memory Lookup          DuckDuckGo Search       Wikipedia
          │                      │                      │
          └──────────────┬───────┴──────────────┬───────┘
                         ▼                      ▼
                  Report Generation       Report Evaluation
                         │
                         ▼
                  Report Improvement
                         │
                         ▼
                 SQLite Research History
                         │
                         ▼
             Markdown & PDF Export
```

# 📷 Screenshots

## Home

![Home](docs/images/home.png)

---

## Generated Report

![Report](docs/images/report.png)

---

## Research History

![History](docs/images/history.png)

---

## Swagger API

![Swagger](docs/images/swagger.png)

---

## Downloads

![Downloads](docs/images/downloads.png)

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/single-agent-ai-research-assistant.git
cd single-agent-ai-research-assistant
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -e .
```

## 4. Configure environment variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key
LLM_PROVIDER=groq
LLM_MODEL=llama-3.3-70b-versatile
```

## 5. Run FastAPI

```bash
uvicorn app.main:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

## 6. Run Streamlit

```bash
streamlit run frontend/app.py
```