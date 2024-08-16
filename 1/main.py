from utils import summary, rte_features
from nltk.corpus import wordnet as wn
import nltk

summ1 = summary("ww_interview.txt", 1)
summ2 = summary("ww_interview.txt", 3)

print("---------- Реферат з порогом 1 ----------", end="\n\n")
print(summ1, end="\n\n")

print("---------- Реферат з порогом 3 ----------", end="\n\n")
print(summ2, end="\n\n")

print("---------- Усі логічні зв'язки для першого значення дієслова reach ----------", end="\n\n")
print(wn.synset('reach.v.01').entailments(), end="\n\n")

rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])[18]
extractor = nltk.RTEFeatureExtractor(rtepair)
print("---------- Пошук логічних зв’язків між текстами та гіпотезами ----------", end="\n\n")
print(f"Ключові слова з тексту: {extractor.text_words}", end="\n\n")
print(f"Ключові слова з гіпотези: {extractor.hyp_words}", end="\n\n")
print(f"Перекриття між текстом і гіпотезою серед звичайних слів: {extractor.overlap('word')}", end="\n\n")
print(f"Перекриття між текстом і гіпотезою серед іменованих сутностей (NE): {extractor.overlap('ne')}", end="\n\n")
print(f"Звичайні слова, які містяться лише в гіпотезі: {extractor.hyp_extra('word')}", end="\n\n")
print(f"Iменовані сутності, які містяться лише в гіпотезі: {extractor.hyp_extra('ne')}", end="\n\n")
