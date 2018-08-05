import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pyttsx3
import webbrowser
new = 2
import requests
from bs4 import BeautifulSoup
import pyglet
##os.environ["HTTPS_PROXY"] = "https://ipg_2014037:79971521@192.168.1.107:3128"
##os.environ["HTTP_PROXY"] = "https://ipg_2014037:79971521@192.168.1.107:3128"
##pyglet.lib.load_library('avbin')
##pyglet.have_avbin=True

def speak(audioString):
    print(audioString)
    ################################### Way 1 ############################################
##    tts = gTTS(text=audioString, lang='en')
##    filename = 'audio'
##    tts.save(filename+'.mp3')
####    os.system("start audio.mp3")
##    os.startfile("audio.mp3")
    tts = gTTS(text=audioString, lang='en')
    filename = 'temp.mp3'
    tts.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)

    ################################# Way 2 ####################################
    # engine = pyttsx3.init()
    # engine.say(audioString)
    # engine.runAndWait()
 
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
    
 
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
##        data = data.split(" ")
        location = data[9:]
        speak("Hold on Rahul, I will show you where " + location + " is.")
##        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;",new = new)
    if "open" in data:
##        data = data.split(" ")
        location = data[5:]
        speak("Hold on Rahul")
        webbrowser.open("https://www."+location+".com",new = new)
    if "search for" in data:
        data = data[10:]
        speak("give me some time")
        webbrowser.open("https://www.google.com/search?source=hp&ei=ch0FWr-lLsP5kwWiiYugBw&q="+data+"&oq="+data+"&gs_l=psy-ab.3..0i131k1l3j0i20i264k1l2j0i131k1j0l2j0i131k1l2.12371.14491.0.14839.10.9.0.0.0.0.572.1086.2-2j5-1.4.0....0...1.1.64.psy-ab..6.4.1404.6..35i39k1.319.-lYZLuRyYno",new=new)
    if "play" and "on YouTube" in data:
        data = data[5:][::-1][11:][::-1]
        speak("playing")
        webbrowser.open("https://www.youtube.com/results?search_query="+data,new=new)

    if "give me direction" in data:
        speak("what is your location")
        text1 = recordAudio()
        speak("where you want to go")
        text2 = recordAudio()
        webbrowser.open("https://www.google.com/maps/dir/"+text1+"/"+text2+"/")

    if "top" and "headline" and "Hindu" in data:
        link = 'http://www.thehindu.com/todays-paper/'
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")

        c = 0
        for i in soup.find_all("ul",{'class':'archive-list'}):
            for j in i.find_all("li"):
                k = j.text
                if c <= 15 and k!='nearby':
                    speak(k)
                    c += 1

    if "top" and "headline" and "times of India" in data:
        link = 'https://timesofindia.indiatimes.com/mostread.cms?day=1'
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        c = 0

        for i in soup.find_all("div",{'class':'listing4 clearfix'}):
            for j in i.find_all("li"):
                k = j.text
                if c<=10:
                    speak(k)
                    c += 1
                    
    if "launch" in data:
        data = data[7:]
        try:
            os.startfile('E:\\python files\\speech to text\\exe files\\'+data)
        except:
            print("check again")
    
    



time.sleep(2)
speak("Hi Rahul, what can I do for you?")

while 1:
    data = recordAudio()
    jarvis(data)
