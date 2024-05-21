import pyttsx3
import datetime
import os
import smtplib

engine = pyttsx3.init('sapi5')  # used for intake api voices from windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 17:
        speak("Good Afternoon")
    elif 17 <= hour < 18:
        speak("Good Evening")
    else:
        speak("Good Night")


def takeCommand():
    # Function to take user input
    command = input("Enter a command: ")
    return command.lower()


if __name__ == "_main_":
    wishMe()
    speak("Hi, I am Nova. How can I assist you today?")

    while True:
        user_input = takeCommand()

        if 'open spotify' in user_input:
            speak("Opening Spotify")
            # Add code to open Spotify here
            # For example, you can use the os.system command:
            os.system("start spotify.exe")

        elif 'open notepad' in user_input:
            speak("Opening Notepad")
            os.system("start notepad.exe")

        elif 'open windows explorer' in user_input:
            speak("Opening Windows Explorer")
            os.system("start explorer.exe")
        
        elif 'open chrome' in user_input:
            speak("Opening Google Chrome")
            # Add code to open Chrome here
            # For example, you can use the os.system command:
            os.system("start chrome.exe")
        elif 'what is the current time' in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")

        elif 'what can you do' in user_input or 'what can i do' in user_input:
            speak("I can perform various tasks. You can ask me to open applications like Spotify or Notepad, open Windows Explorer, or inquire about the current time.")

        elif 'exit' in user_input or 'quit' in user_input:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that command. Please try again.")