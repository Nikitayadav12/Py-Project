# 🤖 Rule-Based ChatBot

A simple **rule-based chatbot** built in Python.  
This chatbot responds to greetings, tells the time & date, cracks jokes, solves simple math problems, and remembers the chat history.  

---

## 🚀 Features
- 👋 **Personalized greetings** (asks for your name and remembers it).  
- ⏰ **Tells current time & date/day** using `datetime`.  
- ☀️ **Weather (simulated)** – friendly response even without real API.  
- ➕ **Basic math operations** (like addition).  
- 😂 **Random jokes & fun facts**.  
- 📝 **Chat history saved** and displayed when you exit.  
- 👌 **User-friendly responses** with emojis.  

---

## 📂 Project Structure
ChatBot/
│-- chatbot.ipynb 
│-- README.md 
1️⃣OPEN JUPYTER NOTEBOOK /VS CODE
2️⃣ Run the chatbot
python chatbot.py

🎮 Example Run
🤖 Welcome to ChatBot! Type 'bye' anytime to exit.

Before we start, may I know your name? Nikita
Bot: Nice to meet you, Nikita! 👋 Type 'help' if you need options.

Nikita: hi
Bot: Hey Nikita! How’s your day going?

Nikita: time
Bot: The current time is 07:45 PM

Nikita: joke
Bot: Why don’t scientists trust atoms? Because they make up everything! 😆

Nikita: bye
Bot: Bye Nikita! It was nice chatting with you. 👋
Bot: Here’s what we talked about today:
  1. hi
  2. time
  3. joke
  4. bye

🛠 Tech Stack

Python 3

datetime (for time & date)

random (for jokes/facts)

🌟 Future Improvements

Connect with a real Weather API for live updates 🌦

Add NLP support with libraries like NLTK or spaCy 🤓

Build a GUI version using Tkinter or Flask for web.
