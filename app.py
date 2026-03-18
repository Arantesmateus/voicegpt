import whisper
import os
import numpy as np
import sounddevice as sd
from playsound import playsound
from dotenv import load_dotenv
from groq import Groq
from gtts import gTTS
from scipy.io import wavfile

#Load settings from .env file
load_dotenv()

language = "pt"

#Get the API value
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#Set the API Key and Instance the Groq
client = Groq(
    api_key = GROQ_API_KEY,
)


#Listen to the mic
print("Fale algo...")
audio = sd.rec(5*16000, samplerate=16000, channels=1, dtype=np.float32)
sd.wait()
print("Gravado!\n")

#Save the request audio file
wavfile.write("request_audio.wav", 16000, audio)

#Set the record file with the audio flattened
record_file = audio.flatten()

#Transcribe the audio to text
model =  whisper.load_model("small")
result = model.transcribe(record_file, fp16=False, language = language)
transcription = result["text"]
print(transcription)

#Calling the grop to response the request
response = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [{
        "role":"user", "content":transcription
    }]
)

#Get the response from the chat api as text
chat_response = response.choices[0].message.content

#Get and save the answer from the API as sound
gtts_object = gTTS(text=chat_response, lang=language, slow=False)
response_audio = "response_audio.wav"
gtts_object.save(response_audio)

print("Processando...\n")

#Play the response audio
playsound(response_audio)

#Print the response only after the audio is played
print("Reposta do chat: \n")
print(chat_response)
