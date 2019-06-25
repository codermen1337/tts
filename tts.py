import os, time
from win32com.client import Dispatch

voice = "SAPI.SpVoice"
shit = ""

def ffs():
	global voice, shit
	readtf = input("Read from text.txt? [y/n]: ")
	if readtf == 'n':
		shit = input("Please write/paste what you want to say: ")
		voice = input("Please enter the voice you would like to use (don't write anything to use default voice): ")
		if voice == "": 
			voice = "SAPI.SpVoice"
			speak()
		else:
			speak()
	else:
		print("Reading from text.txt...")
		file = open("text.txt", "r")
		shit = file.readlines()
		voice = input("Please enter the voice you would like to use (don't write anything to use default voice): ")
		if voice == "": 
			voice = "SAPI.SpVoice"
			speak()
		else:
			speak()

def cls():
	os.system("cls")
			
def speak():
	global voice, shit
	speak = Dispatch(voice)
	speak.Speak(shit)
	print("Successfully spoke.")
	time.sleep(5)
	cls()
	ffs()
	
ffs()