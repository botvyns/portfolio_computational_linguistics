# import nltk
import random
from collections import defaultdict

def markov_chain(text):
    # words = nltk.word_tokenize(text)
    words = text.split(' ')
    my_dict = defaultdict(list)
    for current_word, next_word in zip(words[:-1], words[1:]):
        my_dict[current_word].append(next_word)
    my_dict = dict(my_dict)
    return my_dict

def generate_sentence(chain, word_count):
    cur_word = random.choice(list(chain.keys()))
    sentence = cur_word.capitalize()
    for i in range(word_count-1):
        next_word = random.choice(chain[cur_word])
        sentence += ' ' + next_word
        cur_word = next_word
    sentence += '.'
    return sentence

def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_input_int = int(user_input)
            return user_input_int
        except ValueError:
            print("Будь ласка, вкажіть ціле число")
