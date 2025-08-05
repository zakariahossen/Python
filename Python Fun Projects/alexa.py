import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except sr.RequestError:
        talk("Sorry, I couldn't access the microphone.")
    except sr.UnknownValueError:
        talk("Sorry, I couldn't understand what you said.")
    return command


def run_alexa():
    command = take_command()
    if not command:
        talk("I didn't hear anything. Please try again.")
        return

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '').strip()
        if song:
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        else:
            talk("Please specify a song name.")
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '').strip()
        try:
            info = wikipedia.summary(look_for, sentences=1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("There are multiple results for your query. Please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("I couldn't find any information on that topic.")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry vaiya, I am in another relation')
    else:
        talk('I did not get it. Please try again.')


while True:
    run_alexa()
