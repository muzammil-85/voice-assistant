import speech_recognition as sr
import time
import webbrowser
from time import ctime
# importing the pyttsx library
import pyttsx3
  

# initialisation
engine = pyttsx3.init()
  
r = sr.Recognizer()

master = 'sir'
def record_audio(ask=False):
    print("lisening")
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_sphinx(audio)
            print(voice_data)
        except sr.UnknownValueError:
            engine.say('sorry ,i did not get that '+master)
            print('sorry ,i did not get that')
        except sr.RequestError:
            engine.say('sorry , my speech is down '+master)
            print('sorry , my speech is down')
        print("exiting record")
        return voice_data


def respond(voice_data):
    if 'name' in voice_data:
        engine.say('my name is jarvis and lisening')
        print('my name is jarvis')
    if 'time' in voice_data:
        engine.say(ctime())
        print(ctime())
    if 'search' in voice_data:
        engine.say("what do you want to search")
        search = record_audio('what do you want to search')
        engine.say("here what i found")
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)

        print('Here is what i found' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location')
        url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location')
    if 'stop' in voice_data:
        engine.say("ok have nice day")
        exit()
    engine.runAndWait()


time.sleep(1)
print('how can i help you?')
engine.say(master+" I am your personal assitance jarvis ")
engine.say("how can i help you "+master)
engine.runAndWait()
while 1:
    voice_data = record_audio()
    respond(voice_data)
    