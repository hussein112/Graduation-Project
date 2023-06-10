'''
    File: chatbot.py
    @author: Hussein Khalil, github.com/hussein112

    Description:
    .....The code includes various functions and components that enable context maintenance, sentiment analysis, cause identification, and solution proposal.

    The main purpose of this chatbot is to provide a conversational interface that can simulate human-like interactions and assist users in addressing their concerns, discussing emotions, and proposing solutions. The code incorporates natural language processing techniques, such as text classification, sentiment analysis, and context analysis, to enhance the chatbot's understanding and response generation capabilities.
    ..........
    
    
     @@@D --> Debugging
'''

import re
import random
# nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')


from chat_tools.responses import responses as rs
from chat_tools.casual_responses import casual_responses as cs


#####################
### Functions
####################
from pre_text import *
from pronouns import *
from classification import *

#####################
### Variables (Conversation loop, dialogue, context, conversation_state, user info)
####################
from variables import *


def reset_conversation_loop():
    """
    Create new chat
    
    Resets the conversation loop by clearing the conversation state and context variables.
    """
    global conversation_state
    global escaping_context
    conversation_loop.update({
        'feeling': None,
        'feeling_': None, # Feeling happy -> outside the loop
        'cause': None,
        'venting': -1,
        'solution': -2,
        'ending': -1,
    })
    dialogue.update({
        'escaped_context_counter': 0,
        'last_contextual_prompt': None,
        'last_contextual_question': None,
    })

    conversation_state = True
    context.update({
        'pronoun': None,
        'object_pronoun': None,
    })
    context_.clear()
    escaping_context = ''
    conversation_history.update({})
    

responses = rs
casual_responses = cs


def prepare_for_zsc(text):
    """
    Prepares the text for the ZSC (Zero Shot Classification) task.
    It removes stop words from the text and splits it into a list of words.

    Parameters:
    - text: The input text to be prepared for ZSC.

    Returns:
    - A list of words after removing stop words and splitting the text.
    """
    text = ''.join([word + '-' for word in text.split(' ') if word not in stop_words])
    return text.split('-')


def is_related_to_previous_prompt(user_input):
    """
    Check if the user input is related to the previous prompt in the conversation context.
    
    Args:
        user_input (str): User input message.
    
    Returns:
        list: A list containing a boolean value indicating if the input is related to the previous prompt,
              and the previous prompt if it is related.

    FOR MORE ACCURACY: we can get synonyms, and different of the word to be classified.
    e.g., 'creation' => 'created' = past, 'made' => synoym...
    """
    if(len(context_) >= 2):
        if(general_zsc(user_input, context_[-1]) > 0.5):
            if(context_[-1]):
                context_.remove(context_[-1])
                return [True, context_[-1]]
        elif(general_zsc(user_input, context_[-2]) > 0.5):
            if(context_[-2]):
                context_.remove(context_[-2])
                return [True, context_[-2]]
    elif(len(context_) == 1):
        if(general_zsc(user_input, context_[-1]) > 0.5):
            if(context_[-1]):
                context_.remove(context_[-1])
                return [True, context_[-1]]
    return [False, ""]

    

def get_feeling(user_input):
    """
    Extract the feeling from the user input.
    
    Args:
        user_input (str): User input message.
    
    Returns:
        str: Response based on the extracted feeling.
    """
    global escaping_context
    _class = zsc(user_input)
    if(_class == 'immediate-help'):
        return immediate_help()
    if(_class['scores'][0] > 0.5):
        if(_class['labels'][0] == "happy"):
            conversation_loop['feeling_'] = _class['labels'][0]
            return random.choice(responses["happy"])
        if(_class['labels'][0] in suicide_classes):
            conversation_loop['feeling'] = 'suicide'
            escaping_context = 'cause-'+conversation_loop['feeling']
            return random.choice(responses['cause-'+conversation_loop['feeling']])
        else:
            conversation_loop['feeling'] = _class['labels'][0]
            escaping_context = 'cause-'+conversation_loop['feeling']
            return responses['cause-'+conversation_loop['feeling']][0]
    elif(_class['labels'][0] in suicide_classes): # Potential Danger
        conversation_loop['feeling'] = 'suicide'
        escaping_context = 'cause-'+conversation_loop['feeling']
        return random.choice(responses['cause-'+conversation_loop['feeling']])
    else: # Cannot Extract feeling from user input
        escaping_context = 'feeling'
        return random.choice(responses['no-feeling'])

def immediate_help():
    """
    Call hotline
    Try to calm the user down
    """
    return random.choice(responses['immediate-help'])
    
