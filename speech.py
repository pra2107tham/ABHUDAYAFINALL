import speech_recognition as sr
import time
import threading
import queue
import keyboard
from datetime import datetime

class ContinuousSpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio_queue = queue.Queue()
        self.text_queue = queue.Queue()
        self.is_recording = False
        self.transcribed_text = []
        
    def adjust_ambient_noise(self):
        """Adjust for ambient noise before starting"""
        try:
            with sr.Microphone() as source:
                print("Adjusting for ambient noise. Please wait...")
                self.recognizer.adjust_for_ambient_noise(source, duration=2)
                print("Ambient noise adjustment complete.")
        except Exception as e:
            print(f"Error adjusting for ambient noise: {str(e)}")
            return False
        return True

    def audio_capture_thread(self):
        """Thread to continuously capture audio"""
        try:
            with sr.Microphone() as source:
                while self.is_recording:
                    audio = self.recognizer.listen(source, timeout=None)
                    self.audio_queue.put(audio)
        except Exception as e:
            print(f"Error in audio capture: {str(e)}")
            self.is_recording = False

    def recognition_thread(self):
        """Thread to process audio and convert to text"""
        while self.is_recording or not self.audio_queue.empty():
            if not self.audio_queue.empty():
                audio = self.audio_queue.get()
                try:
                    text = self.recognizer.recognize_google(audio)
                    self.text_queue.put(text)
                    self.transcribed_text.append(text)
                    print(f"Recognized: {text}")
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results; {str(e)}")
                except Exception as e:
                    print(f"Error in recognition: {str(e)}")

    def save_transcript(self):
        """Save the transcribed text to a file"""
        if not self.transcribed_text:
            print("No text to save!")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"transcript_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write('\n'.join(self.transcribed_text))
            print(f"Transcript saved to {filename}")
        except Exception as e:
            print(f"Error saving transcript: {str(e)}")

    def start_recording(self):
        """Start the recording process"""
        if not self.adjust_ambient_noise():
            return

        self.is_recording = True
        self.transcribed_text = []
        
        # Start the audio capture thread
        audio_thread = threading.Thread(target=self.audio_capture_thread)
        audio_thread.start()
        
        # Start the recognition thread
        recognition_thread = threading.Thread(target=self.recognition_thread)
        recognition_thread.start()
        
        print("\nRecording started! Press 'q' to stop recording...")
        
        # Wait for 'q' key to stop recording
        keyboard.wait('q')
        
        self.is_recording = False
        
        # Wait for threads to complete
        audio_thread.join()
        recognition_thread.join()
        
        # Save the transcript
        self.save_transcript()
        
        print("\nRecording stopped and saved!")

def main():
    try:
        # First, install required packages
        # !pip install SpeechRecognition pyaudio keyboard
        
        print("Initializing speech recognition system...")
        recognizer = ContinuousSpeechRecognizer()
        
        print("\nInstructions:")
        print("1. The system will first adjust for ambient noise")
        print("2. Then it will start recording your speech")
        print("3. Speak clearly into your microphone")
        print("4. Press 'q' to stop recording")
        print("5. The transcript will be saved automatically\n")
        
        input("Press Enter to start...")
        recognizer.start_recording()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()