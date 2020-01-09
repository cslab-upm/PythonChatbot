import speech_recognition as sr
from functions_UI.introduction import *
from functions import *

#standard answers:
#dont understand,
#repeat
#help me
#options

#Get response after 3 or 4 seconds.


#connect with the API, application programming interface
#Get sound

i = 0
j = 0
#sr.__version__

r = sr.Recognizer()
#r.pause_threshold = 1.0
#r.phrase_threshold = 1.0
#r.non_speaking_duration = 1.0
mic = sr.Microphone()

def Help(FunctionCalled):
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

def Welcome(r,mic,step):
    goto = ""
    while True:
        start = True
        messages = ['Welcome to the program for classifying meteor sounds',
                    'Program has started',
                    'I like that you started the program']
        firstmessage1 = random.choice(messages)
        
        bleepmessages = ['If you hear this sound:',
                         "when you hear this sound"]
        bleepmessage1 = random.choice(bleepmessages)
        
        bleepmessages = ['you can speak',
                         'I expect you to say something']
        bleepmessage2 = random.choice(bleepmessages)
        
        optionmenumessages = ['Would you like to get an introduction or would you like to do some practice?', #intro, practice or classify
                              'Do you want to learn the sounds with the introduction or with some practice?',
                              'Would you like to hear the sound examples or do a little bit of pactice?']
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
        Tanswer = "introduction"
        Tanswer2 = "examples"
        #Tanswer3 = "yes"
        T = check_words(Tanswer,Tanswer2,None,words)
        
        Fanswer = "no"
        Fanswer2 = "thank"
        Fanswer3 = "thanks"
        F = check_words(Fanswer,Fanswer2,Fanswer3,words)
        
        Panswer = "practice"
        Panswer2 = "exercise"
        Panswer3 = "breakfast" #sounds like practice apparently
        P = check_words(Panswer,Panswer2,Panswer3,words)
        #dont understand,
        #repeat
        #help me
        #options
        Hanswer1 = "repeat"
        Hanswer2 = "help"
        Hanswer3_1 = "option"
        Hanswer3_2 = "options"
        Hanswer4 = "menu"
        H1 = check_words(Hanswer1,None,None,words)
        H2 = check_words(Hanswer2,None,None,words)
        H3 = check_words(Hanswer3_1,Hanswer3_2,None,words)
        H4 = check_words(Hanswer4,None,None,words)
        
        
        
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
            print("debug, this is not possible")
    return goto

def Classify_sounds():
    #print should be voice
    message = "We are now in function classify sounds. Let's start."
    Speak(message)
    #print("We are in function classify sounds")
    return "end" #have to be changed

def Practice():
    goto = ""
    messages1 = ["We are now in practice",
                 "Now we are going to practice"]
    message1 = random.choice(messages1)
    
    messages2 = ["There are 8 levels of practice.",
                 "You have the option of 8 different levels."]
    message2 = random.choice(messages2)
    
    Speak(message1)
    Speak(message2)
    goto = Listen_level()
    return goto

def Listen_level():
    goto = ""
    messages1 = ["Which level do you want to do?",
                 "Which level shall we do?"]
    message1 = random.choice(messages1)
    Speak(message1)
    
    text = listen(r,mic)
    words = text.split()
    print(text)
    
    First = check_words("one","first","1",words)
    Second = check_words("two","second","2",words) #add "to" and "too" and...? "through"
    Third = check_words("three","third","3",words) #add "tree"
    Fourth = check_words("four","fourth","4",words)
    Fifth = check_words("five","fifth","5",words)
    Sixth = check_words("six","sixth","6",words)
    Seventh = check_words("seven","seventh","7",words)
    Eighth = check_words("eigth","eighth","8",words)
    Skip = check_words("quit","skip","stop",words)
    
    if First == True:
        goto = "practice_level1"
    elif Second == True:
        goto = "practice_level2"
    elif Third == True:
        goto = "practice_level3"
    elif Fourth == True:
        goto = "practice_level4"
    elif Fifth == True:
        goto = "practice_level5"
    elif Sixth == True:
        goto = "practice_level6"
    elif Seventh == True:
        goto = "practice_level7"
    elif Eighth == True:
        goto = "practice_level8"
    elif Skip == True:
        goto = "classify"
    else:
        goto = "end"
    return goto

