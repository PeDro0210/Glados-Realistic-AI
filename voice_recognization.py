from speech_recognition import Recognizer,Microphone,WaitTimeoutError
import openai
import os
from API_KEYS_FOR_FRIENDS import Open_AI_API
import keyboard

Open_AI_KEY= Open_AI_API
recognizer = Recognizer()
model="whisper-1"



def voice_recognization():
    try:
        #takes input from microphone and saves it in a file
        if (keyboard.is_pressed('space')):
            with Microphone() as Users_microphone:
                print(f"\033[34mINFO:\033[0m \033[38;5;208mGlados is listening\033[0m")
                Users_audio = recognizer.listen(Users_microphone, timeout=2)
                os.system("cls")
                print(f"\033[34mINFO:\033[0m \033[38;5;208mGlados done listening\033[0m")
                with open("src/Audios/microphone-results.wav", "wb") as f:
                    f.write(Users_audio.get_wav_data())
            return True                                                            
        else:
            return None

    except WaitTimeoutError:
        print(f"\033[34mINFO:\033[0m \033[38;5;208mGlados done listening\033[0m")
        return None


def TTSQuery():
    openai.api_key = Open_AI_KEY
    #sends audio as bytes to openai and gets the text
    with open("src/Audios/microphone-results.wav", "rb") as audio_file:
        glados_response = openai.Audio.transcribe(file=audio_file, model=model)

        if glados_response['text']=="" or glados_response['text']==" " or glados_response['text']==None:
            pass
        else:                
            return glados_response['text']