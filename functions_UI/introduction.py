import random
from functions import *

def Introduction(r,mic):
    messages1 = ["Perfect. Now you'll get an introduction",
                'Lovely. You will now learn how to classify the sounds',
                'Great. We are now in the introduction part']
    
    messages2 = ["There are 5 different types of meteors: Underdense meteor.., M meteor.., long overdense meteor.., medium overdense meteor... And the short overdense meteor",
                'Meteors are classified into 5 different types, which are: Underdense meteor.., M meteor.., long overdense meteor.., medium overdense meteor... And the short overdense meteor']
    #FIRST SOUND
    messages3 = ["The first sound is the underdense meteor, which also will be called meteor one.",
                "The underdense meteor, which also will be called meteor one, sounds like this:"]
    #SECOND SOUND
    messages4 = ["The second sound is the M meteor also called meteor 2",
                "The M meteor or meteor 2 sounds like this:"]
    #THIRD SOUND
    messages5 = ["The third sound is the long overdense meteor also called meteor 3",
                "The long overdense meteor or meteor 3 sounds like this:"]
    #FOURTH SOUND
    messages6 = ["The fourth sound is the medium overdense meteor also called meteor 4",
                "The medium overdense meteor or meteor 4 sounds like this:"]
    #FIFTH SOUND
    messages7 = ["And the fifth sound is the short overdense meteor also called meteor 5",
                "And the short overdense meteor sounds like this:"]
    #What to do now?
    messages8 = ["Would you like to repeat, practice or continue to classify the sounds?",
                 "Did you get everything? Would you like to repeat, practice or classify the sounds?"]
    
    message1 = random.choice(messages1)
    message2 = random.choice(messages2)
    message3 = random.choice(messages3)
    message4 = random.choice(messages4)
    message5 = random.choice(messages5)
    message6 = random.choice(messages6)
    message7 = random.choice(messages7)
    message8 = random.choice(messages8)
    
    #playing the sounds
    Speak(message1)
    Speak(message2)
    Speak(message3)
    Play("underdense")
    Speak(message7)
    Play("short overdense")
    Speak(message4)
    Play("M")
    Speak(message6)
    Play("medium overdense")
    Speak(message5)
    Play("long overdense")
    Speak(message8)
    
    text = listen(r,mic)
    words = text.split()
    #options: R(repeat),P(practice) and C(continue)
    
    
    
    Panswer = "practice"
    Panswer2 = "exercise"
    P = check_words(Panswer,Panswer2,None,words)
    
    Ranswer = "repeat"
    Ranswer2 = "again"
    Ranswer3 = "time" #one more time
    R = check_words(Ranswer,Ranswer2,Ranswer3,words)
    
    Canswer = "continue"
    Canswer2 = "classify"
    C = check_words(Canswer,Canswer2,None,words)
    
    
    if P:
        goto = "practice"
    elif R:
        goto = "introduction"
    elif C:
        goto = "classify"
    else:
        Speak("You said: '{}'. I can't do anything with this answer.".format(text))
        goto = text
    return goto