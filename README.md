# 🩺 AI-Powered Healthcare Assistant

An intelligent, interactive healthcare chatbot built with **Streamlit**, **Hugging Face Transformers**, and **NLTK**. This lightweight assistant blends rule-based logic and a fine-tuned AI model to help users get relevant health-related responses in real-time.

---

## 🚀 Features

- 🔍 **Hybrid Intelligence**: Combines keyword-based rule logic with GPT-powered natural language generation.
- 💬 **Real-time Responses**: Delivers context-aware replies to common medical queries.
- 🧠 **Optimized NLP Pipeline**: Uses `DistilGPT2` for efficient text generation on CPU.
- 🛡️ **Safe & Guided Outputs**: Prioritizes safe, informative responses for common health concerns.
- 🌐 **Web Interface**: Simple and elegant UI built with Streamlit.

---

## 🛠️ Tech Stack

| Technology       | Description                                |
|------------------|--------------------------------------------|
| 🐍 Python         | Core programming language                  |
| 🤖 Transformers  | Text generation with `distilgpt2`          |
| 🧠 NLTK           | Text preprocessing, stopword removal       |
| 🌐 Streamlit      | Interactive web app framework              |

---

## 📦 Installation

> **Requirements**: Python 3.8+

1. **Clone the Repository**

```bash
git clone https://github.com/SoumyajitPaul-git/ai-healthcare-assistant.git
cd ai-healthcare-assistant
```

2. **Create & Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate  # On macOS/Linux
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the App**

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
.
├── app.py                  # Main Streamlit app
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── nltk_data               # NLTK data (downloaded on runtime)
```

---

## ✨ Example Usage

```text
User: I have fever and headache.
Bot: A fever could indicate an infection. Stay hydrated and consider consulting a doctor if it persists.
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💡 Future Enhancements

- 🗂️ Integrate with Electronic Health Records (EHR) APIs
- 🏥 Schedule real appointments via integrated services
- 🌍 Multilingual support
- 🔒 Secure user authentication

---

## 🙋‍♂️ Disclaimer

This assistant **does not provide medical advice** and should not be considered a substitute for professional medical consultation. For any medical emergencies or concerns, please consult a certified healthcare provider.


---


## 📬 Contact

Made with ❤️ by Soumyajit Paul
GitHub: [github.com/SoumyajitPaul-git](https://github.com/SoumyajitPaul-git)  
