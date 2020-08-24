import os
import pyttsx3

print()

print("\t\t\t\tHello my name is leonne , what can I do for you?")
print("\t\t\t\t```````````````````````````````")
pyttsx3.speak("Tell me, what can I do for you?")
pyttsx3.speak("Leonne here , what can I do for you?")
global application
global cmd

def command():
	if ("run" in x):
		pyttsx3.speak("running " + application)
	elif ("launch" in x):
		pyttsx3.speak("launching " + application)
	elif ("open" in x):
		pyttsx3.speak("opening " + application)
	else:
		print("Nothing")

print()
def desire():
	print("Launching the application as soon as possible")
print()
def exit_1():
	print("Exit")
	pyttsx3.speak("GoodBye")
	

while True:
	x = input(" Enter your command: ").lower()
	if ((("run" in x) or ("open" in x) or ("launch" in x)) and (("notepad" in x) or ("editor" in x))):
		application = "notepad"
		command()
		desire()
		os.system(application)
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("explorer" in x) or ("fileexplorer" in x))):
		application = "file explorer"
		command()
		desire()
		os.system("explorer")
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and ("chrome" in x)):
		application = "chrome"
		command()
		desire()
		os.system(application)
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("ppt" in x) or ("powerpnt" in x) or ("powerpoint" in x))):
		application = "powerpoint"
		command()
		desire()
		os.system("powerpnt")
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("winword" in x) or ("word" in x) or ("msword" in x))):
		application = "MS Word"
		command()
		desire()
		os.system("winword")
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("excel" in x) or ("msexcel" in x))):
		application = "MS excel"
		command()
		desire()
		os.system("excel")
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("paint" in x) or ("mspaint" in x))):
		application = "MS paint"
		command()
		desire()
		os.system("mspaint")
		print(" ------------------------------------")
	elif (("exit" in x) or ("close" in x) or ("terminate" in x)):
		print("\n  See you next time!")
		pyttsx3.speak("See you next time")
		exit_1()
		break
	else:
		print(" :( Wrong Input!")
		pyttsx3.speak("Wrong Input, try again")
		print(" ------------------------------------")
print()
