from google.cloud import texttospeech

# Load the Google Cloud API credentials
credentials_path = 'path_to_your_credentials.json'
client = texttospeech.TextToSpeechClient.from_service_account_json(credentials_path)

# The text you want to convert to speech
input_text = "Hello, this is a demo of the Google Text-to-Speech API."

# Set the text input
synthesis_input = texttospeech.SynthesisInput(text=input_text)

# Select the voice type and language
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Set the audio format
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Generate the TTS request
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Save the generated speech to a file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)

print("Text-to-Speech conversion completed. Output saved as output.mp3")
