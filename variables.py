conversation_loop = {
    'feeling': None,
    'feeling_': None, # Feeling happy -> outside the loop
    'cause': None,
    'venting': -1,
    'solution': -2,
    'ending': -1,
}


dialogue = {
    'escaped_context_counter': 0, # How many time the user goes outside the current loop element
    'last_contextual_prompt': None,
    'last_contextual_question': None, # Last question from the prompt inside the current loop element
}

context_ = []
escaping_context = '' # The current loop element, used in classification to determine if the user trying to escape the current context (loop element)


user_meta = {
    'name': "Hussein",
    'hotline': "03/123 456",
    'bot-name': "Joe",
    'CSSRS': 1
}

context = {
    'pronoun': None,
    'object_pronoun': None,
}


conversation_history = {}

conversation_state = True


# For if-else 
suicide_classes = ['suicide', 'death', 'self-harm']