from gtts import gTTS
from time import sleep
import os
import pyglet
os.environ["HTTPS_PROXY"] = "https://ipg_2014037:79971521@192.168.1.107:3128"
tts = gTTS(text='hellow divanshu, what are you doing', lang='en')
filename = 'temp.mp3'
tts.save(filename)

music = pyglet.media.load(filename, streaming=False)
music.play()

sleep(music.duration) #prevent from killing
os.remove(filename) #remove temperory file
