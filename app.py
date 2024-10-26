import asyncio
from flask import Flask, jsonify
from frame_sdk import Frame
from frame_sdk.display import Alignment
import whisper
from google.cloud import translate_v2 as translate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
model = whisper.load_model("base")
translate_client = translate.Client()

async def frame_translate():
    async with Frame() as frame:
        # Show initial message
        await frame.display.show_text("Tap to start speaking...", align=Alignment.MIDDLE_CENTER)
        
        # Wait for tap
        await frame.motion.wait_for_tap()
        
        # Show recording message
        await frame.display.show_text("Listening...", align=Alignment.MIDDLE_CENTER)
        
        # Record audio
        audio_data = await frame.microphone.record_audio(
            silence_cutoff_length_in_seconds=2,
            max_length_in_seconds=10
        )
        
        # Save audio temporarily
        await frame.files.write_file("temp_audio.wav", audio_data.tobytes())
        
        # Show processing message
        await frame.display.show_text("Processing...", align=Alignment.MIDDLE_CENTER)
        
        # Convert speech to text using Whisper
        result = model.transcribe("temp_audio.wav")
        text = result["text"].strip()
        
        # Translate text
        translation = translate_client.translate(
            text,
            target_language='ko',
            source_language='en'
        )
        
        # Display both original and translated text
        display_text = f"{text}\n\n{translation['translatedText']}"
        await frame.display.scroll_text(
            display_text,
            lines_per_frame=3,
            delay=0.15,
            color=frame.display.PaletteColors.WHITE
        )
        
        # Clean up
        os.remove("temp_audio.wav")
        
        # Show ready message
        await frame.display.show_text("Tap to translate again...", align=Alignment.MIDDLE_CENTER)

@app.route('/start', methods=['POST'])
def start_translation():
    asyncio.run(frame_translate())
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)