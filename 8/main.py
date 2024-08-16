import logging
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot_corpus
from data import small_talk, math_talk_1, math_talk_2
from utils import markov_chain, generate_sentence, get_integer_input

import time
time.clock = time.time
import collections
collections.Hashable = collections.abc.Hashable

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

# text-generation

myfile = open('austen-emma.txt', 'r')
test_text = myfile.read()

test_dict = markov_chain(test_text)

user_num_words = get_integer_input("Вкажіть ціле число: ")


print(f'Згенерований текст ({user_num_words}): \n' + generate_sentence(test_dict, user_num_words) + '\n')

# small-talk bot

my_bot = ChatBot(name="PyBot", read_only=True, logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"])

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)

print("\nHi! I'm a ChatBot.\n")

for i in range(12):
    user_input = input("User: ")
    print("\n Bot: ", my_bot.get_response(user_input), '\n')

#  german-speaking bot

my_german_bot = ChatBot(name="PyGermanBot", read_only=True, logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"])

corpus_trainer = ChatterBotCorpusTrainer(my_german_bot)

corpus_trainer.train('chatterbot.corpus.german')

print('\nDies ist ein Chatbot auf Deutsch\n')

for i in range(12):
    user_input = input("User: ")
    print("\n Bot: ", my_german_bot.get_response(user_input), '\n')