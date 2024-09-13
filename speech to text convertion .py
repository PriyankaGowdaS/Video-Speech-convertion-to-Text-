#!/usr/bin/env python
# coding: utf-8

# In[2]:


import speech_recognition as sr
from googletrans import Translator
import moviepy.editor as mp

# Load the video
video = mp.VideoFileClip("VID_20240508_234207.mp4 p1")

# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile("1.wav")

# Initialize recognizer
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile("1.wav") as source:
    audio_data = r.record(source)

# Recognize speech (Kannada) from the audio
try:
    kannada_text = r.recognize_google(audio_data, language="kn-IN")
    print("\nThe Kannada text from the video is: \n")
    print(kannada_text)
except sr.UnknownValueError:
    print("Speech recognition could not understand the Kannada audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Translate Kannada text to English
translator = Translator()
translated_text = translator.translate(kannada_text, src='kn', dest='en').text

# Output the translated text
print("\nThe translated text to English is: \n")
print(translated_text)


# In[ ]:




