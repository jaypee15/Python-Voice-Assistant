import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening !") 
  
    assistant_name =("Jaypee 1 point o")
    speak("I am your Assistant")
    speak(assistant_name)
     
 
def username():
    speak("What should i call you? ")
    boss_name = takeCommand()
    speak("Welcome Mister")
    speak(boss_name)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", boss_name.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
  


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
    
    while True:
        
        query = takeCommand().lower()
        
        
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow .Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Listen to some music")
            
            music_dir = "C:\JAYPEE\MUSIC"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            boss_name = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assistant_name = takeCommand()
            speak("Thanks for naming me")
            speak(assistant_name)
            

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assistant_name)
            print("My friends call me", assistant_name)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Johnpaul.")
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            

        elif 'search' in query:
            
            query = query.replace("search", "")
            query = query.replace("play", "")		
            webbrowser.open(query)


        elif "why have you come to this world" in query:
            speak("I cannot tell you my secret")

        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\user\\Documents\\ME\\Voice Assistant.pptx"
            os.startfile(power)

        elif "who are you" in query:
            speak("I am your virtual assistant")

        
        elif 'lock windows' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how long do you want to stop jaypee 1 point o from listening for commands?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jaypee Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
            
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jaypee.txt', 'w')
            speak("Sir, Should i include date and time?")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        
                    
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "jaypee" in query:
            
            wishMe()
            speak("Jaypee 1 point o at your service Mister")
            speak(assistant_name)

        elif "weather" in query:
            
            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
            
            else:
                speak(" City Not Found ")
            

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assistant_name)

        