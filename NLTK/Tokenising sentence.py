from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import wordnet

def get_synonyms(question_vocab):
    synonyms = set()

    # Process synonyms while skipping None values
    for word in question_vocab:
        if word is None:
            continue
        print(f"Processing word: {word}")  # Debugging print
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())

    return list(synonyms)


def adding_words_to_question(question_stop_words, question_words=[None],add=[None]):
    synonyms = get_synonyms(question_words)

    for stop_words in question_stop_words:
        for question_vocab in synonyms:

            #Combination of words
            combined = f"{stop_words} {question_vocab}".lower()
            combined2 = f"{question_vocab} {stop_words} {question_vocab}".lower()
            combined3 = f"{question_vocab} {stop_words}".lower()
            new_list.append(combined)
            new_list.append(combined2)
            new_list.append(combined3)
            
        if add is None:
            continue
        else:
            add_syn = get_synonyms(add)
            new_list.extend(add_syn)

    # Clean up formatting of generated phrases
    upgraded_question_list = [s.replace("_", " ") for s in new_list]
    print(f"Upgraded list: {upgraded_question_list}")

   

    return upgraded_question_list

#Stop
question = [('• a supported conclusion as to which algorithm the developer should choose. (12 marks)',
                     ['to','and','of','to be','efficient'],
                     ['very ineffecient','take a long time to complete','some users,','could be waiting a long time before their details were retrieved.','search increases greatly','o(n)',
                      'could hinder the growth of the number of users accessing the game.'])]
#Word
op = ['easy', 'understand', 'develop','list','users','not','need','sorted','before','searched','efficient','camelcase']
p = ['high','long']
for question_stop_words in question:
        new_list = []
        stop_words = question_stop_words[1]
        print(f"List of greetings: {stop_words}")

upgraded_question_list = adding_words_to_question(stop_words,op)  # Calls function with None values handled properly
print(upgraded_question_list)
user = input('Enter: ').strip().lower()

# Check user input against generated greetings and synonyms
if any(word in user for word in upgraded_question_list):
    print('Correct')
elif user in stop_words and not upgraded_question_list:  # Ensures greetings are correctly compared
    print('Correcty')
else:
    print('Incorrect')