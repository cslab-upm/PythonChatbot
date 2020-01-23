import speech_recognition as sr
import time
from gtts import gTTS
from pygame import mixer
from mutagen.mp3 import MP3
import wave #wav files
import contextlib #wav files
import os #to delete files
import random
from functions_UI.ReadMessages import *

Messages = ReadFile_Messages("functions_UI\messages.txt")

def answerright(answer,list2,playsound):
    if answer in list2:
        if answer == playsound:
            return "correct"
        else:
            return "wrong"
    else:
        return "notpossible"

def Meteor2number(x):
    answer = ""
    if x == "underdense":
        answer = "1"
    elif x == "short overdense":
        answer = "2"
    elif x == "M":
        answer = "3"
    elif x == "medium overdense":
        answer = "4"
    elif x == "long overdense":
        answer = "5"
    return answer


def Setup():
    mixer.pre_init(frequency=24000)
    mixer.init()

def Get_volume():
    volume = mixer.music.get_volume()
    return volume
def Set_volume(x):
    mixer.music.set_volume(x)

def Get_duration(fname):
    if fname[-4:] == ".mp3":
        audio = MP3(fname)
        #print (audio.info.length)
        return audio.info.length
    elif fname[-4:] == ".wav":
        with contextlib.closing(wave.open(fname,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            #print (duration)
            return duration
    return None

#check 3 termen in words (oude functie)
def check_words(term,term2,term3,words):
    if term in words:
        return True
    elif term2 in words:
        return True
    elif term3 in words:
        return True
    return False

#check alle woorden uit de set met de woorden in de antwoorden
def check_words_set(answers,words):
    answer=False
    for word in words:
        if word in answers:
            answer=True
    return answer

def Listen_level(r,mic):
    goto = ""
    messages1 = Message_Tag(Messages,"function1")
    message1 = random.choice(messages1)
    Speak(message1)
    
    text = listen(r,mic)
    words = text.split()
    
    First = check_words_set(Message_Tag(Messages,"answer4"),words)
    Second = check_words_set(Message_Tag(Messages,"answer5"),words)
    Third = check_words_set(Message_Tag(Messages,"answer6"),words)
    Fourth = check_words_set(Message_Tag(Messages,"answer7"),words)
    Fifth = check_words_set(Message_Tag(Messages,"answer8"),words)
    Sixth = check_words_set(Message_Tag(Messages,"answer9"),words)
    Seventh = check_words_set(Message_Tag(Messages,"answer10"),words)
    Eighth = check_words_set(Message_Tag(Messages,"answer11"),words)
    Skip = check_words_set(Message_Tag(Messages,"answer12"),words)
    
    if First == True:
        goto = "practice_level1"
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
    elif Second == True:
        goto = "practice_level2" #because "to" is included, can be recognized when saying "go to level X"
    else:
        goto = "end"
    return goto

def Play(fname):
    if fname == "underdense":
        fname = "Sounds/meteor1_underdense.wav"
    elif fname == "short overdense":
        fname = "Sounds/meteor5_short overdense.wav"
    elif fname == "M":
        fname = "Sounds/meteor2_M.wav"
    elif fname == "medium overdense":
        fname = "Sounds/meteor4_medium overdense.wav"
    elif fname == "long overdense":
        fname = "Sounds/meteor3_long overdense.wav"
        
    duration = Get_duration(fname)
    song = wave.open(fname)
    freq = song.getframerate()
    mixer.init(frequency=freq) #play is .wav file is standard 44100
    #print(mixer.get_init())
    mixer.music.load(fname)
    mixer.music.play()
    time.sleep(duration)
    mixer.quit()
    
def Speak(sentence):
    language = "en"
    print("Debug: Before gTTS")
    myobj = gTTS(text=sentence, lang=language, slow=False)
    print("Debug: After gTTS")
    savename = "Sounds/speak.mp3"
    myobj.save(savename)
    duration = Get_duration(savename)
#     testing speed
#     https://stackoverflow.com/questions/2159365/pygame-audio-playback-speed
    mp3freq = MP3(savename).info.sample_rate
    mixer.init(mp3freq)
    mixer.music.load(savename)
    mixer.music.play()
    time.sleep(duration)
    time.sleep(0.1)
    mixer.music.stop()
    mixer.music.load("Sounds/dontremove.mp3") #(Dummy)otherwise I cannot remove the .mp3 files
    os.remove(savename)
    mixer.quit()
    
    
def Recognize_speech(r,mic):
    with mic as source:
        print("DEBUG: ambientnoise start")
        r.adjust_for_ambient_noise(source, duration = 0.6) # can be to long error
        print("DEBUG: ambientnoise end")
        Play("Sounds/Bleep.wav") #bleep sound
        print("speak now")
        audio = r.listen(source)
    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = r.recognize_google(audio)#, show_all=True
        print(response["transcription"])
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response

def listen(r,mic):
    for j in range(10): #give a range
        response = Recognize_speech(r,mic)
        if response["transcription"]:
            break
        if not response["success"]:
            break
        Speak("I didn't catch that. What did you say?\n")
    if response["error"]:
        Speak("Error: {}".format(response["error"]))
    print ("DEBUG...You said: '{}'".format(response["transcription"]))
    return response["transcription"]

def Practice_general(list2,playsound,r,mic):
    number3 = None
    number4 = None
    number5 = None
    listlength = len(list2)
    number1 = Meteor2number(list2[0])
    number2 = Meteor2number(list2[1])
    if listlength > 2:
        number3 = Meteor2number(list2[2])
    if listlength > 3:
        number4 = Meteor2number(list2[3])
    if listlength > 4:
        number4 = Meteor2number(list2[4])
        
        
    answernumber = Meteor2number(playsound)
    
    if listlength == 2:
        message1 = random.choice(Message_Tag(Messages,"practice1"))
        message1 = message1.format(list2[0],number1,list2[1],number2)
    elif listlength == 3:
        message1 = random.choice(Message_Tag(Messages,"practice9"))
        message1 = message1.format(list2[0],number1,list2[1],number2,list2[2],number3)
    elif listlength == 4:
        message1 = random.choice(Message_Tag(Messages,"practice10"))
        message1 = message1.format(list2[0],number1,list2[1],number2,list2[2],number3,list2[3],number4)
    elif listlength == 5:
        message1 = random.choice(Message_Tag(Messages,"practice11"))
        message1 = message1.format(list2[0],number1,list2[1],number2,list2[2],number3,list2[3],number4,list2[4],number5)
        
    while True:
        Speak(message1)
        Play(playsound)
        text = listen(r,mic)
        print("You said: '{}'".format(text))
        words = text.split()
        
        First = check_words_set(Message_Tag(Messages,"answer4"),words)
        Second = check_words_set(Message_Tag(Messages,"answer5"),words)
        Third = check_words_set(Message_Tag(Messages,"answer6"),words)
        Fourth = check_words_set(Message_Tag(Messages,"answer7"),words)
        Fifth = check_words_set(Message_Tag(Messages,"answer8"),words)
        Repeat = check_words_set(Message_Tag(Messages,"answer16"),words)
        answer = None
        
        if First:
            print("You chose underdense")
            answer = "underdense"
            k = answerright(answer,list2,playsound)
            if k == "notpossible":
                Speak(random.choice(Message_Tag(Messages,"practice2")))
                continue
        elif Second:
            print("you chose short overdense")
            answer = "short overdense"
            k = answerright(answer,list2,playsound)
            if k == "notpossible":
                Speak(random.choice(Message_Tag(Messages,"practice2")))
                continue
        elif Third:
            print("you chose M")
            answer = "M"
            k = answerright(answer,list2,playsound)
            if k == "notpossible":
                Speak(random.choice(Message_Tag(Messages,"practice2")))
                continue
        elif Fourth:
            print("you chose medium overdense")
            answer = "medium overdense"
            k = answerright(answer,list2,playsound)
            if k == "notpossible":
                Speak(random.choice(Message_Tag(Messages,"practice2")))
                continue
        elif Fifth:
            print("you chose long overdense")
            answer = "long overdense"
            k = answerright(answer,list2,playsound)
            if k == "notpossible":
                Speak(random.choice(Message_Tag(Messages,"practice2")))
                continue
        elif Repeat:
            print("Debug: Repeating...")
            continue
        else:
            Speak(random.choice(Message_Tag(Messages,"practice3")))
            continue
        break
    if k == "correct":
        Speak(random.choice(Message_Tag(Messages,"practice4")))
        return "break"
    elif k == "wrong":
        if listlength == 2:
            print("Explanation here:")
            msg1 = random.choice(Message_Tag(Messages,"practice5"))
            Speak(msg1.format(answer,Meteor2number(answer)))
            Play(answer)
            msg2 = random.choice(Message_Tag(Messages,"practice6"))
            Speak(msg2.format(playsound,answernumber))
            Play(playsound)
            Speak(random.choice(Message_Tag(Messages,"practice7")))
            return "continue"
        elif listlength > 2:
            list2.remove(answer)
            return Practice_general(list2,playsound,r,mic)
    else:
        return "thiscannothappen"