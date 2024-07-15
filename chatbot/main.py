from bot import ChatBot
from tts import TextToSpeech

def main():
    chatbot = ChatBot()
    tts = TextToSpeech()

    test_inputs = [
        "Hello, how can I book an appointment?",
        "What are your operating hours?",
        "Can you help me with a booking?",
        "Tell me a joke."
    ]

    for input_text in test_inputs:
        print("You:", input_text)
        response = chatbot.generate_response(input_text)
        print("Bot:", response)
        audio = tts.convert(response)

        # Save the audio as a .wav file
        audio_filename = f"response_{input_text[:10].replace(' ', '_')}.wav"
        with open(audio_filename, "wb") as f:
            f.write(audio)

        print(f"Audio response saved as '{audio_filename}'.")

if __name__ == "__main__":
    main()
