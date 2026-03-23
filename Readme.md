# 🧠 Multi-Agent Insurance System

A smart AI-powered insurance assistant built using **Streamlit + Groq API + Multi-Agent Architecture**.

This project uses:
- 🔍 Research Agent → Gathers insurance information  
- 📝 Writer Agent → Generates structured reports  
- 💬 Chatbot UI → Interactive user experience  
- 🕘 History → Stores past queries  

---

## 🚀 Features

- Multi-Agent AI system (Research + Writer)
- Clean Streamlit Web UI
- Chatbot-style interaction
- Suggested queries for users
- History tracking (JSON-based)
- Groq LLM integration

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API (LLM)
- LangChain / CrewAI (optional)
- JSON (for storage)

---

## 📁 Project Structure


multiagent-insurance-creator/
│
├── app.py
├── pages/
│ ├── 1_Analysis.py
│ ├── 2_History.py
│
├── agents/
│ ├── researcher.py
│ ├── writer.py
│
├── utils/
│ ├── groq_api.py
│ ├── sidebar.py
│
├── data/
│ ├── history.json
│
├── .env
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions


2️⃣ Create Virtual Environment
python -m venv venv

Activate:

venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Groq API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here
🔑 How to Get Groq API Key

Go to: https://console.groq.com

Sign up / login

Go to API Keys section

Click Create API Key

Copy and paste into .env

5️⃣ Run the App
streamlit run app.py
💡 How It Works

User enters insurance query

Research Agent fetches insights

Writer Agent generates structured report

Output is displayed and saved in history
