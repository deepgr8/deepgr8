
from math import e
from PyQt5.QtWidgets import QInputDialog
import keyboard
import playsound
import requests

from pyttsx3.engine import Engine
import speech_recognition as sr 

from time import ctime 
import webbrowser 
import time
import subprocess
import pyttsx3


import datetime 
import wikipedia
import os
# from mainfile import InputDialog

import pywhatkit
from keyboard import play, press,press_and_release



class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

def engine_speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine_speak("good morning ")
        engine_speak("i am, your personal assistant, tell me how may i help you")

    elif hour>=12 and hour<18:
            engine_speak("good afternoon ")
            engine_speak("i am, your personal assistant, tell me how may i help you")

    else:
        engine_speak("good evening ")
        engine_speak("i am, your personal assistant, tell me how may i help you")

r=sr.Recognizer()
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.0
        audio = r.listen(source ,5 ,5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        engine_speak("Say that again please...")
        return "None" 
    return query

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "9085685fe1mshb5b26d0134fd891p1ac19djsn1736123a2e1a",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()






def there_exists(terms):
    for term in terms:
        if term in query:
            return True


def task():
        global query
        wishMe()
        while True:
        
                query = takeCommand().lower() #Converting user query into lower case

                # 1: greeting
                # if there_exists(['hi','hello']):
                #     greetings = ["hey, how can I help you", "hey, what's up?", "I'm listening", "how can I help you"]
                #     greet = greetings[random.randint(0,len(greetings)-1)]
               
                
                
                
                
                
                try:    # engine_speak(greet)
                    
                    
                    if there_exists(['what is your name','your name']):
                        engine_speak("I dont have any name, but you call me your personal assistant")

                    
                    def search(cityname):
                        
                        for each in response['state_wise']:
                            if int(response['state_wise'][each]['active']) != 0:
                                for city in response['state_wise'][each]['district']:
                                    if city.lower()==user2.lower():
                                        return city,response['state_wise'][each]['district'][city]['active']

                    
                    if there_exists(['corona','covid','tracker','covid19']):
                        engine_speak("for which city you want to know")
                        

                        user2=takeCommand().lower()
                    
                        result=search(user2)
                        engine_speak(f"Total number of cases in {user2} {result}")
                        
                    if there_exists(['date','Date','date today']):
                        engine_speak(f"Date is {datetime.date.today()}")
                                
                        
                        



                    elif there_exists(["how are you","how are you doing"]):
                        engine_speak("I'm very well, thanks for asking ")

                    elif there_exists(["what's the time", "tell me the time", "what time is it"]):
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        engine_speak(f"the time is {strTime}")
                        print(strTime)

                    elif there_exists(['sleep']):
                        engine_speak("okay")
                        # a=int(input("for how long do i go to in sleep mode"))
                        time.sleep(10)
                    elif there_exists(['wake up']):
                        engine_speak("I'm here")
                        task()

                
                        




                    # 5: search google
                    elif there_exists(["search for","search on google","google"]) and 'youtube' not in query:
                        search = query.split()[-0:-3]
                        search_term=' '.join(str(d) for d in search)
                        url = "https://google.com/search?q=" + search_term
                        webbrowser.get().open(url)
                        engine_speak("Here is what I found for" + search_term + "on google")

                    # 6: search youtube
                    elif there_exists(['YouTube','open YouTube','youtube']):
                            engine_speak("okay, what you want to play in youtube")
                            choice=takeCommand()
                            pywhatkit.playonyt(choice)
                            
                    elif there_exists(['pause','stop','play']):
                        keyboard.press('k')
                    elif there_exists(['minimize the video','minimise','minimise the video']):
                        keyboard.press('i')
                    elif there_exists(['skip','skip the video','forward']):
                        keyboard.press('l')
                    elif there_exists(['Next','next video']):
                        keyboard.press('n')
                    elif there_exists(['full screen','full']):
                        keyboard.press('f')
                    elif there_exists(['close youtube','close tab']):
                        pywhatkit.close_tab()

                    elif there_exists(['skype','open skype']):
                        engine_speak("okay wait a second...")
                        url1="https://www.skype.com/en/free-conference-call/?cm_mmc=accessurl"
                        webbrowser.get().open(url1)


                    #7: get stock price
                    elif there_exists(["price of"]):
                        search_term = query.split("for")[-1]
                        url = "https://google.com/search?q=" + search_term
                        webbrowser.get().open(url)
                        engine_speak("Here is what I found for " + search_term + " on google")

                    # search for music
                    elif there_exists(["play music"]):
                        search_term= query.split("for")[-1]
                        url="https://open.spotelify.com/search/"+search_term
                        webbrowser.get().open(url)
                        engine_speak("You are listening to"+ search_term +"enjoy sir")



                    #search for amazon.com
                    elif there_exists(["amazon.com","amazon"]):
                        search_term = query.split()[-1]
                        url="https://www.amazon.in/"
                        webbrowser.get().open(url)

                        engine_speak("here is what i found for"+search_term + "on amazon.com")

                    #make a note
                    elif there_exists(["make a note"]):
                        search_term=query.split("for")[-1]
                        url="https://keep.google.com/#home"
                        webbrowser.get().open(url)
                        engine_speak("Here you can make notes")

                    #open instagram
                    elif there_exists(["open instagram","want to have some fun time"]):
                        search_term=query.split()[-1]
                        url="https://www.instagram.com/"
                        webbrowser.get().open(url)
                        engine_speak("opening instagram")

                    #open twitter
                    elif there_exists(["open twitter"]):
                        search_term=query.split()[-1]
                        url="https://twitter.com/"

                        webbrowser.get().open(url)
                        engine_speak("opening twitter")

                    elif there_exists(['shutdown','turnoff']):
                            engine_speak("Hold On a Sec ! Your system is on its way to shut down")
                            subprocess.call("shutdown /p /f")

                    # elif there_exists(['close']):
                    #     search=query.split()[-1]
                    #     search_term='.exe'.join(search)
                    #     os.system(f"taskkill /F /IM {search_term}")

                    elif there_exists(['open notepad']):
                        engine_speak("opening...")
                        d=query.split()[1]
                        e=d+".exe"
                        print(e)
                        a=subprocess.Popen(e)

                    elif there_exists(['close notepad']):
                        a.terminate()

                    elif there_exists(["close chrome"]):
                        ch=query.split()[-1]
                        ro=ch+".exe"

                        
                        subprocess.call(["taskkill","/F","/IM",ro])





                    #9 weather
                    elif there_exists(["weather","tell me the weather report","whats the condition outside"]):
                        search_term = query.split("wheather in")[-1]
                        url = "https://www.google.com/search?q="+search_term
                        webbrowser.get().open(url)
                        engine_speak("Here is what I found for on google")

                    #open gmail
                    elif there_exists(["open my mail","gmail","check my email"]):
                        search_term = query.split()[-1]
                        url="https://mail.google.com/mail/u/0/#inbox"
                        webbrowser.get().open(url)
                        engine_speak("here you can check your gmail")





                    #12 calc
                    elif there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
                        opr = query.split()[1]

                        if opr == '+':
                            engine_speak(f"The sum is, {int(query .split()[0]) + int(query.split()[2])}")
                        elif opr == '-':
                            engine_speak(f"answer is, {int(query.split()[0]) - int(query.split()[2])}")
                        elif opr == 'multiply':
                            engine_speak( f"answer is, {int(query.split()[0]) * int(query.split()[2])}")
                        elif opr == 'divide':
                            engine_speak(f"answer is, {int(query.split()[2]) / int(query.split()[0])}")
                        elif opr == 'power':
                            engine_speak(f"answer is, {int(query.split()[0]) ** int(query.split()[2])}")
                        else:
                            engine_speak(
                                    "check your expression again"
                            )



                    #13 screenshot
                    elif there_exists(["capture","my screen","screenshot"]) :
                        pywhatkit.take_screenshot()

                    


                    #14 to search wikipedia for definition
                    elif 'wikipedia' in query:
                        engine_speak("searching wikipedia....")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences = 3)
                        engine_speak("according to wikipedia")
                        engine_speak(results)
                    else:
                        engine_speak("")




                    if there_exists(["krishna","hi krishna"]):
                        engine_speak("hello.. I'm here for you just click on start button")
                        break
                    

                                     
                    


                    if there_exists(["exit","bye","Goodbye"]):
                        engine_speak("okay thanks for giving me time")
                        engine_speak('You can call me any time, by just saying hello krishna')
                        break

                    

                except Exception as e:
                    print(e)

task()



        






