from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from os import path

tts = gTTS(text='Hello, i am Ídi', lang='en')
tts.save('said.mp3')

playsound('said.mp3')

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language="pt-br"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

