import random
from functions import *
from functions_UI.ReadMessages import *

Messages = ReadFile_Messages("functions_UI\messages.txt")



def Help(r,mic,FunctionCalled):
    messages = ['You are now in the help menu.',
                "I'll help you now!",
                "What can I do for you?"]
    m1 = random.choice(messages)
    messages = ["What do you want? You can change the volume or the speed.",
                "Would you like to change the volume or would you like to change the speed?"]
    m2 = random.choice(messages)
    Speak(m1)
    Speak(m2)
    text = listen(r,mic)
    words = text.split()
    v1 = "volume"
    v2 = "harder"
    v3 = "softer"
    V = check_words(v1,v2,v3,words)
    s1 = "speed"
    s2 = "faster"
    s3 = "slower"
    S = check_words(s1,s2,s3,words)
    f1 = "neither"
    f2 = "none"
    f3 = "else"
    F = check_words(f1,f2,f3,words)
    exit1 = None
    if V:
        while True:
            harder = check_words(v2,None,None,words)
            softer = check_words(v3,None,None,words)
            if harder:
                vol = Get_volume() #between 0 and 1
                Rvol = vol * 100
                Svol = str(Rvol)
                text = str("Your volume right now is: " + Svol[0:2])
                Speak(text)
                Set_volume(vol + 0.2)
                vol = Get_volume()
                Rvol = vol * 100
                Svol = str(Rvol)
                text = str("Your volume right now is: " + Svol[0:2])
                Speak(text)
                text = ("Is this oke? Or do you want me to turn up the volume?")
                Speak(text)
                text = listen(r,mic)
                words2 = text.split()
                Repeat = check_words("harder","more","up",words2)
                Repeat2 = check_words("louder","hard","higher",words2)
                Exit = check_words("ok","oke","fine",words2)
                if Repeat:
                    continue
                elif Repeat2:
                    continue
                elif Exit:
                    break
            elif softer:
                vol = Get_volume()
                Rvol = vol * 100
                Svol = str(Rvol)
                text = str("Your volume right now is: " + Svol[0:2])
                Speak(text)
                Set_volume(vol - 0.2)
                vol = Get_volume()
                Rvol = vol * 100
                Svol = str(Rvol)
                text = str("Your volume right now is: " + Svol[0:2])
                Speak(text)
                text = ("Is this oke? or do you want me to lower the volume?")
                Speak(text)
                text = listen(r,mic)
                words2 = text.split()
                Repeat = check_words("softer","more","down",words2)
                Exit = check_words("ok","oke","fine",words2)
                if Repeat:
                    continue
                elif Exit:
                    break
            elif exit1:
                break
            else:
                text = ("Do you want it harder or softer?")
                Speak(text)
                text = listen(r,mic)
                words = text.split()
                exit1 = check_words("exit",None,None,words)
    return FunctionCalled