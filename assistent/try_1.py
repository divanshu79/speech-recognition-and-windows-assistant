from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QRadioButton, QApplication, QMainWindow
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup
import pyglet
new = 2

class Ui_MainWindow(object):
    def Assistent(self):
        print('jsdj')
        self.speak("Hi Divanshu, what can I do for you?")
        # while 1:
        data = self.recordAudio()
        self.jarvis(data)

    def speak(self,audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        filename = 'temp.mp3'
        tts.save(filename)

        music = pyglet.media.load(filename, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(filename)

    def recordAudio(self):
        print('igudczx')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        #
        data = "how are you"
        # try:
        #     data = r.recognize_google(audio)
        #     print("You said: " + data)
        # except sr.UnknownValueError:
        #     print("Google Speech Recognition could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Google Speech Recognition service; {0}".format(e))
        #
        return data

    def jarvis(self,data):
        print('xcgyu')
        if "how are you" in data:
            self.speak("I am fine")

        if "what time is it" in data:
            self.speak(ctime())

        if "where is" in data:
            ##        data = data.split(" ")
            location = data[9:]
            self.speak("Hold on Divanshu, I will show you where " + location + " is.")
            ##        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
            webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;", new=new)
        if "open" in data:
            ##        data = data.split(" ")
            location = data[5:]
            self.speak("Hold on Divanshu")
            webbrowser.open("https://www." + location + ".com", new=new)
        if "search for" in data:
            data = data[10:]
            self.speak("give me some time")
            webbrowser.open(
                "https://www.google.com/search?source=hp&ei=ch0FWr-lLsP5kwWiiYugBw&q=" + data + "&oq=" + data + "&gs_l=psy-ab.3..0i131k1l3j0i20i264k1l2j0i131k1j0l2j0i131k1l2.12371.14491.0.14839.10.9.0.0.0.0.572.1086.2-2j5-1.4.0....0...1.1.64.psy-ab..6.4.1404.6..35i39k1.319.-lYZLuRyYno",
                new=new)
        if "play" and "on YouTube" in data:
            data = data[5:][::-1][11:][::-1]
            self.speak("playing")
            webbrowser.open("https://www.youtube.com/results?search_query=" + data, new=new)

        if "give me direction" in data:
            self.speak("what is your location")
            text1 = self.recordAudio()
            self.speak("where you want to go")
            text2 = self.recordAudio()
            webbrowser.open("https://www.google.com/maps/dir/" + text1 + "/" + text2 + "/")

        if "top" and "headline" and "Hindu" in data:
            link = 'http://www.thehindu.com/todays-paper/'
            r = requests.get(link)
            soup = BeautifulSoup(r.content, "html.parser")

            c = 0
            for i in soup.find_all("ul", {'class': 'archive-list'}):
                for j in i.find_all("li"):
                    k = j.text
                    if c <= 15 and k != 'nearby':
                        self.speak(k)
                        c += 1

        if "top" and "headline" and "times of India" in data:
            link = 'https://timesofindia.indiatimes.com/mostread.cms?day=1'
            r = requests.get(link)
            soup = BeautifulSoup(r.content, "html.parser")
            c = 0

            for i in soup.find_all("div", {'class': 'listing4 clearfix'}):
                for j in i.find_all("li"):
                    k = j.text
                    if c <= 10:
                        self.speak(k)
                        c += 1

        if "launch" in data:
            data = data[7:]
            try:
                os.startfile('E:\\python files\\speech to text\\exe files\\' + data)
            except:
                print("check again")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 247)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        ##################################### Radio Button 1 #####################################################

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.clicked.connect(self.Assistent)
        self.horizontalLayout.addWidget(self.radioButton)

        #################################### Radio Button 1 #####################################################

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        # self.radioButton_2.clicked.connect()
        self.horizontalLayout.addWidget(self.radioButton_2)

        ############################################################################################################

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "start "))
        self.radioButton_2.setText(_translate("MainWindow", "off"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

