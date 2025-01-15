# Voice assistant
This is a Python-based voice-activated virtual assistant capable of responding to user voice commands. It uses speech recognition and text-to-speech synthesis to provide an interactive experience. The assistant performs a variety of tasks, including:

- Telling the current date and time.
- Performing simple arithmetic calculations.
- Sharing jokes to entertain users.
- Engaging in basic conversational exchanges.

## Features
- Voice Recognition: Listens to user input via a microphone and converts it into text using the speech_recognition library.
- Text-to-Speech: Responds to user commands audibly with the pyttsx3 library.
-  Multi-Functional: 
    - Retrieving the current date and time.
    - Telling jokes from a predefined list.
    - Evaluating simple mathematical expressions (e.g., addition, subtraction).
- Interactive Flow: Provides real-time feedback for user input, handles errors gracefully, and ends the session when the user says "bye."

## Installation
Install the required dependencies:

```bash
pip install pyttsx3
pip install speechrecognition
pip install pyaudio
```
## Usage
1. Run the assistant:

```bash
 python va.py
```

2. Interact with the assistant by speaking commands such as:

- "What is the date today?"
- "What time is it?"
- "Tell me a joke."
- "Calculate 5 + 3."
- "Bye."

3. The assistant will respond audibly and terminate when you say "bye."

## Notes
- Ensure your microphone is working and accessible by the program.
- Install PyAudio for speech_recognition to work properly. If installation fails, use the following command:
```bash
pip install pipwin
pipwin install pyaudio

```
