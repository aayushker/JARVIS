import pyttsx3
import speech_recognition as sr

def initialize_tts():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Choose a voice (0: Male, 1: Female usually)
    engine.setProperty('rate', 150)  # Set speech rate
    return engine

def speak(text, engine):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)  # Use Google recognizer offline alternative next
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return None
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
            return None

def main():
    tts_engine = initialize_tts()
    speak("Hello! I'm ready to assist you. Please say something.", tts_engine)

    while True:
        command = listen()
        if command:
            if "hello" in command:
                speak("Hi there! How can I help you today?", tts_engine)
            elif "how are you" in command:
                speak("I'm just a program, but I'm functioning perfectly! Thanks for asking!", tts_engine)
            elif "exit" in command or "quit" in command:
                speak("Goodbye! Have a great day!", tts_engine)
                break
            else:
                speak("I'm not sure how to respond to that. Can you try something else?", tts_engine)

if __name__ == "__main__":
    main()
