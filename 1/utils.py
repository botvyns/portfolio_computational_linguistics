from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import sent_tokenize
import nltk

def summary(file_name, threshold=None):
    
    # read file 
    
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
    
    # build frequency table
    
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    ps = PorterStemmer()
    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
            
    # tokenize by sentences
    
    sentences = sent_tokenize(text)
            
    # calculate sent score   
    
    sent_value = dict()
    for sent in sentences:
        word_count_in_sentence = len(word_tokenize(sent))
        for wordValue in freqTable:
            if wordValue in sent.lower():
                if sent[:15] in sent_value:
                    sent_value[sent[:15]] += freqTable[wordValue]
                else:
                    sent_value[sent[:15]] = freqTable[wordValue]
        sent_value[sent[:15]] = sent_value[sent[:15]] / word_count_in_sentence

    # calculate average score if threshold is not provided

    if not threshold:
        sumValues = 0
        for entry in sent_value:
            sumValues += sent_value[entry]
        threshold = sumValues / len(sent_value)
        print(threshold, end="\n\n")
        
    # make final summary 
    
    sentence_count = 0
    summary = ''
    for sent in sentences:
        if sent[:15] in sent_value and sent_value[sent[:15]] > (threshold):
            summary += " " + sent
            sentence_count += 1
            
    return summary


def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features["word_hyp_extra"] = len(extractor.hyp_extrs('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features