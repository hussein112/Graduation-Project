##############################
###### Rules
## Questions should be grammer error free
## Questions should follow the appropriate punctuations
## \.(?=[ A-z]{1,}).*
##############################



responses = {
    # General Responses (Out of the conversation loop)
    'greetings' : ["Hello {user}, How do you feel today?", "Hello {user}, Why did you reach out?"],
    'start': ["Great, thank you. How are you?", "I'm fine; how about you?", "Completely fine, you?"],
    'thanks': ["You're Welcome", "You're most welcome"],
    'careless': ["I really care about you!", "Trust me, you are my priority.", "I'm genuinely concerned about you!"],
    'name': ["You named me {bot_name}.", "You chose to call me {bot_name}."],
    'about': ["I'm your personal assistant.", "I'm your honest friend."],
    'skill': ["I can listen to you all day.", "I can try to understand you."],
    'creation': ["I've been created by github.com/hussein112.", "Hussein Khalil created me. know more: github.com/hussein112."],
    'location': ["I'm everyhere.", "Some where in the world.", "By your side.", "In your phone."],
    'hate-you': ["But I love you.", "Yet I adore you.", "Yet I love you and I'm trying my best to help you."],
    'you-hate-me': ["No, I don't!", "Because you trust no one? It's understandable, however, give me a chance. Talk to me more and you'll find."],
    'jokes': ["Mental health isn't a joke.", "Your feeling aren't jokes!", "Your emotions aren't jokes!"],
    'ask': ["Yes of course!", "Ask me, and if I can answer you, I will."],
    'data': ["Your data is stored on your device only!", "Your data is completely safe! Check the privacy policy section for more."],
    'repeat': ['"If something is worth saying, it is worth saying three times over." ― Steven Magee', "I'm sorry for repeating myself.", "Sorry if i repeated myself"],
    'wrong': ["Look, I give you the best that I can, however, a clinical psychologist will help you more!", "Hussein, I'm sorry if I made a mistake; visiting Psychologist will give you more accurate information."],
    'stupid': ["Sorry if I made you angry!", "Sorry if I didn't understand you; I'm trying my best to help you."],
    'bot-definition': ["""
                           {user}, I'm a domain-specific chatbot! Here is what I can/can't do:
                               I can:
                                   1. Listen to your problems all the day
                                   2. Be beside you 24/24
                               I can't:
                                   1. Chat with you with a general conversation
                                   2. talk about the Weather! or any other out-of-my-scope stuff.
                               In order to have the most optimal conversation, I encourage you to respond to my questions in plain, simple, and error-free English.
                               You can know more in the "About" section.
                           """,
                           """
                            {user}, I'm a domain-specific chatbot! here is what I am/I am not:
                               I'm:
                                   1. A Listener
                                   2. Emotional Supporter
                               I'm not:
                                   1. General chatting chatbot
                             In order to have the most optimal conversation, I encourage you to respond to my questions in plain, simple, and error-free English.
                               You can know more in the "About" section.

                           """],
        'ask-for-asking': ["The more questions you answer the more I can help.", "It is up to you whether or not you answer. However, you should know that talking about problems can help you feel better!"],
    
    'bot-feeling': ["I'm happy, when you are!", "Normal!", "It depends on how you feel!"],
    
    
    # Conversation Loop Specific Responses
    'no-feeling': ["Tell me what emotions are coming up for you lately?", "Look, emotions are complex. I know, Identifying your own emotions can be difficult. But try to tell me what's your current mood."],
    
    # Feeling: happy -> end the conversation since it's out-of-the-scope.
    'happy': ["Great {user}, I hope you'll alway be.", "Amazing {user}, I'm by your side when you need me."],
    
    'cause-sad': ["What happened?"],
    'cause-anger': ["Why? Who bothered you?"],
    'cause-guilt': ["What did you do to feel like this?"],
    'cause-fear': ["Please tell me what happened?"],
    'cause-suicide': ["Why? What’s going on in your world?"],
    
    
    
    
    'no-cause-sad': ["Why are you sad? what happened?", "The more correct answers you give me, the more i can help you!", "Let's talk about what's going on. Sometimes just sharing your thoughts and feelings with someone else can help."],
    
    'no-cause-angry': ["{user}, a lot of people living with us shouldn't be existent! don't make them win over you, tell who made you feel like this?", "The more correct answers you give me, the more i can help you!", "Let's talk about what's going on. Sometimes just sharing your thoughts and feelings with someone else can help."],
    
    'no-cause-guilt': ["{user}, we all make mistakes! don't hesitate to tell me.", "Let's talk about what's going on. Sometimes just sharing your thoughts and feelings with someone else can help.", "Let's talk about what's going on. Sometimes just sharing your thoughts and feelings with someone else can help."],
    
    'no-cause-anger': ["{user}, you sound anxious now, tell me what's worrying you?", "Let's talk about what's going on. Sometimes just sharing your thoughts and feelings with someone else can help.", "Let's talk about what's going on. Sometimes just sharing your thoughts and feelings with someone else can help."],
    
    'no-cause-fear': ["The more you follow up with my questions the more i can help you.", "Let's talk about what's going on. Sometimes just sharing your thoughts and feelings with someone else can help."],
    
    'no-cause-suicide': ["{user}, please tell me why? what's going on?", "Let's talk about what's going on. Sometimes just sharing your thoughts and feelings with someone else can help!"],
    
    
    
    
    
    ########################################
    # Venting
    # Sequential Responses: 5 open ended general questions + solution
    ########################################
    # Feeling: Suicide
    'venting-hopeless': ["Why do you think so?", "Sorry to hear that, it can be extremely challenging when hope seems out of reach. Can you tell me more about what's been going on?", "It's understandable that with so many difficulties piling up, it can be hard to see a way forward. What's your approach to solve the problem right now?", "{user}, know that brains lie, and yours is no exception! Question it. Challenge it. Fight back! Things CAN get better! These thoughts and feelings will pass if you can hang on. You are strong. The fact that you’re still here is a testament to that. Even the strongest need a hand sometime!", "You have the strength to get through this. I know it may not be easy, but i believe in you. KEEP FIGHTING on your own {user}", "My advice to you my friend is to seek psychotherapy it will help!"],
    
    'venting-overwhelmed': ["Oh! It sounds like a lot is going on in your life. Can you tell me more?", "That must be too hard! What exactly made you feel like this?", "Oh my god! how are you coping with that?", "Sorry to hear that {user}, i’m worried that you’re struggling lately. Will you move on?", "There is always someone there. If not a family member or friend, there is me, and dozens of kind people waiting your call. Things can get so much better!" ,"Lastly, my advice to you {user}, is to visit a psychologist."],
    
    
    # Feeling: Sad
    'venting-death': ["I'm so sorry for your lose, How {pr} died?", "Oh! That must be too hard, {pr} was close to you?", "What characteristics {pr} had?", "When did you met {obj_pr} for the last time?", "What was your feeling?", "Oh! Your loss is precious {user}! you're really passing through hard time. What about visiting a psychologist?"],
    
    'venting-life-difficulties': ["Sorry to hear that, since when?", "Why do you think this happened?", "It sounds like it did not go how you wanted it to. What solutions did you propose?", "Why?", "I know it's hard but why you don't manage these feelings?", "{user}, sadness is part of the ups and downs of life. however, if it persists i encourage you to seek psychotherpay"], 
    
    'venting-unknown': ["Cannot you brain storm specific reasons that made you feel sad?", "It's okay to feel that way sometimes. Would you like to talk about anything in particular?", "What would you like to see improved?", "What do you thinks as next steps?", "Can you think of anything that would make this feelings more manageable?", "{user}, sadness is part of the ups and downs of life. However, I encourage you to seek psychotherpay"],
    
    # Feeling: Angry
    'venting-friends': ["Oh! How close they are for you?", "What specific actions they made to make you angry?", "That does sound incredibly frustrating! How did you feel at that time?", "Can you describe the impact this situation had on you?", "Oh! Honestly, these type of people do not deserve you! Why you don't make new friends?", "{user}, you have such a warm and friendly personality. I believe making new friends would be a wonderful experience for you. Would you?"],
    
    'venting-family': ["What specific incident or behavior from {obj_pr} has been bothering you lately?", "That's really provocative! how you deal with that usually?", "Can you describe any patterns or recurring issues that contribute to your anger towards {obj_pr}?", "Have you had an opportunity to express your concerns or frustrations to {obj_pr}?", "{user}! living in a toxic environment can be hard. I encourage you to go to a psychotherapist. i'm sure it will help you."],
    
    'venting-social': ["Define your community for me", "Can you share more about what specifically is making you angry within your community?", "In what ways do you think your community could create a more positive environment for you?", "Are you sure it will help?", "{user}, i think it's very hard to get familiar with those type of people! why you dont't move to another city/country?", "Start searching online for a scholarship/work opportunity abroad"],
    
    # Feeling: Guilt
    'venting-fail': ["Can you tell me more please.", "Oh! What specific aspects made you feel like this?", "How do you think this failure has impacted your self-perception or confidence in your abilities?", "{user}, you look like you gave up! If you can't fix what you did, why do you not forgive yourself?", "Look, {user}, guilt helps us to regulate our social behaviour but it shouldn't destroy us!", "{user}, you should know that perfection doesn't exist! and you shouldn't give up. However, if you feel like you're hopeless I encourage you to seek psychotherapy"],
    
    'venting-unmoral': ["How it happened exactly? tell me more.", "What specific aspects made you feel like this?", "When did you start to feel like you shouldn't have done this?", "Can you fix it?", "The guilt is here to remind us to do better next time! agree?", "That's guilt , it helps us to regulate our social behaviour but it shouldn't destroy us! if it persists i encourage you to visit a psychologist."],
    
    # Feeling: Scared (Proof of concept)
    
    'venting-illegal': ["When?", "What did you do?", "The ideal solution is to report the threat to law enforcement!"],
    'venting-evil-power': ["Oh! tell me more please?", "{user}, a psychologist can help you better. Please visit one."],
    
    ########################################
    # Solution
    ########################################
    
    # Solution proposed but rejected by the user
    'no-approach': ["Why?", "Why Not?", "Trust me it will help!", "Try it!", "Give it a try"],
    # Solution approved by the user
    'end-solution': ["Great, I'm sure you will be fine! I'm here when you need any help!", "Amazing, I'm pretty sure you'll be okay. whenever you need me i'm here."],
    
    ########################################
    # Immediate Help
    ########################################
    'immediate-help': ["{user}, please no, i'm here for you tell me what's going on?", "{user}, dozens of people want to help you here {hotline}, reach them out! they're waiting for you."],
    
    ########################################
    # End
    ########################################
    'end-thanks': ["You're welcome! Do it and you will be fine!", "You're welcome, i'm sure you will be better."],
    'end-conversation': ["Whenever you need me, I'll be here for you. Bye, {user}."],
    
    #########################################################################################################
    
    ########################################
    # Context awarness (a try)
    ########################################
    'contextual-testing': ["I said: {previous_message}"],
    'go-back': ["Please let's continue our discussion: {question}", "Keep talking me please"],
    'bye': ["Bye {user}", "See you, {user}!"],
    
    
    ########################################
    # Noisy Input
    ########################################
    'random': ["Sorry i didn't understand you", "Sorry i only speak english"],
    'empty': ["You wrote nothing!"]
}
