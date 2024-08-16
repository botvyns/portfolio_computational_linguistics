import nltk
from nltk.corpus import wordnet as wn
from operator import itemgetter
from collections import defaultdict

def print_definitions(word):
    print(f"Definitions for '{word}':")
    for synset in wn.synsets(word):
        print(synset.name(), ":", synset.definition(), "\n")

def print_relations(word):
    print(f"Hypernyms and Hyponyms for '{word}':")
    for synset in wn.synsets(word, wn.NOUN):
        print("Hypernyms --->", synset.name(), ":", synset.hypernyms(), "\n")
        print("Hyponyms --->", synset.name(), ":", synset.hyponyms(), "\n")

def find_common_hypernym(word1, word2):
    print(f"Common Hypernym for '{word1}' and '{word2}':")
    print(wn.synset(f"{word1}.n.01").lowest_common_hypernyms(wn.synset(f"{word2}.n.01")))

def calculate_similarity(word1, word2):
    print(f"Semantic Similarity between '{word1}' and '{word2}':")
    winner = wn.synset(f"{word1}.n.01")
    loser = wn.synset(f"{word2}.n.01")
    print("Path Distance Similarity:", winner.path_similarity(loser))
    print("Wu-Palmer Similarity:", winner.wup_similarity(loser))
    print("Leacock Chodorow Similarity:", winner.lch_similarity(loser))

def calculate_levenshtein_distance(word1, word2):
    print(f"Levenshtein Distance between '{word1}' and '{word2}':")
    print(nltk.edit_distance(word1, word2, transpositions=False))

# def find_closest_words(user_word, num_words):
#     distances = {}
#     with open("1-1000.txt", "r") as file:
#         for line in file:
#             word_distance = nltk.edit_distance(user_word, line.strip(), transpositions=False)
#             distances[line.strip()] = word_distance
#     sorted_dict = sorted(distances.items(), key=itemgetter(1))
#     closest_words = sorted_dict[:num_words]
#     return closest_words

# def dict_distance(word, num_words):
#     distances = {}
#     file = open("1-1000.txt", "r")
#     lines = file.readlines()
#     file.close()
#     for line in lines:
#         word_distance = nltk.edit_distance(word, line.strip(), transpositions=False)
#         distances[line.strip()] = word_distance
#     sorted_dict = sorted(distances.items(), key=itemgetter(1))
#     closest_words = []
#     for i in range(num_words):
#         closest_words.append(sorted_dict[i])
#     return closest_words

def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    lemmatized_tokens = [nltk.stem.WordNetLemmatizer().lemmatize(token.lower()) for token in tokens if token.isalpha()]
    return lemmatized_tokens

def calculate_word_frequencies(tokens):
    word_frequencies = defaultdict(int)
    for token in tokens:
        word_frequencies[token] += 1
    return word_frequencies

def sort_words_by_frequency(word_frequencies):
    return sorted(word_frequencies.items(), key=itemgetter(1), reverse=True)

def find_closest_words(user_word, words, num_words):
    closest_words = sorted(words, key=lambda w: nltk.edit_distance(user_word, w, transpositions=False))[:num_words]
    return closest_words

def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_input_int = int(user_input)
            return user_input_int
        except ValueError:
            print("Please, enter valid number")