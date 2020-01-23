import random
from functions import *
from functions_UI.ReadMessages import *

Messages = ReadFile_Messages("functions_UI\messages.txt")

def Practice(r,mic):
    goto = ""
    
    messages1 = Message_Tag(Messages,"practice12")
    messages2 = Message_Tag(Messages,"practice13")
    
    message1 = random.choice(messages1)
    message2 = random.choice(messages2)
    
    Speak(message1)
    Speak(message2)
    goto = Listen_level(r,mic)
    return goto

def Practice_level1(r,mic):
    #Underdense OR short overdense
    #VS Long overdense
    while True:
        Speak("Level 1")
        goto = ''
        list1 = ["underdense",
                 "short overdense"]
        soundA = random.choice(list1)
        
        list2 = [soundA,"long overdense"]
        playsound = random.choice(list2)

        con_break = Practice_general(list2,playsound,r,mic)
        if con_break == "continue":
            continue
        elif con_break == "break":
            break
        else:
            print(con_break)
    Speak(random.choice(Message_Tag(Messages,"practice8")))  
    goto = Listen_level(r,mic)
    return goto

def Practice_level2(r,mic):
    #M OR medium overdense
    #VS
    #Long overdense
    while True:
        Speak("Level 2")
        goto = ''
        list1 = ["M",
                 "medium overdense"]
        soundA = random.choice(list1)
        
        list2 = [soundA,"long overdense"]
        playsound = random.choice(list2)
        
        con_break = Practice_general(list2,playsound,r,mic)
        if con_break == "continue":
            continue
        elif con_break == "break":
            break
        else:
            print(con_break)
    Speak(random.choice(Message_Tag(Messages,"practice8")))  
    goto = Listen_level(r,mic)
    return goto

def Practice_level3(r,mic):
    #underdense OR short overdense
    #VS
    #M OR medium overdense
    while True:
        Speak("Level 3")
        goto = ''
        list1 = ["underdense",
                 "short overdense"]
        soundA = random.choice(list1)
        
        list3 = ["M",
                 "medium overdense"]
        soundB = random.choice(list3)
        
        list2 = [soundA,soundB]
        playsound = random.choice(list2)
        
        con_break = Practice_general(list2,playsound,r,mic)
        if con_break == "continue":
            continue
        elif con_break == "break":
            break
        else:
            print(con_break)
    Speak(random.choice(Message_Tag(Messages,"practice8")))  
    goto = Listen_level(r,mic)
    return goto

def Practice_level4(r,mic):
    #underdense OR short overdense
    #VS
    #M OR medium overdense
    #VS
    #long overdense
    while True:
        Speak("Level 4")
        goto = ''
        list1 = ["underdense",
                 "short overdense"]
        soundA = random.choice(list1)
        
        list3 = ["M",
                 "medium overdense"]
        soundB = random.choice(list3)
        soundC = "long overdense"
        
        list2 = [soundA,soundB,soundC]
        playsound = random.choice(list2)
        
        con_break = Practice_general(list2,playsound,r,mic)
        if con_break == "continue":
            continue
        elif con_break == "break":
            break
        else:
            print(con_break)
    Speak(random.choice(Message_Tag(Messages,"practice8")))  
    goto = Listen_level(r,mic)
    return goto

def Practice_level5(r,mic):
    #underdense
    #VS
    #short overdense
    while True:
        Speak("Level 5")
        goto = ''
        soundA = "underdense"
        soundB = "short overdense"
        
        list2 = [soundA,soundB]
        playsound = random.choice(list2)
        
        con_break = Practice_general(list2,playsound,r,mic)
        if con_break == "continue":
            continue
        elif con_break == "break":
            break
        else:
            print(con_break)
    Speak(random.choice(Message_Tag(Messages,"practice8")))  
    goto = Listen_level(r,mic)
    return goto

def Practice_level6(r,mic):
    #M
    #VS
    #medium overdense
    while True:
        Speak("Level 6")
        goto = ''
        soundA = "M"
        soundB = "medium overdense"
        
        list2 = [soundA,soundB]
        playsound = random.choice(list2)
        
        con_break = Practice_general(list2,playsound,r,mic)
        if con_break == "continue":
            continue
        elif con_break == "break":
            break
        else:
            print(con_break)
    Speak(random.choice(Message_Tag(Messages,"practice8")))  
    goto = Listen_level(r,mic)
    return goto

def Practice_level7(r,mic):
    #underdense AND short overdense
    #VS M OR medium overdense
    #VS long overdense
    while True:
        Speak("Level 7")
        goto = ''
        soundA = "M"
        soundB = "medium overdense"
        
        list1 = [soundA,soundB]
        list2 = ["underdense","short overdense",random.choice(list1),"long overdense"]
        playsound = random.choice(list2)
        
        con_break = Practice_general(list2,playsound,r,mic)
        if con_break == "continue":
            continue
        elif con_break == "break":
            break
        else:
            print(con_break)
    Speak(random.choice(Message_Tag(Messages,"practice8")))  
    goto = Listen_level(r,mic)
    return goto

def Practice_level8(r,mic):
    #all meteors
    while True:
        Speak("Level 8")
        goto = ''

        list2 = ["underdense","short overdense","M","medium overdense","long overdense"]
        playsound = random.choice(list2)
        
        con_break = Practice_general(list2,playsound,r,mic)
        if con_break == "continue":
            continue
        elif con_break == "break":
            break
        else:
            print(con_break)
    Speak(random.choice(Message_Tag(Messages,"practice8")))  
    goto = Listen_level(r,mic)
    return goto



