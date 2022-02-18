import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# These are the voices present in my pc

print(voices)

# print(voices[1].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 & hour <= 12):
        speak("Good morning babe")
    elif(hour >= 12 & hour <= 18):
        speak("Good afternoon babe")
    else:
        speak("Good evening babe")

    speak("Hi babe , alexi here , wanna have some fun")


def take():
    """This will take my voice as input """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing... wait few seconds")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"user said{query} \n")
        
    except Exception as e:
        print(e)
        print("Hmm.. nah.. say that again..")
        return None
    return query
        


if __name__ == '__main__':
    # speak("Hello there , sunny leone here , your new bot")
    wish()
    take()