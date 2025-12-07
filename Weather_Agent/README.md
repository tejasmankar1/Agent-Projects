🧠 Weather Agent — Tool-Using AI Assistant (Python + OpenAI)

This project is an Agentic AI system built in Python using the OpenAI API, Pydantic, and custom tool calling.
It follows a multi-step reasoning workflow inspired by OpenAI Swarm and LangGraph:

START → PLAN → TOOL → OBSERVE → OUTPUT

The agent receives a user question, plans its reasoning, decides whether to call a tool, executes it, observes the result, and finally returns a well-structured output.

🚀 Features

✔️ Chain-of-Thought style planning (without revealing internal reasoning)

✔️ Tool calling support (weather_agent(city))

✔️ JSON-structured responses validated using Pydantic models

✔️ Automatic tool execution + passing OBSERVE steps

✔️ Full conversational memory with role-based messages

✔️ Clean terminal interface for interactive querying

🧩 Architecture
Agent Workflow
START → PLAN (multiple) → TOOL → OBSERVE → OUTPUT
Tools

The agent currently has one tool:

weather_agent(city: str)
Fetches live weather information using wttr.in.

You can easily add new tools by extending the available_tools dictionary.

📁 Project Structure
weather-agent/
│
├── agent.py          # Main script (your tool-using agent)
├── README.md         # Documentation
├── .env              # OPENAI_API_KEY stored here
└── requirements.txt  # Dependencies

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/weather-agent.git
cd weather-agent
2. Create a virtual environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
3. Install dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:
OPENAI_API_KEY=your_api_key_here

▶️ Run the Agent
python agent.py

You will see:

Query 👉🏻

Ask anything like:

What is the weather in Mumbai?

The agent will output START, PLAN, TOOL, OBSERVE, and OUTPUT steps.

💡 Example Interaction
Query 👉🏻 What is the weather in Delhi?

🔥 START: User asked for the weather in Delhi
🧠 PLAN: Checking available tools for weather info
🧠 PLAN: We have 'weather_agent' available
🛠️ TOOL CALL → weather_agent(Delhi)
🛠️ TOOL RESULT → The Weather in Delhi is Sunny +28°C
👀 OBSERVE: Received tool output
🤖 OUTPUT: The current weather in Delhi is Sunny and 28°C.
🧰 How the Tool Works
weather_agent(city: str)

Uses requests to call https://wttr.in/<city>?format=%C+%t

Returns weather summary as plain text

Automatically integrated into the agent’s workflow

📦 Dependencies
openai
python-dotenv
requests
pydantic

📌 Future Improvements

Add more tools:
News lookup
Stock prices
Calculator
Web search
Add LangGraph-based version
Convert into a FastAPI backend
Add memory persistence

