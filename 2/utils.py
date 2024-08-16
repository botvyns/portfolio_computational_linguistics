import stanza
import tokenize_uk
import re
import random
random.seed(7)

uk_nlp = stanza.Pipeline(lang='uk', verbose=False)

def filter_words(text):
    words_list = tokenize_uk.tokenize_words(text)
    filtered_words = [word for word in words_list if re.match(r"^[А-ЩЬЮЯҐЄІЇа-щьюяґєії][А-ЩЬЮЯҐЄІЇа-щьюяґєії’ʼ']*?[А-ЩЬЮЯҐЄІЇа-щьюяґєії]?$", word)]
    return filtered_words, len(filtered_words)

def substitute_user_mentions_and_links(text):
    # Regular expression to match user mentions
    user_mention_pattern = r'@\w+'

    # Regular expression to match links
    link_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    text = re.sub(user_mention_pattern, '', text)

    text = re.sub(link_pattern, '', text)

    text = re.sub(r'[a-zA-Z]+', '', text)

    return text.lower()

def sample_rows(subset, sampled_df):
    words = 0
    rows = subset.index.tolist()  
    random.shuffle(rows) 
    for index in rows:
        row = subset.loc[index]
        if words + row['num_words'] <= 20000:
            sampled_df.loc[len(sampled_df)] = row
            words += row['num_words']

def lemmatize(cleared_text):
    lemmas = []
    for sent in uk_nlp(' '.join(cleared_text)).sentences:
        for word in sent.words:
            lemmas.append(word.lemma)
    return lemmas


def calculate_statistics(df):
    V_wordforms_unique = len(set(wordform for sublist in df['tokens'] for wordform in sublist))
    V_lemmas_unique = len(set(lemma for sublist in df['lemmatized_words'] for lemma in sublist))
    N_wordforms = sum(len(sublist) for sublist in df['tokens'])
    vocab_richness = V_lemmas_unique / N_wordforms
    avg_word_freq = N_wordforms / V_lemmas_unique
    V1 = sum(1 for sublist in df['tokens'] for wordform in sublist if sum(1 for s in df['tokens'] if wordform in s) == 1)
    richness_for_text = V1 / N_wordforms
    richness_for_vocab = V1 / V_lemmas_unique
    V10 = sum(1 for sublist in df['tokens'] for wordform in sublist if sum(1 for s in df['tokens'] if wordform in s) >= 10)
    concentration_index_text = V10 / N_wordforms
    concentration_index_vocab = V10 / V_lemmas_unique

    return {
        'V_wordforms_unique': round(V_wordforms_unique,3),
        'V_lemmas_unique': round(V_lemmas_unique,3),
        'vocab_richness': round(vocab_richness,3),
        'avg_word_freq': round(avg_word_freq,3),
        'V1': round(V1,3),
        'richness_for_text': round(richness_for_text,3),
        'richness_for_vocab': round(richness_for_vocab,3),
        'V10': round(V10,3),
        'concentration_index_text': round(concentration_index_text,3),
        'concentration_index_vocab': round(concentration_index_vocab, 3)
    }