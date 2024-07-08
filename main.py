#For MacOs
"""import os
if __name__ == '__main__':
    x = input("Welcome to RoboSpeaker")
    while True:
    x = input("Enter what you want me to speak: ")
    if x == "q":
        os.system("say 'bye'")
        break;
    command = f"say {x}"
    os.system(command)"""

#For Windows
import win32com.client as wincom

    # you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = input("What you want to speak: ")
speak.Speak(text)

# 3 second sleep
time.sleep(3)

text = "This text is read after 3 seconds"
speak.Speak(text)