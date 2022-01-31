import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('Ho﻿ visto un nero con le scarpe di gomma PORCO DIO, PORCA MADONNA; Le scarpeP di gomma le voglio anchio PORCA MADONNA, PORCO DIO;')
engine.runAndWait()