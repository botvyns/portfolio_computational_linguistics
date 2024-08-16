import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import LinearSVC
from functions import document_contains


documents = [(list(movie_reviews.words(fileid)), category)
for category in movie_reviews.categories()
for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
    
print("-" * 15)
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(f'20 найбільш уживаних слів у корпусі: {all_words.most_common(20)}')

print("-" * 15)
deep_stats = all_words['deep']
print(f'Кількість вживань слова deep корпусі: {deep_stats}')

print("-" * 15)

neg_words = []

for file in movie_reviews.fileids('neg'):
    neg_words.extend(movie_reviews.words(file))

neg_words_stats = nltk.FreqDist(neg_words)['deep']

pos_words = []

for file in movie_reviews.fileids('pos'):
    pos_words.extend(movie_reviews.words(file))

pos_words_stats = nltk.FreqDist(pos_words)['deep']

print(f"Кількість вживань слова  deep серед негативних відгуків {neg_words_stats}")
print(f"Кількість вживань слова  deep серед позитивних відгуків {pos_words_stats}")


all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:3700] 

print("-" * 15) 

words = document_contains(movie_reviews.words('pos/cv016_4659.txt'), word_features)

print([(k, v) for k, v in words.items() if v])


word_features = list(all_words)[:2000] 

train_set = [(document_contains(d, word_features), c) for (d,c) in documents[:1800]]
test_set = [(document_contains(d, word_features), c) for (d,c) in documents[1800:]]

classifier = nltk.NaiveBayesClassifier.train(train_set)

print("-" * 15)

print(f"Точність Баєсового класифікатора {nltk.classify.accuracy(classifier, test_set)}")

print("-" * 15)

print(classifier.show_most_informative_features(20))

print("-" * 15)

LinearSVC = SklearnClassifier(LinearSVC()).train(train_set)
print(f"Точність LinearSVC класифікатора {nltk.classify.accuracy(LinearSVC, test_set)*100}")