import speech_recognition as sr
import time
#import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
from mutagen.mp3 import MP3
import wave #wav files
import contextlib #wav files
import os #to delete files

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

def check_words(term,term2,term3,words):
    if term in words:
        return True
    elif term2 in words:
        return True
    elif term3 in words:
        return True
    return False

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
    myobj = gTTS(text=sentence, lang=language, slow=False)
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
        r.adjust_for_ambient_noise(source, duration = 1) # can be to long error
        print("DEBUG: ambientnoise end")
        Play("Sounds/Bleep.wav") #bleep sound
        print("speak now")
        audio = r.listen(source, timeout = 3) # can be to long error
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