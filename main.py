import speech_recognition as sr
from playsound import playsound
import pyaudio

listener = sr.Recognizer()

try:
	with sr.Microphone() as source:
		print('listening...')
		playsound('Audio/Wake-up.wav')
		voice = listener.listen(source)
		command = listener.recognize_google(voice)
		print (command)

except:
	pass
