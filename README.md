# AI-Ethics-Chatbot

# 🤖 AI Ethics Chatbot

An AI-powered chatbot built with **Google Gemini** and **Streamlit** that analyzes ethical dimensions of AI-related questions.

---

## ✨ Features

- 💬 Chat interface powered by Streamlit
- 🧠 Structured ethical analysis for AI-related queries
- ⚠️ Risk identification and recommendations
- 🚦 Risk level rating (Low / Medium / High)
- 🙋 Natural responses for casual greetings

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|------------------------|
| Frontend  | Streamlit              |
| AI Model  | Google Gemini 3 Flash  |
| Backend   | Python                 |
| API Key   | python-dotenv          |

---

ai-ethics-chatbot/
├── chatbot.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .gitignore          # Files excluded from GitHub
└── README.md           # Project documentation

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-ethics-chatbot.git
cd ai-ethics-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
- Copy `.env.example` and rename it to `.env`
- Add your Gemini API key:

GEMINI_API_KEY=your_actual_key_here

### 4. Run the app
```bash
streamlit run app.py
```

---

## 🔑 Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click **"Get API Key"**
4. Copy and paste it into your `.env` file

---

## 💡 Example Queries

- *"Is it ethical to use AI in hiring decisions?"*
- *"What are the risks of facial recognition in public spaces?"*
- *"Should AI be used in medical diagnosis?"*

---

## ⚠️ Disclaimer

This chatbot provides educational perspectives on AI ethics. It is not a substitute for professional ethical or legal advice.

---

## 👩‍💻 Author

B S Lakshmi Prerana - 

## 📁 Project Structure
