from flask import Flask, request, jsonify, session, render_template
from flask_cors import CORS
import json

from urllib.parse import unquote
from dialogue_manager.dm import *

from variables import *


def send_response(user_input):
    if(conversation_loop['ending'] == 1):
        chatting = False
        return

    response = generate_response(user_input)

    if(len(conversation_history) > 0):            
        response = response.format(hotline=user_meta['hotline'], pr=context['pronoun'], obj_pr=context['object_pronoun'], user=user_meta['name'], bot_name=user_meta['bot-name'], question=dialogue['last_contextual_question'], previous_message=conversation_history[list(conversation_history)[-1]])
    else:
        response = response.format(hotline=user_meta['hotline'], pr=context['pronoun'], obj_pr=context['object_pronoun'], user=user_meta['name'], bot_name=user_meta['bot-name'])

    if(user_input in conversation_history):
        user_input = user_input + "_duplicate"
    conversation_history[user_input] = response

    if(get_conversation_state() == False):
        chatting = False
        reset_conversation_loop()
        return jsonify(resp =response, status='end')

    if(user_meta['CSSRS'] >= 2 and conversation_loop['venting'] != -1 and conversation_loop['solution'] != 1):
        conversation_history[user_input] = response
        return jsonify(resp =response, hotline="I encourage you to call: 12345")
    else:
        return jsonify(resp =response)


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    user_input = request.args.get('input')
    user_input = unquote(user_input).replace('%22', ' ')
    user_input = unquote(user_input).replace('%20', ' ')
    extract_meta(request)
    return send_response(user_input)

def extract_meta(request):
    user_name = request.args.get('user_name')
    if user_name != None:
        user_name = unquote(user_name).replace('%22', ' ')
        user_meta['name'] = user_name
        
    bot_name = request.args.get('bot_name')
    if bot_name != None:
        bot_name = unquote(bot_name).replace('%22', ' ')
        user_meta['bot-name'] = bot_name
    
    CSSRS = request.args.get('CSSRS')
    if CSSRS != None:
        CSSRS = unquote(CSSRS).replace('%22', ' ')
        user_meta['CSSRS'] = int(CSSRS)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.105')
    
# To run the API, you can save the code to a file (e.g. app.py), and then run the following command in your terminal:
# FLASK_APP=app.py flask run

