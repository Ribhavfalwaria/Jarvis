import pyttsx3
import datetime
import speech_recognition as sr
import pyjokes
import wikipedia
import webbrowser as wb
import psutil
import os
import pyautogui
import random
import time
import json
from urllib.request import urlopen
import requests

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
   Time = datetime.datetime.now().strftime("%H:%M:%S")
   speak('The current time is')
   speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)


def greetings():
    speak("Welcome back Ribhav!")
    time_()
    date_()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
     speak("Good Morning Boss!")
    elif hour >= 12 and hour < 16:
      speak("Good Afternoon Boss!")
    elif hour >= 16 and hour < 24:
     speak("Good Evening Boss!")
    else:
     speak("Its time to sleep boss.")

    speak("Jarvis at your service, How may I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Unable to recognize, Please say again...")
        return "None"
    return query

def cpu():
   usage = str(psutil.cpu_percent())
   speak('CPU is at' + usage)

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/RIBHAV FALWARIA/Desktop/WEB DEVELOPMENT/screenshot.png")
    speak("Done!")

def joke():
    speak(pyjokes.get_joke())

def Introduction():
    speak("I am Jarvis 1.0 , The Personal Virtual/AI assistant , "
          "Speed 8 Gigabytes, Memory 1 Terabyte "
          "I am created by Harshit Arora , "
          "I can do a variety of stuff. ")

def Creator():
    speak("Ribhav created me, He is Studying BCA"
          "He created me as a project for his college , I am one of his fabulous inventions"
         )

if __name__ == "__main__":
    greetings()
    while True:
        query = TakeCommand().lower()
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'yourself' in query:
            Introduction()
        elif 'creator' in query:
            Creator()
        elif 'created' in query:
            Creator()
        elif 'joke' in query:
            joke()
        elif 'cpu' in query:
            cpu()
        elif 'offline' in query:
            speak('Going offline Boss!')
            quit()
        elif 'take screenshot' in query:
            screenshot()
           
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'define' in query:
            speak('Searching...')
            query = TakeCommand().lower()
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("You asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location)
        elif 'take a note' in query:
                speak("What should i write?")
                note = TakeCommand()
                file = open('note.txt', 'w')
                speak("Should I include date and time")
                dt = TakeCommand()
                if 'yes' in dt or 'sure' in dt:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    speak('done taking notes')
                else:
                    file.write(note)
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read())
        elif 'remember something for me' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        elif "i love you" in query:
           speak("Aww, So sweet of you, I love you too. as a Machine!")
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I can be your toyfriend!")
        elif "tell me about your friends" in query:
            speak("I have many friends like Jarvis, Google Assistant, Alexa, Siri!")
        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , ""And I think it is just a mere illusion , ""It is waste of time")