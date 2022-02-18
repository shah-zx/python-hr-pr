import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# These are the voices present in my pc

# print(voices)

# print(voices[1].id)

engine.setProperty('voice' , voices[0].id)


def speak():
    pass

