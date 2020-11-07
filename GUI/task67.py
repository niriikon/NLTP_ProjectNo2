import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
#import matplotlib.pyplot as plt  -- Stays running if using TkAgg
from matplotlib import figure
from os.path import join as os_join

if __name__ == '__main__':
	main(os_join('..', '..', 'corpus'), 'communism.txt', 'capitalism.txt')

def main(path, text_f1, text_f2):
	#text_f1 = 'scientificartistic_final.txt' #need to change these to actual files
	#text_f2 = 'dogscats_final.txt'
	#path = r'C:/Users/Käyttäjä/Desktop/Python38/' #change this
	
	#read the two text files and extract all words
	#set takes out duplicates and is needed for jaccardian distance

	wordlist_t1 = PlaintextCorpusReader(path, text_f1)
	wordlist_t2 = PlaintextCorpusReader(path, text_f2)
	text1_words = set(wordlist_t1.words(text_f1))
	text2_words = set(wordlist_t2.words(text_f2))

	#Task 6 calculate jaccardian distance
	jd_texts = nltk.jaccard_distance(text1_words,text2_words)
	print(jd_texts, 'Jaccard distance between text1 and text2')

	#Task 7
	#Need word frequencies
	fdist_text1 = FreqDist(wordlist_t1.words(text_f1))
	fdist_text2 = FreqDist(wordlist_t2.words(text_f2))


	def my_counter(numerator, nominator, freq):
	    words_in_numerator = set(list(filter(lambda x: x[1] >= freq,numerator.items())))
	    words_in_nominator = set(list(filter(lambda x: x[1] >= freq,nominator.items())))
	    intersect_of_words = words_in_numerator & words_in_nominator
	    #print(intersect_of_words)
	    try:
	    	result = len(words_in_numerator)/len(intersect_of_words)
	    except ZeroDivisionError:
	    	result = len(words_in_numerator)
	    
	    return result

	#by changing the freq value, we get words for freq > value
	#by changing the numerator and nominator we get R1(i) and R2(i)
	#have to use small freqs for this example, small data set
	R1_1 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq = 1) 
	R2_1 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq = 1)

	R1_2 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq = 2)
	R2_2 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq = 2)

	#R1_3 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq = 3)
	#R2_3 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq = 3)

	#etc. maby loop throgh function to save from copy/pasting
	print([R1_1,R2_1,R1_2,R2_2])

	fig = figure.Figure()
	ax = fig.add_subplot(111)
	ax.plot([R1_1,R1_2],'r',[R2_1,R2_2],'b') #and something like this

	return (jd_texts, fig)