def get_cause(feeling, user_input):
    """
    Extract the cause based on the feeling and user input.
    
    Args:
        feeling (str): Feeling extracted from the user input.
        user_input (str): User input message.
    
    Returns: (Start the venting process)
        str: Response based on the extracted cause.
    """
    global escaping_context
    _class = cause_zsc(user_input, feeling)
    if(_class['scores'][0] > 0.5):
        conversation_loop['cause'] = _class['labels'][0]
        context['pronoun'] = get_pronoun(user_input)
        context['object_pronoun'] = get_object_pronoun(user_input)
        escaping_context = conversation_loop['cause']
        return start_venting(conversation_loop['cause'], user_input)
    else: # Cannot Extract cause from user input
        escaping_context = 'cause-' + feeling
        return random.choice(responses['no-cause-' + feeling])
        

def start_venting(cause, user_input):
    """
    Start the venting process for a specific cause.
    
    Venting process consists of 5 general open-ended questions + a solution at the end.
    
    Args:
        cause (str): Cause for venting.
        user_input (str): User input message.
    
    Returns:
        str: Response for the venting process.
    """
    global escaping_context
    conversation_loop['venting'] = conversation_loop['venting'] + 1
    index = conversation_loop['venting']
    if(index >= len(responses['venting-'+cause]) - 1):
        return propose_solution(conversation_loop['cause'])
    escaping_context = 'venting-'+cause
    return responses['venting-'+cause][index]

def propose_solution(cause):
    """
    Last step in the venting process, propose a solution for a specific cause.
    
    Args:
        cause (str): Cause for proposing a solution.
    
    Returns:
        str: Proposed solution for the cause.
    """
    global escaping_context
    escaping_context = 'approach'
    conversation_loop['solution'] = -1
    return responses['venting-'+cause][-1]


def get_satisfiction(user_input):
    """
    Determine the user's satisfaction with the proposed solution.
    
    Args:
        user_input (str): User input message.
    
    Returns:
        str: Response based on the user's satisfaction.
    """
    global escaping_context
    regex_reject = r"(i can't|i cannot|no|i don't want)"
    regex_approve = r'(ok|i will|yes)(try|shall|should|could|might)?'
    
    if(re.search(regex_reject, user_input, re.IGNORECASE)):
        conversation_loop['solution'] = 0
        escaping_context = 'approach'
        return resisting_solution()
    elif(re.search(regex_approve, user_input, re.IGNORECASE)):
        conversation_loop['solution'] = 1
        escaping_context = 'solution-approved'
        return approved_solution()
    # Default
    escaping_context = 'approach'
    return resisting_solution()


def resisting_solution():
    """
    Generate a response when the user is resisting the proposed solution.
    
    Returns:
        str: Response for resisting the proposed solution.
    """
    return random.choice(responses['no-approach'])
  
    
def approved_solution():
    """
    Generate a response when the user approves the proposed solution. 
    The response should be trying to end the conversation
    
    Returns:
        str: Response for approving the proposed solution.
    """
    return random.choice(responses['end-solution'])
   
    
    
def is_out_of_context(user_input, _context):
    """
    Check if the user's input is out of context based on the conversation history and the last bot question.

    Args:
        user_input (str): User input message.
        _context (str): Context for the conversation.

    Returns:
        bool: True if the user's input is out of context, False otherwise.
    """
    proba = 0
    last_bot_question = ''
    
    user_input = remove_punc(user_input)

    if(len(conversation_history) >= 1):
        last_conv = conversation_history[list(conversation_history)[-1]]
        if(last_conv == responses['bot-definition'][0] or last_conv == responses['bot-definition'][1]):
            if(len(conversation_history) >= 2):
                last_conv = conversation_history[list(conversation_history)[-2]]
        dialogue['last_contextual_question'] = last_conv
        last_bot_question = remove_punc(last_conv)
        dialogue['last_contextual_prompt'] = last_bot_question
        
        if(classifier(user_input, candidate_labels=[_context, last_bot_question.lower()], multi_label=True)['scores'][0] < 0.4):
            proba += 3
        if(proba > 0):
            #######################
            ### @@@D
            #######################
#             print("2nd classification Candidate labels: ", prepare_for_zsc(last_bot_question.lower()))
            if(classifier(user_input, candidate_labels=prepare_for_zsc(last_bot_question.lower()), multi_label=True)['scores'][0] >= 0.93):
                proba -= 3
    
    elif(type(general_zsc(user_input, [_context])) is int and general_zsc(user_input, [_context]) < 0.4):
        proba += 3

    if(user_input in casual_responses): proba -= 1
    if(context['pronoun'] in user_input.split()): proba -= 0.5
    if(context['object_pronoun'] in user_input.split()): proba -= 0.5
    if(proba <= 2 and dialogue['escaped_context_counter'] >= 2): # the user_input within the context
        dialogue['escaped_context_counter'] = 1 # Decrement in order to continue classifying the latest bot prompt
    #######################
    ### @@@D
    #######################
