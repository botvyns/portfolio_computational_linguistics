from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from utils import visualize_scores, calculate_jaccard_dist, plot_PCA, preprocess_and_lemmatize
from data import text1, text2, text3, text4
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

texts = preprocess_and_lemmatize([text1, text2, text3, text4])

ctvec_vectorizer = CountVectorizer()
ctvec_matrix = ctvec_vectorizer.fit_transform(texts)

ctvec_array = ctvec_matrix.toarray()

feature_names = ctvec_vectorizer.get_feature_names_out()

df = pd.DataFrame(ctvec_array, columns=feature_names, index=[f"Poetry {i+1}" for i in range(len(texts))])

df = df.T
df['absolute_frequency'] = df.sum(axis=1)
pd.set_option('display.max_rows', 500)
print(df)

pca = PCA(n_components=2)
ctvec_matrix_2d = pca.fit_transform(ctvec_matrix.toarray())

text_names = ['Берези, в снігу занімілі', 'В букварях ти наряджена і заспідничена', 'Встає над нами сонце, як вставало', 'Десь на горизонті хмара-хустка']

plot_PCA(texts, text_names, ctvec_matrix_2d)

euclidean_distances_matrix = euclidean_distances(ctvec_matrix)

cosine_similarity_matrix = cosine_similarity(ctvec_matrix)

jaccard_indexes = calculate_jaccard_dist(texts)

euclidean = pd.DataFrame(euclidean_distances_matrix, columns=text_names, index=text_names)

cosine = pd.DataFrame(cosine_similarity_matrix, columns=text_names, index=text_names)

jaccard = pd.DataFrame(jaccard_indexes, columns=text_names, index=text_names)

visualize_scores(euclidean, 'Euclidean distance')
visualize_scores(cosine, 'Cosine Similarity')
visualize_scores(jaccard, 'Jaccard distance')