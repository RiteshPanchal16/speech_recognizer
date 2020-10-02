import speech_recognition as sr
import webbrowser
import time
r = sr.Recognizer()
def  record_audio(ask= False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech services is down')
        return voice_data

def respond(voice_data):
    if 'what is your name'or"tell me your name" in voice_data:
        print('i am a speech recognization system')
        
    if 'what time is it' in voice_data:
        print(time.ctime())
        
    if 'search on Google' in voice_data:
        search=record_audio('What do you want to search for?')
        url='http://google.com/search?q='+ search
        webbrowser.get().open(url)
        print('Here is what I found for'+ search)
    if 'location' in voice_data:
        search= record_audio('which location')
        url='https://www.google.co.in/maps/place/'+search
        webbrowser.get().open(url)
        print("location" + search)

        
print('How can i help you?')
voice_data=record_audio()
respond(voice_data)
