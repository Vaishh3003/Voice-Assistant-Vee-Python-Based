import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import ctypes  
import pyautogui 
import psutil    
import requests  
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    print(f"Vee: {text}")
    engine.say(text)
    engine.runAndWait()

def vee_command():   
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.pause_threshold = 1 
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "vee" in command:
                command = command.replace("vee", "").strip()
            return command
    except Exception as e:
        return ""

def run_vee():
    command = vee_command()
    if not command:
        return

    if "exit" in command or "stop" in command:
        talk("Goodbye! Have a nice day.")
        exit()

    elif "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)

    elif "superstar" in command:
        person = command.replace("superstar", "")
        info = wikipedia.summary(person, 2)
        talk(info)

    elif "search" in command:
        search_query = command.replace("search", "")
        talk(f"Searching Google for {search_query}")
        pywhatkit.search(search_query)
   
    elif "open notepad" in command:
        talk("Opening Notepad for you.")
        os.startfile("notepad.exe")

    elif "lock my computer" in command:
        talk("Locking the device.")
        ctypes.windll.user32.LockWorkStation()

    elif "write a note" in command:
        talk("What should I write?")
        note_text = vee_command()
        with open("vee_notes.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {note_text}\n")
        talk("Note saved.")

    elif "screenshot" in command:
        img = pyautogui.screenshot()
        img.save("vee_screenshot.png")
        talk("Screenshot saved to your folder.")

    elif "battery" in command:
        battery = psutil.sensors_battery()
        talk(f"Your battery is at {battery.percent} percent.")

    elif "open gmail" in command:
        talk("Opening your mail.")
        webbrowser.open("https://mail.google.com")

    elif "open amazon" in command:
        talk("Opening Amazon.")
        webbrowser.open("https://www.amazon.in/")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    else:
        talk("I didn't quite catch that. Could you say it again?")

talk("Vee initialized. How can I help you?")
while True:
    run_vee()