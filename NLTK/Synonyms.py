import nltk
from nltk.corpus import wordnet


def one_synonyms():
    synonyms = []
    wn_pos = wordnet.ADV
    for syn in wordnet.synsets('train'):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())


    more = list(set(synonyms))

    print(more)

one_synonyms()