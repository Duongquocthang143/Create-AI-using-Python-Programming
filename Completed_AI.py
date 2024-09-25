import speech_recognition
import pyttsx3
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init() 
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic: 
		print("Robot: I'm listening, go ahead ")
		audio = robot_ear.listen(mic)
	print("robot: ...")
	try:	
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("you: "+ you)

	if you == "":
		robot_brain = "I can't hear you, please try again!!"
	elif "hello" in you:
		robot_brain = "hello Dương Quốc Thắng"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "president" in you:
		robot_brain = "Tô Lâm"
	elif "girlfriend" in you:
		robot_brain = "She looks so cute and beautiful so i'm jealous with you "
	elif "bye" in you:
		robot_brain = "See you Thắng!"
		print("robot: "+robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "I'm fine thanks!"
	 
	print("robot: "+robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()