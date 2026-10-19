from nltk.corpus import wordnet

def two_syn(words):
    synonyms = set()

    
    question_1c = [
    (['sensible','naming','8','conventions'],
     ['meaningful','identifiers'],
     ['convey','purpose','clarify','structure','start','end','username'])]
    
    
    pos_tag = 'VB'

   
    
    for word in words:
        for syn in wordnet.synsets(word[0],pos=word[1]):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
                        

    print(list(synonyms))






word = [('book',wordnet.NOUN),
         ('hype',wordnet.VERB),
          ('fire',wordnet.NOUN),
         ('heaven',wordnet.NOUN),
         ('good',wordnet.VERB),
         ('bad',wordnet.VERB),
         ('sad',wordnet.NOUN),
         ('more',wordnet.ADV),
         ('more', wordnet.ADJ)
        ]





two_syn(word)