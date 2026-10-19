from nltk.corpus import stopwords
from random import shuffle
from itertools import product, permutations, combinations


def stop_words():
    #Stop words being establish by the stop words key words
    stopword = stopwords.words('english')
       
    
    return list(stopword)
       
    
def filtering():
    stopword_list = stop_words()

    
  
    stopword_list.append('i')
    stopword_list.append('went')
   

    #newlist = [x for x in fruits if x != "apple"]

    #Remove words list
    remove_letter = ['q','w','e','r','t','y','u','o','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','ma','qor']
    #Removing alphabetic letters except for words
    filtered = [s for s in stopword_list if s not in remove_letter]
        
    return filtered


l = []
filtered = filtering()
lp = ['kim']
op = ['park']
new = filtered.copy()

brand = filtered.copy()

shuffle(new)

shuffle(brand)

l=[]
s = ['mouse','giraffe']

for combo in product(lp, filtered, new, op):
    pi = ' '.join(list(combo)).lower()
    l.extend([pi])

for combo1 in product(lp, filtered, op):
    pin = ' '.join(list(combo1)).lower()
    l.extend([pin])

pri = list(set(l))

print(len(pri))

pds = len(pri)

p = input(': ').lower().strip()

if any(u in p for u in pri):
    print('correct')
else:
    print('incorrect')