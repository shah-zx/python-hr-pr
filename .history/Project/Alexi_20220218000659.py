import pyttsx3
import datetime

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


if __name__ == '__main__':
    # speak("Hello there , sunny leone here , your new bot")
    wish()