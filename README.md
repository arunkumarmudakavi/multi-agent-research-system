# 🚀 MARS - Multi-Agent Research System

MARS (Multi-Agent Research System) is a backend application that automates the research process using multiple AI agents. It takes a research query, searches the web for relevant information, summarizes findings, verifies them against trusted sources, and generates a structured research report.

The project is built with a modular architecture so that each agent has a single responsibility, making the system easy to extend and maintain.

---

## ✨ Features

- AI-powered research planning
- Real-time web search using Tavily
- Research summarization using local LLMs
- Fact-checking against collected sources
- Automatic report generation
- REST API built with FastAPI
- Modular multi-agent workflow
- Local LLM support using Ollama

---

## 🏗️ Architecture

```
                    User Query
                         │
                         ▼
                  Research Workflow
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
 Planner Agent     Search Agent      Research Agent
      │                  │                  │
      └──────────────► Sources ◄────────────┘
                         │
                         ▼
                 FactCheck Agent
                         │
                         ▼
                  Report Agent
                         │
                         ▼
                 Final Research Report
```

---

## 🤖 Agents

### Planner Agent

- Understands the user's query
- Breaks the topic into major research areas
- Creates research tasks

---

### Search Agent

- Searches the web using Tavily Search API
- Collects relevant sources for every task

---

### Research Agent

- Reads multiple search results
- Produces concise research summaries
- Removes duplicate information

---

### FactCheck Agent

- Verifies summaries using collected sources
- Removes unsupported information
- Generates confidence scores

---

### Report Agent

- Combines verified findings
- Produces a structured report

---

## 🛠 Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

### AI

- Ollama
- Qwen 3 (1.7B)

### Search

- Tavily Search API

### Database

- PostgreSQL

---

## 📂 Project Structure

```text
backend/
│
├── agents/
│   ├── planner_agent.py
│   ├── search_agent.py
│   ├── research_agent.py
│   ├── factcheck_agent.py
│   ├── report_agent.py
│   └── state.py
│
├── api/
│   ├── get_research.py
│   └── research.py
│
├── services/
│   ├── get_research_service.py
│   └── research_service.py
│
├── workflow/
│   └── research_workflow.py
│
├── llm/
│   └── ollama_client.py
│
├── search/
│
├── prompts/
│   ├── factcheck_prompt.py
│   ├── planner_prompt.py
│   └── research_prompt.py
│
├── models/
│   └── research_job.py
│
├── schemas/
│   └── research.py
│
├── config/
│
└── db/
    └── database.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/arunkumarmudakavi/multi-agent-research-system.git

cd multi-agent-research-system
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Install Ollama

Download Ollama

https://ollama.com/

Pull the model and start

```bash
ollama pull qwen3:1.7b
```

---

### Configure Environment

Create a `.env` file.

```env
DATABASE_URL = your_db

TAVILY_API_KEY = your_api_key
```

---

### Run Application

```bash
uvicorn backend.main:app --reload
```

---

## 🔄 Workflow

```
User Query
      │
      ▼
Planner
      │
      ▼
Search
      │
      ▼
Research
      │
      ▼
FactCheck
      │
      ▼
Report
      │
      ▼
Final Report
```

---

## 📊 Current Version

### ✅ Version 1.0

Implemented

- Planner Agent
- Search Agent
- Research Agent
- FactCheck Agent
- Report Agent
- Workflow Orchestration
- FastAPI
- SQLAlchemy
- Tavily Integration
- Ollama Integration
- Markdown Report Generation

---

## 👨‍💻 Author

**Arunkumar Mudakavi**

GitHub: [https://github.com/<your-username>](https://github.com/arunkumarmudakavi)
