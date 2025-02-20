import streamlit as st
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.data.path.append('/usr/share/nltk_data')
nltk.download('punkt', force=True)
nltk.download('stopwords', force=True)


# Load a pre-trained optimized model
chatbot = pipeline("text-generation", model="distilgpt2", device=-1)  # Uses CPU (-1) for efficiency


# Function to preprocess user input (remove stopwords for better model performance)
def preprocess_text(text):
    words = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    filtered_words = [
        word for word in words if word.isalnum() and word not in stopwords.words("english")
    ]
    return " ".join(filtered_words)


# Enhanced healthcare response function
def healthcare_chatbot(user_input):
    user_input = preprocess_text(user_input)  # Clean user input
    
    # Rule-based responses for healthcare queries
    keyword_responses = {
        "symptom": "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice.",
        "appointment": "Would you like me to schedule an appointment with a doctor?",
        "medication": "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor.",
        "fever": "A fever could indicate an infection. Stay hydrated and consider consulting a doctor if it persists.",
        "pain": "Pain can have many causes. If the pain is severe or persistent, please seek medical help.",
        "emergency": "If you are experiencing a medical emergency, please call emergency services immediately.",
    }

    # Check for rule-based responses first
    for keyword, response in keyword_responses.items():
        if keyword in user_input:
            return response

    # If no rule-based match, use AI model to generate response
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    return response[0]["generated_text"]


# Streamlit Web App Interface
def main():
    st.set_page_config(page_title="AI Healthcare Assistant", layout="centered")

    # App Title
    st.title("🩺 AI-Powered Healthcare Assistant")

    # User input field
    user_input = st.text_input("How can I assist you today?", "")

    # Button to submit query
    if st.button("Submit"):
        if user_input:
            response = healthcare_chatbot(user_input)
            st.write("🗣 **User:**", user_input)
            st.write("🤖 **Healthcare Assistant:**", response)
        else:
            st.warning("Please enter a query to proceed.")


if __name__ == "__main__":
    main()
