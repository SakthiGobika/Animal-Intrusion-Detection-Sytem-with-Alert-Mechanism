import speech_recognition as sr
import os
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening for speech...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("Transcribed Text: " + text)
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
    from transformers import pipeline
from transformers import pipeline

summarizer = pipeline("summarization")

text = """Today we talked about machine learning, covering supervised learning, unsupervised learning, and reinforcement learning. Supervised learning uses labeled data to train models. Unsupervised learning finds patterns in unlabeled data. Reinforcement learning involves an agent interacting with an environment to maximize rewards.
"""

summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

print("Summary: ", summary[0]['summary_text'])

from transformers import pipeline

summarizer = pipeline("summarization")

text = """
Today we talked about machine learning, covering supervised learning, unsupervised learning, and reinforcement learning. Supervised learning uses labeled data to train models. Unsupervised learning finds patterns in unlabeled data. Reinforcement learning involves an agent interacting with an environment to maximize rewards.
"""

summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

print("Summary: ", summary[0]['summary_text'])
with open("lecture_notes.txt", "a") as file:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Transcribed: {text}")
            file.write(text + "\n")
        except Exception as e:
            print("Error:", e)
import pyttsx3

engine = pyttsx3.init()
engine.say("Lecture Notes: " + text)
engine.say("Summary: " + summary[0]['summary_text'])
engine.runAndWait()
