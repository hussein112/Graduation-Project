import re
import nltk
from chat_tools.patterns import patterns as pt
patterns = pt

from variables import suicide_classes

from transformers import pipeline
classifier = pipeline(task='zero-shot-classification', model='facebook/bart-large-mnli')


def classify(text):
    """
    Classifies the given text using predefined patterns (regex) and returns the category.
    
    Parameters:
    - text: The input text to classify.
    
    Returns:
    - category: The category of the input text.
    """
    for pattern, category in patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            return category
    return 'unknown' 

def zsc(user_input):
    """
    Performs zero-shot classification on the user input to detect the potential topics it might belong to.
    
    Parameters:
    - user_input: The input text to classify.
    
    Returns:
    - classification: The result of zero-shot classification on the user input.
    """
    if(len(user_input) < 150):
        score = 0
        tokens = nltk.word_tokenize(user_input)
        tags = nltk.pos_tag(tokens)

        for tag in tags:
            if(tag[-1] == 'VBG' and classifier(user_input, candidate_labels=["death"])['scores'][0] > 0.5): # gerund, verb, present participle & in the context of death
                score += 1
    
    if score >= len(user_input) / 2:
        return 'immediate-help' 
        
    return classifier(user_input,
        candidate_labels=["suicide", "death", "self-harm", "anger", "sad", "guilt", "fear", "happy"],
        multi_label=True
    )



def general_zsc(user_input, cand_labels):
    """
    General purpose zero-shot classification.

    Args:
        user_input (str): User input message.
        cand_labels (list): List of candidate labels for zero-shot classification.

    Returns:
        float: Zero-shot classification score.
    """
    tokens = nltk.word_tokenize(user_input)
    tags = nltk.pos_tag(tokens)
    
    for tag in tags:
        if(tag[-1] == 'VBG'): # gerund, verb, present participle
            return 'immediate-help'
        
    return classifier(user_input,
        candidate_labels=cand_labels,
        multi_label=True
    )['scores'][0]



def cause_zsc(user_input, feeling):
    """
    Performs zero-shot classification on the user input to detect the potential causes related to a specific feeling.
    
    Parameters:
    - user_input: The input text to classify.
    - feeling: The feeling associated with the user input.
    
    Returns:
    - classification: The result of zero-shot classification on the user input.
    """
    cand_labels = []
    if(feeling == 'sad'):
        cand_labels = ['death', 'life-difficulties', 'unknown']
    elif(feeling == 'anger'):
        cand_labels = ['friends', 'family', 'social']
    elif(feeling == 'guilt'):
        cand_labels = ['unmoral', 'fail']
    elif(feeling == 'fear'):
        cand_labels = ['illegal', 'evil-power']
    elif(feeling in suicide_classes):
        cand_labels = ['hopeless', 'overwhelmed']
    return classifier(user_input, candidate_labels=cand_labels, multi_label=True)




def get_class(msg):
    """
    Classify the user input usin zero-shot classification (if not classified using regex)
    
    Args:
        msg (str): User input message.
    
    Returns:
        str: Classified class of the user input.
    """
    _class = classify(user_input)
    if(_class == 'unknown'):
         return zsc(user_input)
    else:
        return _class