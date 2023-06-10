import nltk

females = ['wife', 'mom', 'sister', 'grandma', 'aunt', 'grandmother', 'dauther', 'tigress', 'lioness']

males = ['dad', 'father', 'brother', 'grandpa', 'cousin', 'uncle', 'co-worker', 'co worker', 'man', 'boy', 'son', 'dog', 'cat', 'horse', 'rabbit', 'pet', 'animal']

plurals = ['friends', 'family', 'community', 'social', 'people', 'mates', 'teammates']


def get_pronoun(cause_sentence):
    text = nltk.word_tokenize(cause_sentence)
    tags = nltk.pos_tag(text)
    for tag in tags:
        if(tag[1] == 'NN' or tag[1] == 'NNP'):
            if(tag[0] in females):
                return "she"
            elif(tag[0] in males):
                return "he"
            else:
                return "they"

def get_object_pronoun(cause_sentence):
    text = nltk.word_tokenize(cause_sentence)
    tags = nltk.pos_tag(text)
    for tag in tags:
        if(tag[1] == 'NN' or tag[1] == 'NNP'):
            if(tag[0] in females):
                return "her"
            elif(tag[0] in males):
                return "him"
            else:
                return "them"