from gtts import gTTS
import os
os.environ["HTTPS_PROXY"] = "https://ipg_2014037:79971521@192.168.1.107:3128"

tts = gTTS(text='The quick brown fox jumped over the lazy dog.', lang='en')
tts.save("hello.mp3")
os.system("mpg321 hello.mp3")
