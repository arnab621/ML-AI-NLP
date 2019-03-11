# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from os import path
output = " "
def speech2text (chunk):
    AUDIO_FILE = path.join("/Users", "arnab", "Documents", "COde", chunk)
    global output
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
    try:
        output+=str(" ~ ")
        output+= str(r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

myaudio = AudioSegment.from_file("test.wav" , "wav") 
chunk_length_ms = 10000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = "chunk{0}.wav".format(i)
    print "exporting", chunk_name
    chunk.export(chunk_name, format="wav")
    speech2text(chunk_name)
    print output