#     if(last_bot_question != ''):
#         print("Bot question: ", last_bot_question)
#     print("Escaping Context: ", _context)
#     print("Final Probability: ", proba)
    return (proba >= 2)


def get_go_back_to_context_response():
    """
    Get a response to prompt the user to go back to the previous context.

    Returns:
        str: Response to prompt the user to go back to the previous context.
    """
    return random.choice(responses['go-back'])



def get_conversation_state():
    """
    Get the conversation state.

    Returns:
        str: Conversation state.
    """
    global conversation_state
    return conversation_state

  
    
def end_conversation(user_input):
    """
    End the conversation.

    Args:
        user_input (str): User input message.

    Returns:
        str: Response for ending the conversation.
    """
    conversation_loop['ending'] = 1 
    return random.choice(responses['bye'])

def get_response_from_context(context):
    """
    Get a response based on the given context (previous regex class)

    Args:
        context (str): Context for which to retrieve a response.

    Returns:
        str: Generated response based on the given context.
    """
    if context in responses: return random.choice(responses[context])
    return random.choice(responses['random'])
    
    
def generate_ending_response(user_input, thanks=False):
    """
    Generate a response for ending the conversation.

    Args:
        user_input (str): User input message.
        thanks (bool, optional): Whether to include thanks in the response. Defaults to False.

    Returns:
        str: Generated response for ending the conversation.
    """
    conversation_loop['ending'] = 0 # Start trying to end the conversation
    if(thanks):
        return random.choice(responses['end-thanks'])
    return random.choice(responses['end-conversation'])
    
    
def generate_response(user_input):
    """
    Preprocess the user_input & Generate a response based on the user input and the current conversation context.

    Args:
        user_input (str): User input message.

    Returns:
        str: Generated response based on the conversation context, loop and user input.
    """
    global escaping_context
    global conversation_state
    
    if(is_empty(user_input)):
        return random.choice(responses['empty'])
    
    #######################
    ### @@@D
    #######################
#     print("Escaping Context: ", escaping_context)
#     print("Context (Stack): ", context_)
#     print("Conversation_Loop: ", conversation_loop)
#     print("Conversation State: ", conversation_state)
#     print("Conversation History: ", conversation_history)
#     print("Escaping Context Counter: ", dialogue['escaped_context_counter'])

    if(len(conversation_history) <= 1):
        escaping_context = 'feeling' # in order to detect noisy input in the first prompt
        
        
    user_input = sanitize_input(user_input)
    
    casual_class = classify(user_input)
    
    
    if(casual_class != "unknown"):
        context_.append(casual_class)
        if(casual_class == "bye"): 
            conversation_state = False
            return random.choice(responses['bye'])
        elif(casual_class == 'thanks' and conversation_loop['solution'] == -1 or conversation_loop['solution'] == 1):
            return generate_ending_response(user_input, thanks=True)
        elif(casual_class == 'contextual-testing'):
            return random.choice(responses['contextual-testing'])
        return random.choice(responses[casual_class])        
    elif(is_typical(user_input)):
        return get_typical_response(user_input)
    elif(user_input in casual_responses and conversation_loop['feeling_'] != None): # Positive Feeling
        return "See you."
    elif(is_random(user_input)):
        return random.choice(responses['random'])
    elif(escaping_context != '' and is_out_of_context(user_input, escaping_context)):
        is_related, previous_context = is_related_to_previous_prompt(user_input)
        if(is_related):
            return random.choice(responses[previous_context])
        dialogue['escaped_context_counter'] += 1
        if(dialogue['escaped_context_counter'] >= 2 or len(conversation_history) == 0): # faulty input twice, or first prompt
            return noisy_input()
        return get_go_back_to_context_response()
    elif(conversation_loop['feeling'] == None): # get feeling
        return get_feeling(user_input)
    elif(conversation_loop['cause'] == None): # get cause
        return get_cause(conversation_loop['feeling'], user_input)
    elif(conversation_loop['solution'] == -1): # Solution Proposed
        return get_satisfiction(user_input)
    elif(conversation_loop['ending'] == 0): # trying to end the conversation
        return end_conversation(user_input)
    elif(conversation_loop['solution'] == 1): # Solution Accepted
        return generate_ending_response(user_input)
    elif(conversation_loop['solution'] == 0): # Solution Rejected
        return get_satisfiction(user_input)
    elif(conversation_loop['cause'] != None):
        return start_venting(conversation_loop['cause'], user_input)