import random
from functions import *
from functions_UI.ReadMessages import *

Messages = ReadFile_Messages("functions_UI\messages.txt")

Debug = False

def Classify_sounds(r,mic):
    goto = ""
    secondtime = False
    messages1 = Message_Tag(Messages,"class1")
    messages2 = Message_Tag(Messages,"class2")
    messages3 = Message_Tag(Messages,"class3")
    messages4 = Message_Tag(Messages,"class4")
    messages5 = Message_Tag(Messages,"class5")
    messages6 = Message_Tag(Messages,"class6")
    messages7 = Message_Tag(Messages,"class7")
    messages8 = Message_Tag(Messages,"class8")
    messages9 = Message_Tag(Messages,"class9")
    
    while True:
        message1 = random.choice(messages1)
        message2 = random.choice(messages2)
        message3 = random.choice(messages3)
        message4 = random.choice(messages4)
        message5 = random.choice(messages5)
        message6 = random.choice(messages6)
        message7 = random.choice(messages7)
        message8 = random.choice(messages8)
        message9 = random.choice(messages8)
        if Debug == True:
            Y = True
        else:
            if secondtime == True:
                Y = True
            else:
                Speak(message1)
                Speak(message2)
                Speak(message3)
                
                text = listen(r,mic)
                print("You said: '{}'".format(text))
                words = text.split()
                
                #[Y]es , [R]epeat, [N]o / abort
                Y = check_words_set(Message_Tag(Messages,"answer22"),words)
                R = check_words_set(Message_Tag(Messages,"answer16"),words)
                N = check_words_set(Message_Tag(Messages,"answer23"),words)
            
        if Y:
            sound = random.choice(Message_Tag(Messages,"allsounds"))
            soundpath = "Sounds/Classifysounds/" + sound
            while True:
                if Debug != True:
                    Speak(message5)
                    Play(soundpath)
                
                text = listen(r,mic)
                words = text.split()
                
                First = check_words_set(Message_Tag(Messages,"answer4"),words)
                Second = check_words_set(Message_Tag(Messages,"answer5"),words)
                Third = check_words_set(Message_Tag(Messages,"answer6"),words)
                Fourth = check_words_set(Message_Tag(Messages,"answer7"),words)
                Fifth = check_words_set(Message_Tag(Messages,"answer8"),words)
                Repeat = check_words_set(Message_Tag(Messages,"answer16"),words)
                Other = check_words_set(Message_Tag(Messages,"answer20"),words)
                Dontknow = check_words_set(Message_Tag(Messages,"answer21"),words)
                answer = None
                if First:
                    Speak(message4.format("one","underdense"))
                    answer = 1
                elif Third:
                    Speak(message4.format("three","M"))
                    answer = 3
                elif Fourth:
                    Speak(message4.format("four","medium overdense"))
                    answer = 4
                elif Fifth:
                    Speak(message4.format("five","long overdense"))
                    answer = 5
                elif Other:
                    Speak(message7)
                    answer = 6
                elif Dontknow:
                    Speak(message8)
                    break
                elif Repeat:
                    continue
                elif Second:
                    Speak(message4.format("two","short overdense"))
                    answer = 2
                else:
                    Speak(message9)
                    continue
                text = listen(r,mic)
                words = text.split()
                Y = check_words_set(Message_Tag(Messages,"answer24"),words)
                N = check_words_set(Message_Tag(Messages,"answer23"),words)
                if Y:
                    result_list = Read_results("functions_UI\solutions.txt")
                    if result_list == []:
                        result_list = Reset_results()
                    Add_result(sound,answer,result_list)
                    Write_results(result_list,"functions_UI\solutions.txt")
                    print("Debug: result added")
                    break
                if N:
                    continue
            Speak(message6)
            text = listen(r,mic)
            words = text.split()
            Y = check_words_set(Message_Tag(Messages,"answer25"),words)
            N = check_words_set(Message_Tag(Messages,"answer23"),words)
            if Y:
                secondtime = True
                continue
            if N:
                break
        elif R:
            continue
        elif N:
            break
        goto = "welcome"
    return goto
