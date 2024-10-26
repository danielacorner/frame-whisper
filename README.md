# Frame Translator

A Flask application that uses Frame SDK to provide real-time speech translation through Frame smart glasses. The app listens for speech input when the user taps the Frame, transcribes it using OpenAI's Whisper model, translates it using Google Cloud Translate, and displays both the original and translated text on the Frame display.

## Features

- Speech-to-text using OpenAI's Whisper
- Text translation using Google Cloud Translate
- Real-time display on Frame glasses
- Tap gesture control
- Default translation from English to Korean
- Automatic silence detection
- Scrolling text display for longer translations

## Prerequisites

- Python 3.8 or higher
- Frame SDK and Frame glasses
- Google Cloud account with Translation API enabled
- Google Cloud credentials JSON file

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd frame-translator
```

2. Create and activate a virtual environment:
```bash
# Windows
npm run venv
npm run venv:activate

# macOS/Linux
npm run venv
npm run venv:activate:mac
```

3. Install dependencies:
```bash
npm run install:py
```

4. Configure Google Cloud credentials:
   - Download your Google Cloud credentials JSON file
   - Update the `.env` file with the path to your credentials:
     ```
     GOOGLE_APPLICATION_CREDENTIALS=path/to/your-credentials.json
     ```

## Usage

1. Start the Flask server:
```bash
npm run start
```

2. The Frame display will show "Tap to start speaking..."

3. Tap the Frame to begin recording

4. Speak your message (recording stops after 2 seconds of silence or 10 seconds max)

5. Wait for processing and translation

6. View the original text and translation on the Frame display

7. Tap again to translate another message

## API Endpoints

- `POST /start`: Initiates the translation process
  - Returns: `{"status": "success"}`

## Cleanup

To remove temporary audio files:
```bash
npm run clean
```

## License

MIT

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request