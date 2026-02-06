import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Audio could not be understood."
    except sr.RequestError as e:
        return f"Error with the speech recognition service: {e}"


if __name__ == "__main__":
    audio_path = "audio_sample.wav"

    print("\n================ AUDIO TRANSCRIPTION ================\n")
    transcription = transcribe_audio(audio_path)
    print("Transcribed Text:")
    print(transcription)
