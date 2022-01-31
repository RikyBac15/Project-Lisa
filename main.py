import speech_recognition as sr
from playsound import playsound
<<<<<<< Updated upstream
#import python_weather
=======
>>>>>>> Stashed changes
import asyncio
#import gui
import pyttsx3
import os
import wikipedia
import pywhatkit
#openweather json call
import requests, json
from datetime import datetime
wikipedia.set_lang("it")


listener = sr.Recognizer()
listener.pause_threshold = 2


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
		with sr.Microphone(device_index=0) as source:
			print('listening...')
			#listener.adjust_for_ambient_noise(source)
			voice = listener.listen(source)
			command = listener.recognize_google(voice, language="it-IT")
			command = command.lower()
			print(command)

	except:
		print("ERROR")
		#exit()
    
	return command

def run_lisa():
	command = take_command()
	if 'ora' in command:
		now = datetime.now()

		current_time = now.strftime("%H:%M")
		print("Orario Attuale =", current_time)

	if 'cerca informazioni' in command:
		SearchWiki = command.replace('cerca informazioni su ', '')
		print(wikipedia.summary(SearchWiki, sentences=1))
		#gui.WikiWindow(wikipedia.SearchWiki.images[0], wikipedia.summary(SearchWiki, sentences=1, auto_suggest=True, redirect=True))
	
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

	if 'meteo' in command:
		#coso di openweather
		api_key = "f7e24a88f356a42160be8be935ac5e17"

		base_url = "http://api.openweathermap.org/data/2.5/weather?"

		city_name = command.replace('dimmi il meteo di ', '')

		complete_url = base_url + "appid=" + api_key + "&units=metric" + "&lang=it" + "&q=" + city_name

		response = requests.get(complete_url)

		x = response.json()

		if x["cod"] != "404":

			y = x["main"]

			current_temperature = y["temp"]

			current_pressure = y["pressure"]

			current_humidity = y["humidity"]

			z = x["weather"]

			weather_description = z[0]["description"]

			print(" Temperatura = " +
				str(current_temperature) + "°C" +
				"\n Pressione Atmosferica = " +
				str(current_pressure) + "hPa" +
				"\n umidità = " + 
				str(current_humidity) + "%" +
				"\n descrizione = " +
				str(weather_description))

		else:
			print(" Città inesistente ")
<<<<<<< Updated upstream
=======
			speak("Non sono riuscita a trovare la città, riprovare")
		
	if 'cerca informazioni' in command:
		SearchWiki = command.replace('cerca informazioni su ', '')
		print(wikipedia.summary(SearchWiki, sentences=1))
		speak("Ecco cosa ho trovato su " + SearchWiki + wikipedia.summary(SearchWiki, sentences=1))
		#gui.WikiWindow(wikipedia.SearchWiki.images[0], wikipedia.summary(SearchWiki, sentences=1, auto_suggest=True, redirect=True))
	
	if 'riproduci' in command:
		song = command.replace('riproduci', '')
		pywhatkit.playonyt(song)
		speak("Riproduco " + song)
>>>>>>> Stashed changes


if __name__ == "__main__":
	run_lisa()
	#Window = MainWindow()
