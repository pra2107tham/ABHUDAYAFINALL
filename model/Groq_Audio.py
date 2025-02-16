import os
import speech_recognition as sr
import keyboard
import threading
from groq import Groq
import langid 

# Load environment variables



# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Initialize recognizer
recognizer = sr.Recognizer()
stop_recording = False  # Flag to stop recording

# Function to listen for the stop key (`S`)
def listen_for_stop():
    global stop_recording
    while True:
        if keyboard.is_pressed("s"):
            print("🛑 Stop key ('S') detected. Stopping recording...")
            stop_recording = True
            break

# Function to transcribe speech in real-time
def real_time_transcription():
    global stop_recording
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Press 'R' to start speaking. Press 'S' to stop.")

        # Wait for the user to press 'R' to start speaking
        while not keyboard.is_pressed("r"):
            pass  # Do nothing, just wait

        print("🎙️ Recording started... Speak now!")
        stop_recording = False

        # Start a separate thread to monitor for "S" key press
        stop_thread = threading.Thread(target=listen_for_stop, daemon=True)
        stop_thread.start()

        full_transcript = ""

        while not stop_recording:
            try:
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)  # Record speech in chunks
                text = recognizer.recognize_google(audio)
                detected_lang, _ = langid.classify(text)
                print(f"📝 You said: {text}")  # Show what user is saying
                full_transcript += text + " "  # Append text to final transcript

            except sr.UnknownValueError:
                print("⚠️ Could not understand, please speak clearly.")
            except sr.RequestError:
                print("❌ Speech recognition service error.")

        return full_transcript.strip()

# Start recording and transcription
spoken_text = real_time_transcription()

if spoken_text:  # Only send to Groq if some text was recorded
    print("\n🔄 Sending to Groq for cleanup...")

    try:
        # Send spoken text to Groq for refinement
        groq_response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an AI assistant that refines spoken text, removing noise and grammatical errors."},
                {"role": "user", "content": f"Here is the spoken text: {spoken_text}. Please rephrase it in a clean and grammatically correct way."}
            ],
            model="llama-3.3-70b-versatile",
        )

        # Extract the cleaned-up text
        clean_text = groq_response.choices[0].message.content

        # Print the final cleaned text
        print("\n✨ Final Text (Cleaned by Groq):")
        print(clean_text)

    except Exception as e:
        print(f"❌ Error processing with Groq: {e}")

else:
    print("⚠️ No speech detected. Try again.")

print("\n✅ Done!")

def get_clean_text():
    return clean_text