def Practice_level1():
    #Underdense OR short overdense
    #VS
    #Long overdense
    while True:
        Speak("Level 1")
        
        goto = ''
        #first choose underdense/ short overdense
        list1 = ["underdense",
                 "short overdense"]
        soundA = random.choice(list1)
        
        list2 = [soundA,"long overdense"]
        playsound = random.choice(list2)
        
        number1 = Meteor2number(list2[0])
        number2 = Meteor2number(list2[1])
        answernumber = Meteor2number(playsound)
        
        message = "After you hear the sound, you can choose between the {} meteor, you should call this number {}... and the {} meteor, you should call this number {}".format(list2[0],number1,list2[1],number2) #Error to fast
        while True:
            Speak(message)
            Play(playsound)
            text = listen(r,mic)
            print("You said: '{}'".format(text))
            words = text.split()
            First = check_words("1","one","first",words)
            Second = check_words("2","two","second",words)
            Third = check_words("3","three","third",words)
            Fourth = check_words("4","four","fourth",words)
            Fifth = check_words("5","five","fifth",words)
            Repeat = check_words("again","repeat","over",words)
            answer = None
            
            if First:
                print("You chose underdense")
                answer = "underdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Second:
                print("you chose short overdense")
                answer = "short overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Third:
                print("you chose M")
                answer = "M"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fourth:
                print("you chose medium overdense")
                answer = "medium overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fifth:
                print("you chose long overdense")
                answer = "long overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Repeat:
                print("Let's repeat, fix that he repeats it.")
                continue
            else:
                print("I didn't understand, try again.")
                continue #need another loop where only the answer will be listened, this is fine tho.
            break
        if k == "correct":
            Speak("Your answer is correct")
            break
        elif k == "wrong":
            print("Explanation here:")
            Speak("You chose {} meteor, which is number {}. That sound like this:..".format(answer,Meteor2number(answer)))
            Play(answer)
            Speak("The correct answer was {} meteor, which is number {}. That sounds like this:..".format(playsound,answernumber))
            Play(playsound)
            Speak("Try another time")
            continue
    Speak("Let's continue")
                  
    goto = Listen_level()
    return goto
def Practice_level2():
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
        
        number1 = Meteor2number(list2[0])
        number2 = Meteor2number(list2[1])
        answernumber = Meteor2number(playsound)
        
        message = "After you hear the sound, you can choose between the {} meteor, you should call this number {}... and the {} meteor, you should call this number {}".format(list2[0],number1,list2[1],number2) #Error to fast
        while True:
            Speak(message)
            Play(playsound)
            text = listen(r,mic)
            print("You said: '{}'".format(text))
            words = text.split()
            First = check_words("1","one","first",words)
            Second = check_words("2","two","second",words)
            Third = check_words("3","three","third",words)
            Fourth = check_words("4","four","fourth",words)
            Fifth = check_words("5","five","fifth",words)
            Repeat = check_words("again","repeat","over",words)
            answer = None
            
            if First:
                print("You chose underdense")
                answer = "underdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Second:
                print("you chose short overdense")
                answer = "short overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Third:
                print("you chose M")
                answer = "M"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fourth:
                print("you chose medium overdense")
                answer = "medium overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fifth:
                print("you chose long overdense")
                answer = "long overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Repeat:
                print("Let's repeat, fix that he repeats it.")
                continue
            else:
                print("I didn't understand, try again.")
                continue #need another loop where only the answer will be listened, this is fine tho.
            break
        if k == "correct":
            Speak("Your answer is correct")
            break
        elif k == "wrong":
            print("Explanation here:")
            Speak("You chose {} meteor, which is number {}. That sound like this:..".format(answer,Meteor2number(answer)))
            Play(answer)
            Speak("The correct answer was {} meteor, which is number {}. That sounds like this:..".format(playsound,answernumber))
            Play(playsound)
            Speak("Try another time")
            continue
    Speak("Let's continue")
                  
    goto = Listen_level()
    return goto
