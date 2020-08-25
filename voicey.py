#from googletrans import Translator
import speech_recognition as sr 
import pyttsx3
from translate import Translator
#translator = Translator()

translator = Translator(to_lang="cs")

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:  
	print("Please wait. Calibrating microphone...")  
	r.adjust_for_ambient_noise(source, duration=5)  
	print("Akshat say something!")  
	audio = r.listen(source)  
check = str(r.recognize_google(audio))

print(check)
translation = translator.translate(check)
print(translation)
engine.say(translation)	
engine.runAndWait()


#answer = translator.translate(check, dest='hi')
#s = str(answer)
#ansr = eval(str)
#fan = ansr['pronunciation'] 
#engine.say(answer)
#engine.runAndWait()