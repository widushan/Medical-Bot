from dotenv import load_dotenv
load_dotenv()

# Step 1a : Setup Text To Speech TTS Model with gtts
import os
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text = "Hi this is Ai with Pasindu!"
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")

# Step 1b : Setup Text To Speech TTS Model with ElevenLabs
import elevenlabs
from elevenlabs import voices, generate, save

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
elevenlabs.set_api_key(ELEVENLABS_API_KEY)

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

text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing.mp3")



# Step 2 : Use Model for Text output To Voice