def Practice_level3():
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
        
        number1 = Meteor2number(list2[0])
        number2 = Meteor2number(list2[1])
        answernumber = Meteor2number(playsound)
        
        message = "After you hear the sound, you can choose between the {} meteor, you should call this number {}... and the {} meteor, you should call this number {}".format(list2[0],number1,list2[1],number2) #Error to fast
        while True:
            Speak(message)
            Play(playsound)
            text = listen(r,mic)
            print("You said: '{}'".format(text))
            words = text.split()
            First = check_words("1","one","first",words)
            Second = check_words("2","two","second",words)
            Third = check_words("3","three","third",words)
            Fourth = check_words("4","four","fourth",words)
            Fifth = check_words("5","five","fifth",words)
            Repeat = check_words("again","repeat","over",words)
            answer = None
            
            if First:
                print("You chose underdense")
                answer = "underdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Second:
                print("you chose short overdense")
                answer = "short overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Third:
                print("you chose M")
                answer = "M"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fourth:
                print("you chose medium overdense")
                answer = "medium overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fifth:
                print("you chose long overdense")
                answer = "long overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Repeat:
                print("Let's repeat, fix that he repeats it.")
                continue
            else:
                print("I didn't understand, try again.")
                continue #need another loop where only the answer will be listened, this is fine tho.
            break
        if k == "correct":
            Speak("Your answer is correct")
            break
        elif k == "wrong":
            print("Explanation here:")
            Speak("You chose {} meteor, which is number {}. That sound like this:..".format(answer,Meteor2number(answer)))
            Play(answer)
            Speak("The correct answer was {} meteor, which is number {}. That sounds like this:..".format(playsound,answernumber))
            Play(playsound)
            Speak("Try another time")
            continue
    Speak("Let's continue")
                  
    goto = Listen_level()
    return goto
