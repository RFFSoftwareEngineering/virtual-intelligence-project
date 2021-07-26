from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
from os import path
import time
import sys
import webbrowser
import pyautogui
from unidecode import unidecode


tts = gTTS(text="Hello, i am Ídi, initializing complete..", lang="en")
tts.save("said.mp3")

playsound("said.mp3")


def main():
    while True:
        mic = sr.Recognizer()
        mic.pause_threshold = 3.4
        with sr.Microphone() as source:
            mic.adjust_for_ambient_noise(source)
            source.SAMPLE_WIDTH = 2
            print("speak...")
            audio  = mic.listen(source)
        try:
            comando = mic.recognize_google(audio, language="pt-br" or "en-us")
            print(f"Você disse: {comando}")
        except sr.UnknownValueError:
            playsound("said1.mp3") #removed TTS save, so i don't get a conflict beetween an already created file (she says: sorry i couldn't understand)
            main()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
                           
#space for functions of the assistant:

        if len(comando) > 0:
            query = comando.lower()
            print(comando.lower())
            if  "abra open abre" and "google" in query:
                edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
                webbrowser.get("edge").open("www.google.com")
                tts1 = gTTS(text="what you want me to search for? Mister Creator", lang="en")
                tts1.save("said3.mp3")
                playsound("said3.mp3")
                mic = sr.Recognizer()
                mic.pause_threshold = 3.4
                with sr.Microphone() as source:
                    mic.adjust_for_ambient_noise(source)
                    source.SAMPLE_WIDTH = 2
                    print("speak...")
                    audio0  = mic.listen(source)
                try:
                    comando0 = mic.recognize_google(audio0, language="pt-br" or "en-us")
                    print(f"Você disse: {comando}")
                except sr.UnknownValueError:
                    playsound("said1.mp3")
                    main()
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
                if len(comando0) > 0:
                    subquery0 = comando0.lower()
                    print(f"pesquisando: {subquery0}")
                    pyautogui.write(unidecode(subquery0), interval=0.05)
                    pyautogui.press("enter")
                else:
                    main()
            elif "apague acenda luz luzes" and "garagem" in query:
                tts6 = gTTS(text="clicking on garage lights on our awesome automation system sir")
                tts6.save("said5.mp3")
                playsound("said5.mp3")
                edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
                webbrowser.get("edge").open("http://192.168.0.2/")
                print("waiting the page to load...")
                time.sleep(2)
                pyautogui.moveTo(433, 387)
                time.sleep(0.7)
                pyautogui.click()
                time.sleep(3)
            elif "apague acenda luz luzes" and "jardim" in query:
                tts7 = gTTS(text="clicking on yard's lights sir...")
                tts7.save("said6.mp3")
                playsound("said6.mp3")
                edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
                webbrowser.get("edge").open("http://192.168.0.2/")
                print("waiting the page to load...")
                time.sleep(2)
                pyautogui.moveTo(427, 501)
                time.sleep(0.7)
                pyautogui.click()
                time.sleep(3)
            elif "fechar desligue pare exit" and "assistente" in query:
                tts0 = gTTS(text="finishing assistant execution proccess", lang="en")
                tts0.save("said2.mp3")
                playsound("said2.mp3")
                print("saindo...")
                os._exit(1) 
            else:
                main()
            
        else:
            main()

main()

sys.exit()
