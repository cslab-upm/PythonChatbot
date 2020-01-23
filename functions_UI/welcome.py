import random
from functions import *
from functions_UI.ReadMessages import *

Messages = ReadFile_Messages("functions_UI\messages.txt")
Debug = False

def Welcome(r,mic,step):
    if Debug == True:
        goto = "classify"
        #goto = "introduction"
        return goto
    goto = ""
    while True:
        start = True
        
        messages = Message_Tag(Messages,"welcome1")     
        bleepmessages1 = Message_Tag(Messages,"welcome2")
        bleepmessages2 = Message_Tag(Messages,"welcome3")
        optionmenumessages = Message_Tag(Messages,"welcome4")
        firstmessage1 = random.choice(messages)
        bleepmessage1 = random.choice(bleepmessages1)
        bleepmessage2 = random.choice(bleepmessages2)
        optionmenumessage = random.choice(optionmenumessages)
        
        if step == 1:
            Speak(firstmessage1)
            if start == True:
                Speak(bleepmessage1)
                Play("Sounds/Bleep.wav")
                Speak(bleepmessage2)
            step = 2
        if step == 2:
            Speak(optionmenumessage)
        
        ## new way:
        text = listen(r,mic)
        words = text.split()
        T = check_words_set(Message_Tag(Messages,"answer13"),words)
        F = check_words_set(Message_Tag(Messages,"answer14"),words)
        P = check_words_set(Message_Tag(Messages,"answer15"),words)
        
        #dont understand,
        #repeat
        #help me
        #options
        H1 = check_words_set(Message_Tag(Messages,"answer16"),words)
        H2 = check_words_set(Message_Tag(Messages,"answer17"),words)
        H3 = check_words_set(Message_Tag(Messages,"answer18"),words)
        H4 = check_words_set(Message_Tag(Messages,"answer19"),words)

        if T:
            goto = "introduction"
            print("DEBUG...In WELCOME: goto = introduction")
            break
        elif F:
            goto = "classify"
            print("DEBUG...In WELCOME: goto = classify")
            break
        elif P:
            goto = "practice"
            print("DEBUG...In WELCOME: goto = practice")
            break
        elif H1:
            step = 2
            print("DEBUG...In WELCOME: step = 2")
            continue
        elif H2:
            goto = Help("welcome")
            print("DEBUG...In WELCOME: goto = Welcome")
            break
        else:
            goto = "end"
            message = random.choice(Message_Tag(Messages,"debug1"))
            print(message.format(text))
    return goto