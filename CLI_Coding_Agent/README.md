# 🧠 CLI Coding Agent — Tool-Using AI Assistant (Python + OpenAI)

This project is an **Agentic AI system** built in Python using the **OpenAI API**, **Pydantic**, and **custom tool calling**.
It follows a multi-step reasoning workflow inspired by OpenAI Swarm and LangGraph:

**START → PLAN → TOOL → OBSERVE → OUTPUT**

The agent receives a user question, plans its reasoning, decides whether to call a tool, executes it, observes the result, and finally returns a well-structured output.

---

## 🚀 Features

* ✔️ Chain-of-Thought style planning (without revealing internal reasoning)
* ✔️ Tool calling support (`run_command(cmd : str)`)
* ✔️ JSON-structured responses validated using **Pydantic models**
* ✔️ Automatic tool execution + passing OBSERVE steps
* ✔️ Full conversational memory with role-based messages
* ✔️ Clean terminal interface for interactive querying

---

## 🧩 Architecture

### **Agent Workflow**

```
START → PLAN (multiple) → TOOL → OBSERVE → OUTPUT
```

### **Tools**

The agent currently has one tool:

* `run_command(cmd : str)`
  

You can easily add new tools by extending the `available_tools` dictionary.

---

## 📁 Project Structure

```
weather-agent/
│
├── agent.py          # Main script (your tool-using agent)
├── README.md         # Documentation
├── .env              # OPENAI_API_KEY stored here
└── requirements.txt  # Dependencies
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone "URL"
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Agent

```bash
python agent.py
```

You will see:

```
Query 👉🏻
```

Ask anything like:

```
create a todo app using html css and js.
```

The agent will output START, PLAN, TOOL, OBSERVE, and OUTPUT steps.

---

## 📦 Dependencies

```
openai
python-dotenv
requests
pydantic
```

---




