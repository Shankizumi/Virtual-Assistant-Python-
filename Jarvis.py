'''
Author:Shashank Gupta
Date: 22 May 2022
program Name: Jarvis
Purpose: To surve as an AI
'''


from time import strftime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

numbu = random.randint(0, 9)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning.")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon.")
    else:
        speak("Good Evening.")

    speak("I am Friday sir. Plese tell me, how may I help you?")


def takecommand():
    '''it takes microphone input from the user and return string output.'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        #speak("please, say that again sir")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takecommand().lower()
    # logic for executing task based on query.
        if 'wikipedia' in query:
            speak("Searching wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[numbu]))
        elif 'play a song' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[numbu]))    
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime} ")
        elif 'open code' in query:
            codepath = "C:\\Users\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'how are you' in query:
            speak("I am wonderful sir. Thank you for asking")
        elif 'what is your name' in query:
            speak("I am Friday sir, i am your personal assistant.")

        elif 'what is my name' in query:
            speak("Sir, you never told me your name.")
        elif 'what is my nickname' in query:
            speak("haha, i kmow your nickname too, it is shank right?")
        elif 'yes' in query:
            speak("yeah, i know. i am always right.")
        elif 'who is the owner' in query:
            speak('Shashank Gupta is the owner of this pc.')    
        elif 'hey friday' in query:
            speak('hello! what can i help you with.')    
        elif 'tell me a joke' in query:
            speak('sorry, i suck at this and i can not think of any.')    

        if 'quit' in query:
            exit()
