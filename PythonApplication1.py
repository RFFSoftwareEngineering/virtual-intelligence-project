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
            source.SAMPLE_WIDTH = 2
            print("speak...")
            audio  = mic.listen(source)
            try:
                comando = mic.recognize_google(audio, language="pt-br" or "en-us")
                print(f"Você disse: {comando}")
            except sr.UnknownValueError:
                tts = gTTS(text="Sorry, i couldn't understand..please repeat or try to be more clear", lang='en')
                tts.save('said1.mp3')
                playsound('said1.mp3')
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

main()
