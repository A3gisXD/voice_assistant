import openai
import speech_recognition as sr
import pyttsx3

# Set up OpenAI API
openai.api_key = "secret"

# Initialize TTS engine
tts = pyttsx3.init()
tts.setProperty('rate', 180)

# Initialize recognizer
r = sr.Recognizer()
mic = sr.Microphone()  # Replace with device_index if needed

def chatgpt_reply(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful anime-style voice assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

while True:
    try:
        with mic as source:
            print("Speak now:")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        print("Thinking...")
        reply = chatgpt_reply(text)
        print(f"GPT: {reply}")

        tts.say(reply)
        tts.runAndWait()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        break

    except Exception as e:
        print("Error:", e)
