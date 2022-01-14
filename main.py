import speech_recognition as sr
from playsound import playsound
import python_weather
import asyncio
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

'''
Window.size = (500, 300)Trying to implement wake up word with porcupine
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

def take_command():
	try:
		with sr.Microphone(device_index=4) as source:
			print('listening...')
			voice = listener.listen(source)
			command = listener.recognize_google(voice, language="it-IT")
			command = command.lower()
			if 'lisa' in command:
				playsound('Audio/Lisa_wake-up.mp3')
				command = command.replace('lisa', '')
				print (command)			
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

run_lisa()