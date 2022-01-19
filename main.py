import speech_recognition as sr
from playsound import playsound
import python_weather
import asyncio
#import gui
#import pyttsx3
import os
import wikipedia
import pywhatkit

wikipedia.set_lang("it")

listener = sr.Recognizer()
listener.pause_threshold = 3

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
			listener.adjust_for_ambient_noise(source)
			voice = listener.listen(source)
			command = listener.recognize_google(voice, language="it-IT")
			command = command.lower()
			print(command)
					
	except:
		print("ERROR")
		exit()

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
	if 'riproduci' in command:
		song = command.replace('riproduci', '')
		pywhatkit.playonyt(song)

	'''
	if 'quanto fa' in command:
		if '+' in command:
			factor1 = command.replace('quanto fa', '')
			factor1 = command.replace('più', '')
	'''

if __name__ == "__main__":
	run_lisa()