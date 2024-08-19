import speech_recognition as sr
import webbrowser
import pyttsx3
import pygame
import os
from gtts import gTTS
import time

engine = pyttsx3.init()

engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    else:
        print(f"Unrecognized command: {c}")

def readCommandFromFile(file_path, start_position):
    """
    Read commands from the file starting from `start_position`.
    Returns the next command and the new file position.
    """
    try:
        with open(file_path, 'r') as file:
            file.seek(start_position)
            lines = file.readlines()
            if not lines:
                return None, start_position

            jarvis_active = False
            for i, line in enumerate(lines):
                line = line.strip()
                if "jarvis" in line.lower():
                    jarvis_active = True
                elif jarvis_active:
                    position = start_position + sum(len(line) + 1 for line in lines[:i+1])  # Calculate new file position
                    return line, position

            return None, start_position + sum(len(line) + 1 for line in lines)  # Move position to end of file
    except Exception as e:
        print("Error reading from file:", e)
        return None, start_position


if __name__ == "__main__":
    speak("initializing Jarvis.....")
    current_position = 0  # Start reading from the beginning initially
    while True:

        # # For read command from file
        # command, current_position = readCommandFromFile('command.txt', current_position)
        # if command:
        #     print(f"Command from file: {command}")
        #     processCommand(command)
        #     speak(f"Executing command: {command}")
        #     time.sleep(10)  # Wait for 20 seconds before the next check
        # else:
        #     # Sleep briefly if no command was found to avoid busy waiting
        #     time.sleep(1)


        # # For read command from Microphone

        r = sr.Recognizer()

        print("Recognizer....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "alexa"):
                speak("  Yyahh")

                with sr.Microphone() as source:
                    print("Alexa active")
                    audio = r.listen(source)
                    print("Recognizer..")
                    command = r.recognize_google(audio)
                    speak(command)
                    processCommand(command)

        except Exception as e:
            print("Error; ", e)
