# E-commerce Chatbot using Python & Flask

An intelligent chatbot built using Python and Flask for e-commerce platforms. It can handle user queries, assist with product navigation, and respond to common customer questions. The chatbot is integrated into a web interface with basic routes and templates.

---

## 🚀 Features

- 🧠 NLP-based chatbot for intelligent responses
- 🛍️ Product page route (/product) with UI integration
- 💬 Chat interface via AJAX (Flask + JS)
- 🔍 Dynamic response system using JSON
- 📁 Modular code (chat logic, model training, and routes separated)

---

## 🛠️ Tech Stack

| Layer       | Tech Used                         |
|------------|-----------------------------------|
| Frontend   | HTML5, CSS, JavaScript  |
| Backend    | Python, Flask                     |
|NLP  | NLTK / custom model |
| Others    | JSON, Pickle                       |

---

## 📂 Project Structure

```
ecommerce-chatbot/
├── app.py                 # Main Flask app with route handling
├── chat.py                # Chatbot logic and response generation
├── model.py               # Handles model loading or predictions
├── train.py               # Train chatbot with intents.json
├── nltk_utils.py          # Tokenization, stemming, bag of words
├── data.pth               # Trained model data (torch/pickle)
├── intents.json           # Training data for chatbot
│
├── static/
│   ├── app.js             # JS for frontend chat interaction
│   ├── style.css          # Basic styling
│   └── images/            # Placeholder for any assets
│
├── templates/
│   ├── base.html          # Homepage
│   └── product.html       # Product page
│
└── venv/                  # Virtual environment
```

---

## 🧪 Getting Started

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/ecommerce-chatbot.git
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install flask
```

### 4️⃣ Train the Model (if needed) and Run the App

```bash
python train.py
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Example Intents
```bash
{
  "tag": "greeting",
  "patterns": ["Hi", "Hello", "Is anyone there?"],
  "responses": ["Hello! How can I assist you today?"]
}
```
---

## 🤝 Contributing

Pull requests are welcome. Open issues for suggestions or bugs. 
**Support Us**
https://aniclothe.roytechub.com/

---

## Author
Bidyut Roy
💼 Portfolio: https://github.com/roytechub

## ☺️ Happy Coding
