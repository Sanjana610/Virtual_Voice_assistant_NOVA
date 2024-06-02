import datetime
import os
import subprocess

def speak(audio):
    subprocess.call(["say", audio])

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 17:
        speak("Good Afternoon")
    elif 17 <= hour < 18:
        speak("Good Evening")
    else:
        speak("Good Night")

def takeCommand():
    command = input("Enter a command: ")
    return command.lower()

if __name__ == "__main__":
    wishMe()
    speak("Hi, I am Nova. How can I assist you today?")

    while True:
        user_input = takeCommand()

        if 'open spotify' in user_input:
            speak("Opening Spotify")
            subprocess.call(["open", "-a", "Spotify"])

        elif 'open notepad' in user_input:
            speak("Opening TextEdit")
            subprocess.call(["open", "-a", "TextEdit"])

        elif 'open chrome' in user_input:
            speak("Opening Google Chrome")
            subprocess.call(["open", "-a", "Google Chrome"])

        elif 'open youtube' in user_input:
            speak("Opening youtube")
            subprocess.call(["open", "-a", "youtube"])

        elif 'what is the current time' in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif 'what can you do' in user_input or 'what can i do' in user_input:
            speak("I can perform various tasks. You can ask me to open applications like Spotify or TextEdit, or inquire about the current time.")

        elif 'exit' in user_input or 'quit' in user_input:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that command. Please try again.")
 
  
