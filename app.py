import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import os
import sys
sys.path.append('/path/to/ffmpeg')

import time

@st.cache(suppress_st_warning=True)
def progresso():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.2)
        my_bar.progress(percent_complete + 1)

def transform_text(file):
    with open(os.path.join("", str(file.name)), 'wb') as f:
        f.write(file.getbuffer())

    AudioSegment.from_file(str(file.name)).export(str(file.name)[0:-4]+'.wav', format='wav')

    r = sr.Recognizer()

    with sr.AudioFile(str(file.name)[0:-4]+'.wav') as source:
        src = r.record(source)
        
        text = r.recognize_google(src, language='pt-br')
        
        progresso()

        return text

def play_video(file):
    st.video(file.read())

    st.write(transform_text(file))

def play_audio(file):
    st.audio(file.read())

    st.write(transform_text(file))
    

file = st.file_uploader('Selecione um arquivo', type=['mp4', 'mp3'])


if file:
    if file.type == 'video/mp4':
        play_video(file)
    else:
        play_audio(file)

#https://blog.jcharistech.com/2021/01/21/how-to-save-uploaded-files-to-directory-in-streamlit-apps/