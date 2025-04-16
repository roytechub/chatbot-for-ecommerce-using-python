🛒 E-commerce Chatbot using Python & Flask
An intelligent chatbot built using Python and Flask for e-commerce platforms. It can handle user queries, assist with product navigation, and respond to common customer questions. The chatbot is integrated into a web interface with basic routes and templates.


📌 Features
🧠 NLP-based chatbot for intelligent responses
🛍️ Product page route (/product) with UI integration
💬 Chat interface via AJAX (Flask + JS)
🔍 Dynamic response system using JSON
📁 Modular code (chat logic, model training, and routes separated)

🛠️ Tech Stack
Backend: Python 3, Flask
Frontend: HTML, CSS, JavaScript
NLP: NLTK / custom model
Others: JSON, Pickle

📁 Project Structure
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

🚀 How to Run
1. Clone the Repository
git clone https://github.com/roytechub/chatbot-for-ecommerce-using-python.git
cd ecommerce-chatbot

3. Install Dependencies
pip install flask nltk

5. Train the Model (if needed)
python train.py

7. Start the Flask App
python app.py
Visit http://localhost:5000 to see it in action.

✨ Sample Routes
/ → Loads base.html

/product → Loads product.html

/predict → API route to get chatbot responses (AJAX POST)

🔥 Example Intents
{
  "tag": "greeting",
  "patterns": ["Hi", "Hello", "Is anyone there?"],
  "responses": ["Hello! How can I assist you today?"]
}

🧑‍💻 Author
Bidyut Roy
💼 Portfolio: https://github.com/roytechub

📃 License
MIT License. Free to use and modify with attribution.
