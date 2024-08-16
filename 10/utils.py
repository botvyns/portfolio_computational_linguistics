import matplotlib.pyplot as plt
import seaborn as sns
import pymorphy3
import string

def visualize_scores(scores, title):
  plt.figure(figsize=(10, 6))
  sns.heatmap(scores, annot=True, cmap='coolwarm', fmt='.2f')

  plt.xlabel("Text Documents")
  plt.ylabel("Text Documents")
  plt.title(title)

  plt.show()

def calculate_jaccard_dist(texts):
  jaccard_indexes = []
  for i in range(len(texts)):
      jaccard_row = []
      for j in range(len(texts)):
          if i == j:
              jaccard_row.append(1.0)
          else:
              tokens1 = set(texts[i].split())
              tokens2 = set(texts[j].split())
              intersection = len(tokens1.intersection(tokens2))
              union = len(tokens1) + len(tokens2) - intersection
              jaccard_row.append(1 - (intersection / union))
      jaccard_indexes.append(jaccard_row)
  return jaccard_indexes

def plot_PCA(texts, text_names, ctvec_matrix_2d):
  plt.figure(figsize=(8, 6))
  plt.scatter(ctvec_matrix_2d[:, 0], ctvec_matrix_2d[:, 1])

  for i, text in enumerate(texts):
      plt.annotate(text_names[i], (ctvec_matrix_2d[i, 0], ctvec_matrix_2d[i, 1]))

  plt.xlabel('PCA Component 1')
  plt.ylabel('PCA Component 2')
  plt.title('2D Representation of Count Vectorized Texts')

  plt.show()

morph = pymorphy3.MorphAnalyzer(lang='uk')

def preprocess_and_lemmatize(texts):
    
    # Remove punctuation
    texts = [text.translate(str.maketrans('', '', string.punctuation)) for text in texts]
    
    # Lemmatize the texts
    lemmatized_texts = []
    for text in texts:
        lemmas = []
        for word in text.split():
          parsed_word = morph.parse(word)[0]
          lemmas.append(parsed_word.normal_form)
        lemmatized_texts.append(' '.join(lemmas))
    
    return lemmatized_texts