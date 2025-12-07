# 🌦️ Weather AI Agent

A simple and powerful AI-driven weather assistant built using **Google Generative AI (Gemini API)**.  
This project takes a city name as input and returns a generated, human-like weather report using AI.

---

## 🚀 Features

- 🌍 Accepts **any city** as user input  
- 🤖 Generates an **AI-powered weather report**  
- 🛠 Uses **Google Generative AI (gemini-1.5-flash)**  
- 🧩 Clean, modular Python code  
- 🔐 Uses `.env` file to securely load API keys  

---

## 📁 Project Structure

weather-agent/
│── weather_agent.py
│── .env
│── requirements.txt
│── README.md

---

## 🔧 Installation & Setup

### 1️⃣ Clone this repository

```bash
git clone <your-repo-url>
cd weather-agent
python -m venv venv
source venv/Scripts/activate   # Windows
pip install -r requirements.txt

Create a .env file in the project root:
OPENAI_API_KEY=your_api_key_here

run python weather_agent.py
