# chatbot.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

def process_input(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in tokens if w not in stop_words]
    return filtered_words

def generate_response(user_input):
    responses = {
        "hello": "Hello! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "what its tegar?": "Tegar this guy🗿"
    }
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm sorry, I don't understand."
