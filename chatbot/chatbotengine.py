from datetime import datetime

import chatbot
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from chatbot.nltkchatutil import Chat, reflections
import langid

from chatbot.dialoginput import DialogInput

dialog_input = DialogInput()


def get_default_error():
    error_msg = "Sorry, I don't understand your sentence 🤷!"
    return error_msg


def find_match(query):
    ration_to_value = {'ratio': 0, 'key': ''}
    prev_ratio = 0
    for i in dialog_input.dialogs:
        ratio = fuzz.token_set_ratio(query, i[0])

        if ratio > 90 and ratio > prev_ratio:
            prev_ratio = ratio
            ration_to_value['ratio'] = ratio
            ration_to_value['key'] = i[0]
            if ratio == 100:
                return ration_to_value
    return ration_to_value


def respond(query):
    modified_query = find_match(query)
    pairs = dialog_input.dialogs
    chat = Chat(pairs, reflections)
    outputs = chat.converse(modified_query['key'])
    if outputs is None:
        outputs = get_default_error()
    return outputs


def start_chat():
    return "Hi, I'm Covid Guard and I chat alot ;) I can answer your question regarding Coronavirus(Covid-19)"


class ChatBotEngine(object):
    def __init__(self):
        start_chat()
