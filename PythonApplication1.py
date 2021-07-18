from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from os import path
import time
import sys
import webbrowser


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
            playsound('said1.mp3') #removed TTS save, so i don't get a conflict beetween an already created file (she says: sorry i couldn't understand)
            main()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
                           
            
#space for functions of the assistant:

        if len(comando) > 0:
            query = comando.lower()
            print(comando.lower())
            if "open" and "google" in query:
                edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
                webbrowser.get("edge").open("www.google.com")
        else:
            main()

main()
