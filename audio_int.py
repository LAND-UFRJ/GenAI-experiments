import streamlit as st
import speech_recognition as sr
import pydub
import requests
from io import BytesIO
from langchain_openai import ChatOpenAI
llm = ChatOpenAI


st.title("Chatbot Interface")
st.write("Talk to your AI assistant!")

recognizer = sr.Recognizer()
recording = False
audio_data = None
ip_address = #ip da ia port 9000

def listen():
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        return audio

if st.button("🎤 Speak"):
    if not recording:
        recording = True
        st.session_state.audio = listen()
    else:
        recording = False
        audio_data = st.session_state.audio
        with open("recording.wav", "wb") as f:
            f.write(audio_data.get_wav_data())
        
        # Sending the recording to the given IP address
        with open("recording.wav", "rb") as f:
            files = {"file": f}
            response = requests.post(ip_address, files=files)
            if response.status_code == 200:
                st.write("Audio sent successfully!")
            else:
                st.write("Failed to send audio.")

user_input = st.text_input("You: ", "Hello, how are you?")

if st.button("Send"):
    if user_input:
        response = llm.invoke(user_input).content
        st.write(f"Chatbot: {response}")
