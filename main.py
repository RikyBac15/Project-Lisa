import speech_recognition as sr
from playsound import playsound
import python_weather
import asyncio
import struct
import pyaudio
import pvporcupine
import pywhatkit
'''from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window'''
#import pyttsx3
import os
import wikipedia
wikipedia.set_lang("it")

'''access_key = "nXOstMU6qix+GJqaEpYTNDjoz/nqUoWcPBkU4rWd2voWC7lO3/R3dg=="
keyword_paths = ['HotWord_model/hey_lisa_linux_v2.0.0/hey-lisa_en_linux_v2_0_0.ppn']
porcupine = pvporcupine.create(access_key=access_key, keyword_paths=keyword_paths)

pa = pyaudio.PyAudio()

audio_stream = pa.open(rate = 44100, channels = 1, format = pyaudio.paInt16, input = True, frames_per_buffer = 3200)

Window.size = (500, 300)
Window.borderless = True

class Lisa(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window

        return self.window
'''
listener = sr.Recognizer()
listener.pause_threshold = 1
'''engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

async def getweather(date):
	client = python_weather.Client(format=python_weather.METRIC)
	
	weather = await client.find('Bologna')

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()'''

def get_next_audio_frame():

    pass

def take_command():
	try:
		with sr.Microphone(device_index=4) as source:
			print('listening...')
			voice = listener.listen(source)
			command = listener.recognize_google(voice, language="it-IT")
			command = command.lower()
			print (command)
			'''if 'lisa' in command:
				#playsound('Audio/Lisa_wake-up.mp3')
				command = command.replace('lisa', '')
				print (command)'''		
	except:
		pass
	return command

def run_lisa():
	command = take_command()
	if 'cerca informazioni' in command:
		SearchWiki = command.replace('cerca informazioni su ', '')
		print(wikipedia.summary(SearchWiki, sentences=1))
	'''if 'che tempo' in command:
		location = command.replace('che tempo farà ', '')
		date = command.replace('che tempo farà', '') + command.replace('a ', location)
		if (date == 'domani'):
			when = 'tomorrow'
		elif (date == 'oggi'):
			when = 'today'
		print (getweather(when))'''

def lisa_wake():
	with sr.Microphone(device_index=4) as source:
		voice = listener.listen(source)
		hotword = vosk.KaldiRecognizer(model, args.samplerate)
		hotword = command.lower()

'''while True:
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
    keyword_index = porcupine.process(pcm)
    if keyword_index >= 0:
        playsound('Audio/Lisa_wake-up.mp3')'''
run_lisa()
        #pass

if porcupine is not None:
    porcupine.delete()

if audio_stream is not None:
    audio_stream.close()

if pa is not None:
    pa.terminate()