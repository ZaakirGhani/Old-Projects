import nltk
from nltk.corpus import wordnet

import spacy
spacy.load('en_core_web_sm')

#Synonyms
synonyms = []

words = (['sensible naming styles', 'sensible naming style', 'pep 8','pep8','conventions']
         ,['camelcase', 'snakecase', 'pascalcase','camel case','snake case','pascal case','meaningful identifiers','spacing'],
         ['convey the purpose of each variable', 'variable', 'clarify code structure',' start and end of words'])



for word in words:
    phrase= word[0].split()
    for phrases in phrase:
        for syn in wordnet.synsets(phrases):
            for lemmas in syn.lemmas():
                synonyms.append(lemmas.name())

unique_synonyms = list(set(synonyms))

print(unique_synonyms)

D= input("Enter: ").strip().lower()
if D in unique_synonyms or D in words:
    print("Correct")
else:
    print("Incorrect")

#antanonyms
antonyms = []

for syn in wordnet.synsets('wrong'):
    for lemmas in syn.lemmas():
        if lemmas.antonyms():
            antonyms.append(lemmas.antonyms()[0].name())

unique_antonyms = list(set(antonyms))

print(unique_antonyms)

