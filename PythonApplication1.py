from gtts import gTTS
import speech_recognition as sr
import os
from os import path
import time
import sys
import webbrowser
import pyautogui
from unidecode import unidecode
from audioplayer import AudioPlayer


tts = gTTS(text="Hello, i am Ídi, initializing complete..", lang="en")
tts.save("said.mp3")
AudioPlayer("said.mp3").play(block=True)

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))


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
            tts9 = gTTS(text="sorry, i couldn't understand", lang="en")
            tts9.save("said1.mp3")
            AudioPlayer("said1.mp3").play(block=True)
            main()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))                           
#space for functions of the assistant:

        if len(comando) > 0:
            query = comando.lower()
            print(comando.lower())
            if  "abra open abre" and "google" in query:
                webbrowser.get("edge").open("www.google.com")
                tts1 = gTTS(text="what you want me to search for? Mister Creator", lang="en")
                tts1.save("said3.mp3")
                AudioPlayer("said3.mp3").play(block=True)
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
                    AudioPlayer("said1.mp3").play(block=True)
                    main()
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
                if len(comando0) > 0:
                    subquery0 = comando0.lower()
                    if "sair nothing" or "nada" in subquery0:
                        tts = gTTS(text="Ok..", lang="en")
                        tts.save("said7.mp3")
                        AudioPlayer("said7.mp3").play(block=True)
                        main()
                    else:
                        tts11 = gTTS(text="searching...", lang="en")
                        tts11.save("said10.mp3")
                        print(f"pesquisando: {subquery0}")
                        pyautogui.write(unidecode(subquery0), interval=0.05)
                        pyautogui.press("enter")
                else:
                    main()
            elif "apague acenda luz luzes" and "garagem" in query:
                tts6 = gTTS(text="clicking on garage lights on our awesome automation system sir")
                tts6.save("said5.mp3")
                AudioPlayer("said5.mp3").play(block=True)
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
                AudioPlayer("said6.mp3").play(block=True)
                webbrowser.get("edge").open("http://192.168.0.2/")
                print("waiting the page to load...")
                time.sleep(2)
                pyautogui.moveTo(427, 501)
                time.sleep(0.7)
                pyautogui.click()
                time.sleep(3)
            elif "iniciar colocar coloque ativar ative modo" and "trabalho" in query:
                tts8 = gTTS(text="Activating everything right now...")
                tts8.save("said8.mp3")
                AudioPlayer("said8.mp3").play(block=True)
                pyautogui.moveTo(613, 879)
                pyautogui.click()
                pyautogui.moveTo(708, 883)
                pyautogui.click()
                pyautogui.moveTo(960, 879)
                pyautogui.click()
                pyautogui.press('winleft')
                pyautogui.write('hw', interval=0.25)
                pyautogui.press('enter')
                tts10 = gTTS(text="please press left enter", lang="en")
                tts10.save("said9.mp3")
                AudioPlayer("said9.mp3").play(block=True)                
                pyautogui.hotkey('ctrl','shift','esc')
                print("waiting things to open, click on where EDI is executing to give the controls to her again after the admin interrupt")
                time.sleep(5)
                pyautogui.moveTo(211, 880)
                pyautogui.click()
                pyautogui.write('cmd', interval=0.25)
                pyautogui.moveTo(556, 526)
                pyautogui.click()
                AudioPlayer("said9.mp3").play(block=True)
            elif "fechar desligue pare exit" and "assistente" in query:
                tts0 = gTTS(text="finishing assistant execution proccess", lang="en")
                tts0.save("said2.mp3")
                AudioPlayer("said2.mp3").play(block=True)
                print("saindo...")
                break 
            else:
                main()
            
        else:
            main()

main()
