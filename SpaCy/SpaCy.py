import nltk
from nltk.corpus import wordnet
from collections import Counter


synonyms = []

m = ['efficient','to','atom']

word = Counter(m)



s = str(synonyms)

synonyms_string = ' '.join(synonyms)
print(synonyms_string)

i = [('mik',[f'mike {synonyms}','d'],['ds'])]

print(any(i for i in synonyms))

for ig in i:
    print(ig[0])
    print(ig[1][0])
    o = input(': ')
    if any(word in o.split() for word in ig[1]):
        print('COrrecty')
    else:
        print('Incorect')
    

def io():
    for w in word:
        for syn in wordnet.synsets(w):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
    print(synonyms)
    pi = input(': ')
    if any(words in pi for words in synonyms):
        print('Correct')
    else:
        print('incorrect')
    return pi

def op():
    pi = io()
    pi

op()