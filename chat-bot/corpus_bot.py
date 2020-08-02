from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


bot_name = "a bot"


def start():
    bot = ChatBot(bot_name,
                  logic_adapters=[{
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "Beep boop",
                      "maximum_similarity_threshold": 0.70}],
                  preprocessors=["chatterbot.preprocessors.clean_whitespace"],
                  input_adaptor="chatterbot.input.TerminalAdaptor",
                  output_adaptor="chatterbot.output.TerminalAdaptor",)

    trainer = ChatterBotCorpusTrainer(bot)

    trainer.train(
        "chatterbot.corpus.english",
        )

    print(f"Hi, I am {bot_name}! Type something to begin...")

    while True:
        try:
            bot_input = input("You: ")
            bot_response = bot.get_response(bot_input)
            print(f"{bot_name}: {bot_response}")

        except(KeyboardInterrupt, EOFError, SystemExit):
            break


start()
