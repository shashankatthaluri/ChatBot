from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a new chatbot
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

# Function to generate response based on user input
def generate_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling user input and generating response
@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)
