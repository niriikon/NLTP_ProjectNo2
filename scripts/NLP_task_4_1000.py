
import sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

"""
Reads in text file given as command line argument and outputs the article which matched query with the best score.
Output is appended to file, allowing looping over a list of text files.
Output files can be given as input files without modification.
"""


# MemoryError possible. Reads every line from the wiki.txt to object called
# documents. One line = one document
path = '/path/to/corpus/' + sys.argv[1]
with open(path, 'r', encoding= 'utf-8') as f:
    documents = f.readlines()
    
# Selects only documents that have atleast 1 000 words
documents_1000 = [x for x in documents if len(x.split()) >= 1000]    

# Rest of the code is basically copied from the lab 1
vectorizer = TfidfVectorizer()
docs_idf = vectorizer.fit_transform(documents_1000)


# Queries: we must decide two different queries
Q_1 = 'capitalism'
Q_2 = 'communism'

def Answering_Q(Q, vectorizer, data):
    Vectors = data.toarray()
    Vq = vectorizer.transform([Q]).toarray()[0]
    
    Scores = []
    for V in Vectors:
        Scores.append(np.inner(Vq, V))
        
    Max_index = Scores.index(max(Scores))
    
    #return Max_index
    
    with open(Q.replace(' ', '') + '_final' + '.txt', 'a+', encoding='utf-8') as f:
        f.write(''.join(documents_1000[Max_index]))
    print('Input: {}\nQuery: {}\nBest index: {}\n'.format(sys.argv[1], Q, Max_index))
    

# We need to save these max index values somewhere because we need those values
# in the next task      
Answering_Q(Q_1, vectorizer, docs_idf)
#Answering_Q(Q_2, vectorizer, docs_idf)
#Answering_Q(Q_3, vectorizer, docs_idf)
#Answering_Q(Q_4, vectorizer, docs_idf)
