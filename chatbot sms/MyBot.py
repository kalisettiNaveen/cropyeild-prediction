from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

def get_bot_response(user_input):
    return chatbot.get_response(user_input).text

if __name__ == '__main__':
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = get_bot_response(user_input)
        print('Bot:', response)
