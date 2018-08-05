from gtts import gTTS
import os
os.environ["HTTPS_PROXY"] = "https://ipg_2014037:79971521@192.168.1.107:3128"
class Speech(object):
	def __init__(self):
		while True:
			try:
				a = input("What you want me to say: ")
##				a = unicode(a, "utf-8")
				tts = gTTS(text=a, lang="en")
				
				filename = 'aado.mp3'
				tts.save(filename)

				os.system("mpg123 aado.mp3")
				os.system("clear")
				os.system("rm %s" %(filename))
			except UnicodeDecodeError:
				print("Some characters are not supported.")
spc = Speech()
