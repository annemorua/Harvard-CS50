import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.trex(this)
engine.say(this)
engine.runAndWait()
