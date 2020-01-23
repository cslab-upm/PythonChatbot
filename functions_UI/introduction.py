import random
from functions import *

def Introduction(r,mic):
    messages1 = Message_Tag(Messages,"intro1")
    messages2 = Message_Tag(Messages,"intro2")
    #FIRST SOUND
    messages3 = Message_Tag(Messages,"intro3")
    #SECOND SOUND
    messages4 = Message_Tag(Messages,"intro4")
    #THIRD SOUND
    messages5 = Message_Tag(Messages,"intro5")
    #FOURTH SOUND
    messages6 = Message_Tag(Messages,"intro6")
    #FIFTH SOUND
    messages7 = Message_Tag(Messages,"intro7")
    #What to do now?
    messages8 = Message_Tag(Messages,"intro8")
    
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
    Speak(message4)
    Play("short overdense")
    Speak(message5)
    Play("M")
    Speak(message6)
    Play("medium overdense")
    Speak(message7)
    Play("long overdense")
    Speak(message8)
    
    text = listen(r,mic)
    words = text.split()
    #options: R(repeat),P(practice) and C(continue)
        
    Panswers = Message_Tag(Messages,"answer1")
    P = check_words_set(Panswers,words)
    
    Ranswers = Message_Tag(Messages,"answer2")
    R = check_words_set(Ranswers,words)
    
    Canswers = Message_Tag(Messages,"answer3")
    C = check_words_set(Canswers,words)
    
    
    if P:
        goto = "practice"
    elif R:
        goto = "introduction"
    elif C:
        goto = "classify"
    else:
        messages9 = Message_Tag(Messages,"debug1")
        message9 = random.choice(messages9)
        Speak(message9.format(text))
        goto = text
    return goto