# import libraries
import uuid

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from chatbot.chatbotengine import ChatBotEngine, respond, start_chat

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

chatbot_engine = ChatBotEngine()


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    return start_chat()


@app.route('/chat')
def chat():
    query = request.args.get('message')
    responses = respond(query)
    msg_id = str(uuid.uuid1())
    message = {"response": responses, "id": msg_id}

    return message


if __name__ == '__main__':
    app.run(debug=True)
