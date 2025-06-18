from dotenv import load_dotenv
load_dotenv()




# Step 1a : Setup Text To Speech TTS Model with gtts
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text = "Hi this is Ai with Pasindu!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")





# Step 1b : Setup Text To Speech TTS Model with ElevenLabs
import elevenlabs
from elevenlabs import voices, generate, save

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
elevenlabs.set_api_key(ELEVENLABS_API_KEY)

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    # Get available voices
    available_voices = voices()
    # Find Aria's voice
    aria_voice = next((voice for voice in available_voices if voice.name == "Aria"), None)
    
    if aria_voice is None:
        raise Exception("Aria voice not found")
    
    audio = generate(
        text=input_text,
        voice=aria_voice,
        model="eleven_turbo_v2"
    )
    
    save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text=input_text, output_filepath="elevenlabs_testing.mp3")






# Step 2 : Use Model for Text output To Voice

import subprocess
import platform

def play_audio_file(output_filepath):
    os_name = platform.system()
    file_ext = os.path.splitext(output_filepath)[1].lower()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            if file_ext == ".mp3":
                # Try ffplay for mp3
                try:
                    subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], check=True)
                except Exception as e:
                    print(f"ffplay failed: {e}. Please ensure ffmpeg is installed and ffplay is in PATH.")
            elif file_ext == ".wav":
                subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            else:
                print(f"Unsupported file type for playback: {file_ext}")
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    play_audio_file(output_filepath)

input_text = "Hi this is Ai with Pasindu!, Auto play testing"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    # Get available voices
    available_voices = voices()
    # Find Aria's voice
    aria_voice = next((voice for voice in available_voices if voice.name == "Aria"), None)
    
    if aria_voice is None:
        raise Exception("Aria voice not found")
    
    audio = generate(
        text=input_text,
        voice=aria_voice,
        model="eleven_turbo_v2"
    )
    
    save(audio, output_filepath)
    play_audio_file(output_filepath)

# text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing_autoplay.mp3")