def Practice_level4():
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
        
        number1 = Meteor2number(list2[0])
        number2 = Meteor2number(list2[1])
        number3 = Meteor2number(list2[2])
        answernumber = Meteor2number(playsound)
        
        message = "After you hear the sound, you can choose between the {} meteor, you should call this number {}... the {} meteor, you should call this number {}... and the {} meteor, you should call this number {}.".format(list2[0],number1,list2[1],number2,list2[2],number3)
        while True:
            Speak(message)
            Play(playsound)
            text = listen(r,mic)
            print("You said: '{}'".format(text))
            words = text.split()
            First = check_words("1","one","first",words)
            Second = check_words("2","two","second",words)
            Third = check_words("3","three","third",words)
            Fourth = check_words("4","four","fourth",words)
            Fifth = check_words("5","five","fifth",words)
            Repeat = check_words("again","repeat","over",words)
            answer = None
            
            if First:
                print("You chose underdense")
                answer = "underdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Second:
                print("you chose short overdense")
                answer = "short overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Third:
                print("you chose M")
                answer = "M"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fourth:
                print("you chose medium overdense")
                answer = "medium overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fifth:
                print("you chose long overdense")
                answer = "long overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Repeat:
                print("Let's repeat, fix that he repeats it.")
                continue
            else:
                print("I didn't understand, try again.")
                continue #need another loop where only the answer will be listened, this is fine tho.
            break
        if k == "correct":
            Speak("Your answer is correct")
            break
        elif k == "wrong":
            Speak("Your answer was wrong")
            list2.remove(answer)
            number1 = Meteor2number(list2[0])
            number2 = Meteor2number(list2[1])
            message = "After you hear the sound, you can choose between the {} meteor, you should call this number {}... and the {} meteor, you should call this number {}".format(list2[0],number1,list2[1],number2)
            while True:
                Speak(message)
                Play(playsound)
                text = listen(r,mic)
                print("You said: '{}'".format(text))
                words = text.split()
                First = check_words("1","one","first",words)
                Second = check_words("2","two","second",words)
                Third = check_words("3","three","third",words)
                Fourth = check_words("4","four","fourth",words)
                Fifth = check_words("5","five","fifth",words)
                Repeat = check_words("again","repeat","over",words)
                answer = None
                
                if First:
                    print("You chose underdense")
                    answer = "underdense"
                    k = answerright(answer,list2,playsound)
                    if k == "notpossible":
                        Speak("That was not a possible answer, try again")
                        continue
                elif Second:
                    print("you chose short overdense")
                    answer = "short overdense"
                    k = answerright(answer,list2,playsound)
                    if k == "notpossible":
                        Speak("That was not a possible answer, try again")
                        continue
                elif Third:
                    print("you chose M")
                    answer = "M"
                    k = answerright(answer,list2,playsound)
                    if k == "notpossible":
                        Speak("That was not a possible answer, try again")
                        continue
                elif Fourth:
                    print("you chose medium overdense")
                    answer = "medium overdense"
                    k = answerright(answer,list2,playsound)
                    if k == "notpossible":
                        Speak("That was not a possible answer, try again")
                        continue
                elif Fifth:
                    print("you chose long overdense")
                    answer = "long overdense"
                    k = answerright(answer,list2,playsound)
                    if k == "notpossible":
                        Speak("That was not a possible answer, try again")
                        continue
                elif Repeat:
                    print("Let's repeat, fix that he repeats it.")
                    continue
                else:
                    print("I didn't understand, try again.")
                    continue #need another loop where only the answer will be listened, this is fine tho.
                break
            if k == "correct":
                Speak("Your answer is correct")
                break
            elif k == "wrong":
                print("Explanation here:")
                Speak("You chose {} meteor, which is number {}. That sound like this:..".format(answer,Meteor2number(answer)))
                Play(answer)
                Speak("The correct answer was {} meteor, which is number {}. That sounds like this:..".format(playsound,answernumber))
                Play(playsound)
                Speak("Try another time")
                continue
    Speak("Let's continue")
    goto = Listen_level()
    return goto
def Practice_level5():
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
        
        number1 = Meteor2number(list2[0])
        number2 = Meteor2number(list2[1])
        answernumber = Meteor2number(playsound)
        
        message = "After you hear the sound, you can choose between the {} meteor, you should call this number {}... and the {} meteor, you should call this number {}".format(list2[0],number1,list2[1],number2) #Error to fast
        while True:
            Speak(message)
            Play(playsound)
            text = listen(r,mic)
            print("You said: '{}'".format(text))
            words = text.split()
            First = check_words("1","one","first",words)
            Second = check_words("2","two","second",words)
            Third = check_words("3","three","third",words)
            Fourth = check_words("4","four","fourth",words)
            Fifth = check_words("5","five","fifth",words)
            Repeat = check_words("again","repeat","over",words)
            answer = None
            
            if First:
                print("You chose underdense")
                answer = "underdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Second:
                print("you chose short overdense")
                answer = "short overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Third:
                print("you chose M")
                answer = "M"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fourth:
                print("you chose medium overdense")
                answer = "medium overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fifth:
                print("you chose long overdense")
                answer = "long overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Repeat:
                print("Let's repeat, fix that he repeats it.")
                continue
            else:
                print("I didn't understand, try again.")
                continue #need another loop where only the answer will be listened, this is fine tho.
            break
        if k == "correct":
            Speak("Your answer is correct")
            break
        elif k == "wrong":
            print("Explanation here:")
            Speak("You chose {} meteor, which is number {}. That sound like this:..".format(answer,Meteor2number(answer)))
            Play(answer)
            Speak("The correct answer was {} meteor, which is number {}. That sounds like this:..".format(playsound,answernumber))
            Play(playsound)
            Speak("Try another time")
            continue
    Speak("Let's continue")
                  
    goto = Listen_level()
    return goto
