from transformers import pipeline
from langchain import ChatChain

class ChatBot:
    def __init__(self, model_name='gpt-2'):
        self.generator = pipeline('text-generation', model=model_name)
        self.chat_chain = ChatChain(self.generator)

    def generate_response(self, input_text):
        response = self.chat_chain(input_text)[0]['generated_text']
        return response