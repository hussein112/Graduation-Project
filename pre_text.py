import nltk
from nltk.corpus import words, stopwords
from nltk.stem import PorterStemmer
english_words = words.words()

import string
import re

import random

from chat_tools.chat import chat as ch
chat = ch

from chat_tools.mappings import mappings as typicals
from chat_tools.responses import responses as rs
responses = rs

# Map chatting words to english
def chat_to_english(text):
    """
    Description:
    This function maps chatting words or abbreviations to their corresponding English equivalents. It takes a text string as input and processes it by tokenizing the text into individual words. It then checks each word against a predefined dictionary of chatting words and replaces them with their English counterparts if a match is found. Finally, the function reassembles the modified tokens into a single string and returns it.

    Parameters:

    text: A string representing the input text to be processed and mapped to English.
    Returns:

    A string containing the modified text with chatting words replaced by their English equivalents.
    Example Usage:
    text = "omg ikr, that's so cool!"
    mapped_text = chat_to_english(text)
    print(mapped_text)
    Output: "oh my god I know, that is so cool!"

    Note:
    The function relies on a dictionary called 'chat' that maps chatting words to their English counterparts. The 'chat' dictionary should be defined and populated prior to using this function.
    """
    if('.' in text):
        text = ''.join(text.split('.')) # 'id.k...' ----> idk
    tokens = nltk.word_tokenize(text.lower())
    for x in range(0, len(tokens)):
        if tokens[x] in chat:
            tokens[x] = chat[tokens[x]]
    return ' '.join([token for token in tokens])


def sanitize_input(user_input):
    user_input = user_input.strip()
    user_input = user_input.lower()
    user_input = chat_to_english(user_input)
    return user_input



def is_random(user_input):
    # Remove Punctuations
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))
    
    # Search of spaces inside the input. i.e., determine if it's single/multiple word
    if not re.search(r"[A-z]\s[A-z]", user_input, re.IGNORECASE):
        if(user_input in english_words or user_input.capitalize() in english_words):
            return False
        return True
     
    stemmer = PorterStemmer()
    user_input_tokens = nltk.word_tokenize(user_input)
    stemmed_user_input_tokens = []
    for token in user_input_tokens:
        stemmed_user_input_tokens.append(stemmer.stem(token))
    
    score = 0
    stemmed_score = 0
    
    for token in user_input_tokens:
        if token in english_words or token.capitalize() in english_words:
            score += 1
        else:
            score -= 1
            
    for token in stemmed_user_input_tokens:
        if token in english_words or token.capitalize() in english_words:
            stemmed_score += 1
        else:
            stemmed_score -=1
    
    if(stemmed_score > score):
        score = stemmed_score
    
    if round((score / len(user_input_tokens)) * 100) >= 50:
        return False
    return True



def is_empty(user_input):
    if user_input == "":
        return True
    elif user_input.isspace():
        return True
    else:
        return False
    
    
def is_noisy(user_input):
    is_related, previous_prompt = is_related_to_previous_prompt(user_input)
    return True

def noisy_input():
    return random.choice(responses['bot-definition'])

def remove_punc(_string):
    new_string = _string.translate(str.maketrans('', '', string.punctuation))
    return new_string.strip()

  

def is_typical(user_input):
    user_input = remove_punc(user_input)
    for key in typicals.keys():
        if(user_input in key.split(',')):
            return True
    return False


def get_typical_response(user_input):
    user_input = remove_punc(user_input)
    for question, response in typicals.items():
        if user_input in question.split(','):
            return response