import os
import tkinter as tk
from tkinter import *
import speech_recognition as sr
import time
import threading

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Create the main Tkinter window
root = tk.Tk()
root.config(bg='#16191c')
root.title('Python Speech Recognition')

def recognize_speech():
    """Function to recognize speech using the Google Web Speech API."""
    listen_button.config(text='Listening...')
    root.update()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        output_text.delete('1.0', 'end')
        output_text.insert(END, text)
    except sr.UnknownValueError:
        # Speech was unintelligible
        output_text.delete('1.0', 'end')
        output_text.insert(END, 'Error: Speech not recognized.')
    except sr.RequestError:
        # API was unreachable or unavailable
        output_text.delete('1.0', 'end')
        output_text.insert(END, 'Error: Unable to access the Google Web Speech API.')

    listen_button.config(text='Listen')

# UI Elements
listen_button = Button(root, text='Listen', command=recognize_speech, pady=20, padx=70, fg='#ffa25f', font='Verdana 15', bg='#16191c', activeforeground='#ffa25f', activebackground='#16191c')
listen_button.pack()

output_text = Text(root, font='Verdana 14', bg='#16191c', fg='#ffa25f')
output_text.pack()

label = Label(root, text='Using Google Voice Recognition', fg='#ffa25f', bg='#16191c')
label.pack(side='right')

label1 = Label(root, text='press listen and start talking.\nwhen you stop talking it will display what you said', fg='#ffa25f', bg='#16191c', font='Verdana 10')
label1.pack(side='left')

root.mainloop()
