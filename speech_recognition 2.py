import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pyttsx3
import webbrowser
new = 2
from collections import defaultdict

def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

##dict = defaultdict(str)
def hhru():
    speak("i am fine")
def time():
    speak(ctime())
def where(data):
        location = data[9:]
        speak("Hold on Divanshu, I will show you where " + location + " is.")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;",new = new)
    


dict = {}
dict['how are you'] = hhru
dict['what time is it'] = time
dict['where is'] = where


def jarvis(data):
    k = dict[data]
    k()


speak("Hi Divanshu, what can I do for you?")

while 1:
    data = recordAudio()
    jarvis(data)

