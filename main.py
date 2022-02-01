import speech_recognition as sr
from playsound import playsound
import asyncio
import time
import random
#import gui
#import pyttsx3
import os
import wikipedia
import pywhatkit
#openweather json call
import requests, json
from datetime import datetime
from gtts import gTTS
#import keyboard
#import uinput
import pyautogui

#device =  uinput.Device((uinput.KEY_W,uinput.KEY_Simport os))

language = 'it'

wikipedia.set_lang("it")

listener = sr.Recognizer()
listener.pause_threshold = 2
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
'''
def speak(mytext):
    say = gTTS(text=mytext, lang=language, slow=False)
    say.save("Records/say.mp3")
    playsound("Records/say.mp3")

def take_command():
	try:
		with sr.Microphone(device_index=4) as source:
			print('listening...')
			#listener.adjust_for_ambient_noise(source)
			voice = listener.listen(source)
			command = listener.recognize_google(voice, language="it-IT")
			command = command.lower()
			print(command)

	except:
		print("ERROR")
		speak("Non ho capito, riprovare")
		#take_command()
		#exit()
    
	return command

def run_lisa():
	command = take_command()

	if 'ora' in command:
		now = datetime.now()

		current_time = now.strftime("%H:%M")
		print("Orario Attuale =", current_time)
		speak("Sono le " + current_time)

	elif "creatore" in command:
		speak("I miei creatori sono un gruppo di 4 ragazzi con molta voglia di fare")

	elif "come stai" in command:
		speak(random.choice(["Bene, grazie", "Faccio quello che mi piace, darti una mano", "Sono pronto per le tue domande"]))

	elif 'cara' in command: 
		speak("Ciao Zanna, come sta Giada?")

	elif 'meteo' in command:
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

			current_temperature = round(current_temperature)

			print(" Temperatura = " +
				str(current_temperature) + "°C" +
				"\n Pressione Atmosferica = " +
				str(current_pressure) + "hPa" +
				"\n umidità = " + 
				str(current_humidity) + "%" +
				"\n descrizione = " +
				str(weather_description))
			current_temperature = str(current_temperature)
			speak("La Temperatura attuale a " + city_name + " è di " + current_temperature + "gradi con " + weather_description)

		else:
			print(" Città inesistente ")
			speak("Non sono riuscita a trovare la città, riprovare")
	elif 'cerca informazioni' in command:
		SearchWiki = command.replace('cerca informazioni su ', '')
		print(wikipedia.summary(SearchWiki, sentences=1))
		speak("Ecco cosa ho trovato su " + SearchWiki)
		speak(wikipedia.summary(SearchWiki, sentences=1))
		#gui.WikiWindow(wikipedia.SearchWiki.images[0], wikipedia.summary(SearchWiki, sentences=1, auto_suggest=True, redirect=True))
	
	elif 'riproduci' in command:
		song = command.replace('riproduci', '')
		pywhatkit.playonyt(song)
		speak("Riproduco " + song)
'''
	elif 'play' or 'pausa' in command:
		#keyboard.press_and_release("ctrl+alt+p")
		#device.emit(uinput.KEY_ctrl,1)
		#pyautogui.hotkey('ctrlleft', 'altleft', 'p', 1)
		pyautogui.keyDown('ctrlleft')
		pyautogui.keyDown('alt')
		pyautogui.keyDown('p')
		sleep(0.5)
		pyautogui.keyUp('ctrlleft')
		pyautogui.keyUp('alt')
		pyautogui.keyUp('p')'''
'''
	elif 'quanto fa' in command:
		if '+' in command:
			factor1 = command.replace('quanto fa', '')
			factor1 = command.replace('più', '')
	'''

if __name__ == "__main__":
	#while True:
	run_lisa()
	#Window = MainWindow()
