import pyttsx3
import speech_recognition as sr
from datetime import date, datetime
import random

# Initialize text-to-speech engine and recognizer
hear = sr.Recognizer()
speak = pyttsx3.init()

print("Assistant is ready. Say 'bye' to exit.")
print("Try saying 'What can you do")


# Helper functions
def get_date():
    today = date.today()
    return "Today's date is " + today.strftime("%B %d, %Y")

def get_time():
    now = datetime.now()
    return "The current time is " + now.strftime("%I:%M %p")

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What does a storm cloud wear under his raincoat? Thunderwear.",
        "How does the ocean say hi? It waves!"
    ]
    return random.choice(jokes)

def simple_calculation(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return "Sorry, I couldn't calculate that. Please try again with a valid expression."

# main loop
while True:
    try:
        with sr.Microphone() as mic:
            print("Assistant: I'm listening...")
            audio = hear.listen(mic, timeout=5, phrase_time_limit=5)
            you = hear.recognize_google(audio).lower()  
    except sr.UnknownValueError:
        you = ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        continue
    except sr.WaitTimeoutError:
        you = ""

    print('You:', you)

    # understand
    if you == "":
        brain = "I couldn't hear you clearly. Can you please repeat?"
    elif "what can you do" in you:
        print("I can tell you the time, the date, do simple calculations and make jokes","If you want me to do calculations, say 'Calculate....' ")
    elif "hello" in you or "hi" in you:
        brain = "Hello there! How can I help you today?"
    elif "what is the date today" in you or "today" in you:
        brain = get_date()
    elif "what time is it" in you or "time" in you:
        brain = get_time()
    elif "how are you" in you:
        brain = "I'm doing great! What about you?"
    elif "tell me a joke" in you or "make me laugh" in you:
        brain = tell_joke()
    elif "calculate" in you:
        expression = you.replace("calculate", "").strip()
        brain = simple_calculation(expression)
    elif "bye" in you or "goodbye" in you:
        brain = "Goodbye! Have a good day!"
        print('Assistant:', brain)
        speak.say(brain)
        speak.runAndWait()
        break
    else:
        brain = ("I'm not sure how to respond to that. "
                 "You can ask me about the date, time, tell a joke, or do simple calculations.")

    # Responding to the user
    print('Assistant:', brain)
    speak.say(brain)
    speak.runAndWait()
