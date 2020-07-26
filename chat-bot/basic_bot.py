from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot_name = "a bot"

bot = ChatBot(
    bot_name,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

trainer = ListTrainer(bot)

trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

print(f"Hi, I am {bot_name}! Type something to begin...")

while True:
    try:
        bot_input = input("You: ")
        bot_response = bot.get_response(bot_input)
        print(f"{bot_name}: {bot_response}")

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