def Practice_level6():
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
        
        number1 = Meteor2number(list2[0])
        number2 = Meteor2number(list2[1])
        answernumber = Meteor2number(playsound)
        
        message = "After you hear the sound, you can choose between the {} meteor, you should call this number {}... and the {} meteor, you should call this number {}".format(list2[0],number1,list2[1],number2) #Error to fast
        while True:
            Speak(message)
            Play(playsound)
            text = listen(r,mic)
            print("You said: '{}'".format(text))
            words = text.split()
            First = check_words("1","one","first",words)
            Second = check_words("2","two","second",words)
            Third = check_words("3","three","third",words)
            Fourth = check_words("4","four","fourth",words)
            Fifth = check_words("5","five","fifth",words)
            Repeat = check_words("again","repeat","over",words)
            answer = None
            
            if First:
                print("You chose underdense")
                answer = "underdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Second:
                print("you chose short overdense")
                answer = "short overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Third:
                print("you chose M")
                answer = "M"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fourth:
                print("you chose medium overdense")
                answer = "medium overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Fifth:
                print("you chose long overdense")
                answer = "long overdense"
                k = answerright(answer,list2,playsound)
                if k == "notpossible":
                    Speak("That was not a possible answer, try again")
                    continue
            elif Repeat:
                print("Let's repeat, fix that he repeats it.")
                continue
            else:
                print("I didn't understand, try again.")
                continue #need another loop where only the answer will be listened, this is fine tho.
            break
        if k == "correct":
            Speak("Your answer is correct")
            break
        elif k == "wrong":
            print("Explanation here:")
            Speak("You chose {} meteor, which is number {}. That sound like this:..".format(answer,Meteor2number(answer)))
            Play(answer)
            Speak("The correct answer was {} meteor, which is number {}. That sounds like this:..".format(playsound,answernumber))
            Play(playsound)
            Speak("Try another time")
            continue
    Speak("Let's continue")
                  
    goto = Listen_level()
    return goto
def Practice_level7():
    goto = "end"
    return goto
def Practice_level8():
    goto = "end"
    return goto

# Here you can see that, mixer.init() is fine to use. Mixer.quit() resets all the preset functions
# print("test")
# mixer.init(44100)
# Set_volume(0.2)
# Speak("This is really soft")
# #mixer.quit() #(un)comment this one
# mixer.init(44100)
# Speak("This is really soft too")
# print("end of test")

if __name__ == "__main__":
    Setup()
    goto = Welcome(r,mic,1)
    running = True
    while running is True:
        if goto == "welcome":
            goto = Welcome(r,mic,2)
        elif goto == "classify":
            goto = Classify_sounds()
        elif goto == "introduction":
            goto = Introduction(r,mic)
        elif goto == "practice":
            goto = Practice()
        elif goto == "practice_level1":
            goto = Practice_level1()
        elif goto == "practice_level2":
            goto = Practice_level2()
        elif goto == "practice_level3":
            goto = Practice_level3()
        elif goto == "practice_level4":
            goto = Practice_level4()
        elif goto == "practice_level5":
            goto = Practice_level5()
        elif goto == "practice_level6":
            goto = Practice_level6()
        elif goto == "practice_level7":
            goto = Practice_level7()
        elif goto == "practice_level8":
            goto = Practice_level8()
        elif goto == "end":
            Speak("Program will close")
            running = False
        else:
            print("something went wrong")
            break
            
    print("\nThis is a debugging message.\ngoto = " + goto)
