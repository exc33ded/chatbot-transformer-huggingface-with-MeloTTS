import sys
import os

# Setting the path for MeloTTS
sys.path.append(os.path.join(os.getcwd(), 'MeloTTS'))

from MeloTTS import melo

class TextToSpeech:
    def __init__(self):
        self.tts = melo()

    def convert(self, text):
        audio = self.tts.synthesize(text)
        return audio
