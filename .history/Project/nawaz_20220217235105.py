import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# These are the voices present in my pc

# print(voices)

# print(voices[1].id)

engine.setProperty('voice' , voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
if __name__ == '__main__':
    speak("Hello there , sunny leone here , your new bot")
    

