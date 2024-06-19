import speech_recognition as sr
import pyttsx3

# Initialize recognizer
recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)

            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized: {text}")

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        continue
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        break  # Optional: Break the loop if there is an API error
