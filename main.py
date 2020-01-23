import speech_recognition as sr
from functions import *
from functions_UI.welcome import *
from functions_UI.introduction import *
from functions_UI.help import *
from functions_UI.ReadMessages import *
from functions_UI.practice import *
from functions_UI.classification import *

Messages = ReadFile_Messages("functions_UI\messages.txt")
i = 0
j = 0
r = sr.Recognizer()
#r.pause_threshold = 1.0
#r.phrase_threshold = 1.0
#r.non_speaking_duration = 1.0
mic = sr.Microphone()


if __name__ == "__main__":
    Setup()
    goto = Welcome(r,mic,1)
    running = True
    while running is True:
        if goto == "welcome":
            goto = Welcome(r,mic,2)
        elif goto == "classify":
            goto = Classify_sounds(r,mic)
        elif goto == "introduction":
            goto = Introduction(r,mic)
        elif goto == "practice":
            goto = Practice(r,mic)
        elif goto == "practice_level1":
            goto = Practice_level1(r,mic)
        elif goto == "practice_level2":
            goto = Practice_level2(r,mic)
        elif goto == "practice_level3":
            goto = Practice_level3(r,mic)
        elif goto == "practice_level4":
            goto = Practice_level4(r,mic)
        elif goto == "practice_level5":
            goto = Practice_level5(r,mic)
        elif goto == "practice_level6":
            goto = Practice_level6(r,mic)
        elif goto == "practice_level7":
            goto = Practice_level7(r,mic)
        elif goto == "practice_level8":
            goto = Practice_level8(r,mic)
        elif goto == "end":
            Speak("Program will close")
            running = False
        else:
            print("something went wrong")
            break
            
    print("\nThis is a debugging message.\ngoto = " + goto)
