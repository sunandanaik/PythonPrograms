# -*- coding: utf-8 -*-
"""
Created on Sat May  22 18:49:41 2021

@author: DELL
Visit:https://pypi.org/project/SpeechRecognition/ and go to PyPI and click Download files:SpeechRecognition wheel file
Then create third-party folder into current project directory and copy paste wheel file in it.
Then run >pip3 install ./third-party/SpeechRecognition-3.8.1-py2.py3-none-any.whl
To install pyaudio if error, try >pip install pipwin ;followed by >pipwin install pyaudio
To send emails, you must enable less secure apps with your google admin account.
"""
from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init('sapi5') #inbuilt voice to use
voices = engine.getProperty('voices')
#print(voices)
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour) #extracting hours from 0-24
    if hour >=0 and hour <=24:
        speak("Good Morning!")
    elif hour >=12 and hour <16:
        speak("Good Afternoon!!")
    elif hour >=16 and hour <=19:
        speak("Good Evening!!")
    elif hour >19 and hour <=23:
        speak("Good Night!!")
    speak("I am Jarvis. Please tell me how may I help you?")

def takeCommand():
    #it takes microphone input from user and returns string output
    r = sr.Recognizer() # helps in recognizing audio
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of nonspeaking audio before phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognising...")
        query= r.recognize_google(audio,language='en-in')
        print(f"You said : {query}\n")
    except Exception as ex:
        #print(ex)
        print("Didnt Hear.Say that again Please!!...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587) #587-port no
    server.ehlo()
    server.starttls()
    server.login('sungitmca@gmail.com','your-password')#store your password in text file and read pwd from file
    server.sendmail('sungitmca@gmail.com',to,content)
    server.close()



if __name__=="__main__": 
    speak("Welcome Sunanda!!")
    wishMe()
    while True:
    #or if 1:
        query=takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='E:\\Songs'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,7)])) #to play random songs from the given list
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sunanda, the time is {strTime}")
        elif 'open word' in query:
            #codePath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            #To open word doc
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
        elif 'email to sunanda' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="senderEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!!")
            except Exception as ex:
                print(ex)
                speak("Sorry Sunanda, I am not able to send this email at the moment.")





