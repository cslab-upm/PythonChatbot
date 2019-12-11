import time
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
from mutagen.mp3 import MP3
import random
import wave #wav files
import contextlib #wav files
import os #to delete files

#standard answers:
#dont understand,
#repeat
#connect with the API, application programming interface
#Get sound
#Noelia, upload the code.

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
#import os
language = "en"
i = 0
j = 0
#sr.__version__
r = sr.Recognizer()
#audio files
#r.recognize_google()

#mic recog
mic = sr.Microphone()

def check_words(term,term2,term3,words):
    if term in words:
        return True
    elif term2 in words:
        return True
    elif term3 in words:
        return True
    return False

def Play(fname):
    duration = Get_duration(fname)
    mixer.init()
    mixer.music.load(fname)
    mixer.music.play()
    time.sleep(duration)

def Speak(sentence):
    global language
    global i
    global j
    myobj = gTTS(text=sentence, lang=language, slow=False)
#   notusefull anymore    
#     if i == j:
#         j+=1
#    savename = sentence[:3] + str(j) + ".mp3"
    savename = "speak.mp3"
    myobj.save(savename)
    duration = Get_duration(savename)
#     testing speed
#     https://stackoverflow.com/questions/2159365/pygame-audio-playback-speed
    mp3freq = MP3(savename).info.sample_rate
    mixer.init(frequency=mp3freq)
    mixer.music.load(savename)
    mixer.music.play()

    i+=1
    time.sleep(duration)
    time.sleep(0.1)
    mixer.music.stop()
    mixer.music.load("dontremove.mp3") #(Dummy)otherwise I cannot remove the .mp3 files
    mixer.quit()
    os.remove(savename)
    
    
def Recognize_speech(r,mic):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("speak now")
        Play("Bleep.wav") #bleep sound
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
        #print(response["transcription"])
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response

def listen():
    for j in range(10): #give a range??
        response = Recognize_speech(r,mic)
        if response["transcription"]:
            break
        if not response["success"]:
            break
        Speak("I didn't catch that. What did you say?\n")
    if response["error"]:
        Speak("Error: {}".format(response["error"]))
    return response["transcription"]

def Welcome(r,mic):
    messages = ['Welcome to the program for classifying meteor sounds',
                'Program has started',
                'I like that you started the program']
    firstmessage1 = random.choice(messages)
    Speak(firstmessage1)
    #print(firstmessage)
    optionmenumessages = ['Would you like to get an introduction?', #yes no
                          'Do you want to learn the sounds?',
                          'Would you like to hear the sound examples?']
    optionmenumessage = random.choice(optionmenumessages)
    Speak(optionmenumessage)
    #print(optionmenumessage)

    ## new way:
    text = listen()
    words = text.split()
    Tanswer = "yes"
    Tanswer2 = "please"
    T = check_words(Tanswer,Tanswer2,None,words)
    
    Fanswer = "no"
    Fanswer2 = "thank"
    Fanswer3 = "thanks"
    F = check_words(Fanswer,Fanswer2,Fanswer3,words)
    
    if T == True:
        goto = "introduction"
    elif F == True:
        goto = "classify"
    else:
        print("debug, this is not possible")
    return goto
    
    ## old way:
#     if response["transcription"] == "yes": #"response["transcription"]" now is [text]
#         goto = "introduction"
#     elif response["transcription"] == "no":
#         goto = "classify" #or else...
#     else:
#         Speak("You said: '{}'. I can't do anything with this answer.".format(response["transcription"]))
#         goto = response["transcription"]
#     return goto

def Classify_sounds():
    #print should be voice
    message = "We are now in function classify sounds. Let's start."
    Speak(message)
    #print("We are in function classify sounds")
    return None #have to be changed

def Introduction():
    messages = ["Perfect. Now you'll get an introduction",
                'Lovely. You will now learn how to classify the sounds',
                'Great. We are now in the introduction part']
    message = random.choice(messages)
    Speak(message)
    #print("We are in the introduction")
    
    messages2 = ["There are 5 different types of meteors: Underdense meteor.., M meteor.., long overdense meteor, medium overdense meteor. And the short overdense meteor",
                'Meteors are classified into 5 different types, which are: Underdense meteor, M meteor, long overdense meteor, medium overdense meteor. And the short overdense meteor']
    message2 = random.choice(messages2)
    Speak(message2)
    time.sleep(0.5)
    
    #FIRST SOUND
    messages3 = ["The first sound is the underdense meteor",
                "The underdense meteor sounds like this:"]
    message3 = random.choice(messages3)
    Speak(message3)
    time.sleep(0.5)
    Play("meteor1_underdense.wav")
    
    #SECOND SOUND
    messages4 = ["The second sound is the M meteor",
                "The M meteor sounds like this:"]
    message4 = random.choice(messages4)
    Speak(message4)
    time.sleep(0.5)
    Play("meteor2_M.wav")
    
    #THIRD SOUND
    messages5 = ["The third sound is the long overdense meteor",
                "The long overdense meteor sounds like this:"]
    message5 = random.choice(messages5)
    Speak(message5)
    time.sleep(0.5)
    Play("meteor3_long overdense.wav")
    
    #FOURTH SOUND
    messages6 = ["The fourth sound is the medium overdense meteor",
                "The medium overdense meteor sounds like this:"]
    message6 = random.choice(messages6)
    Speak(message6)
    time.sleep(0.5)
    Play("meteor4_medium overdense.wav")
    
    #FIFTH SOUND
    messages7 = ["And the fifth sound is the short overdense meteor",
                "And the short overdense meteor sounds like this:"]
    message7 = random.choice(messages7)
    Speak(message7)
    time.sleep(0.5)
    Play("meteor5_short overdense.wav")
    
    #What to do now?
    messages8 = ["Would you like to repeat, practice or continue to classify the sounds?",
                 "Did you get everything? And would you like to do some practice before starting?"]
    message8 = random.choice(messages8)
    Speak(message8)
    
    text = listen()
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
    
    
    if P == True:
        goto = "practice"
    elif R == True:
        goto = "introduction"
    elif C == True:
        goto = "classify"
    else:
        Speak("You said: '{}'. I can't do anything with this answer.".format(text))
        goto = text
    return goto
    
    goto = "classify"
    return goto

def Practice():
    messages1 = ["We are now in practice",
                 "Now we are going to practice"]
    goto = "end"
    return goto
    

if __name__ == "__main__":
    goto = Welcome(r,mic)
    running = True
    while running is True:
        if goto == "classify":
            goto = Classify_sounds()
        elif goto == "introduction":
            goto = Introduction()
        elif goto == "practice":
            goto = Practice()
        elif goto == "end":
            Speak("Program will close")
            running = False
        else:
            print("something went wrong")
            
    print("\nThis is a debugging message.\ngoto = " + goto)
