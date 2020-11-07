from os import path as os_path
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# MemoryError possible. Reads every line from the wiki.txt to object called
# documents. One line = one document
if __name__ == '__main__':
	main(os_path.join('..', '..', 'corpus'), 'small.txt', 'anarchism', 'political')

def main(path, dataset, Q_1, Q_2):
	with open(os_path.join(path, dataset), "r", encoding= "utf-8") as f:
	    documents = f.readlines()

	# I had to make a subset from the original data because otherwise MemoryError
	# occurs when calling vectorizer.fit_transform. My largest value is something 
	# between 175 000 and 250 000. However, 5 000 already gives MemoryError in the 
	# Answering_Q function which means that the value for me is something 
	# between 2 500 and 5 000
	#subset_1 = documents[0:2500]

	# Rest of the code is basically copied from the lab 1
	vectorizer = TfidfVectorizer()
	docs_idf = vectorizer.fit_transform(documents)

	# Queries: we must decide two different queries
	#Q_1 = "anarchism and political" # Just testing, should return index of the first document 
	#Q_2 = "something versus something"

	def Answering_Q(Q, vectorizer, data):
	    Vectors = data.toarray()
	    Vq = vectorizer.transform([Q]).toarray()[0]
	    
	    Scores = []
	    for V in Vectors:
	        Scores.append(np.inner(Vq, V))
	        
	    max_index = Scores.index(max(Scores))
	    
	    return ''.join(documents[max_index])

	# We need to save these max index values somewhere because we need those values
	# in the next task      
	res_1 = Answering_Q(Q_1, vectorizer, docs_idf)
	res_2 = Answering_Q(Q_2, vectorizer, docs_idf)
	return (res_1, res_2)
