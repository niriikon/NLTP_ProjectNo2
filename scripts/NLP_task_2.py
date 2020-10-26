from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from numpy import arange
from matplotlib import pyplot
import numpy


corpus_root = 'C:/Users/Aapo' # Change this
wordlist = PlaintextCorpusReader(corpus_root, 'wiki.txt')

# This will take about 1 hour to run
fdist_words = FreqDist(wordlist.words('wiki.txt'))


# Number of distinct words in the corpus
words_distinct = [i[0] for i in fdist_words]

word_len = len(words_distinct)
  
# Index vector from 1 to number of distinct words
index = list(range(1, word_len + 1))  
  
word_freq = [i[1] for i in fdist_words.most_common()]
  
# Fitting Zipf's law
pyplot.plot([element / 1000000 for element in index], 
            [element / 1000000 for element in word_freq])
pyplot.ylabel('Frequency (million)')
pyplot.xlabel('Rank (million)')
pyplot.title('Term frequency vs. rank ')
 
# Fitting Zipf's law on log-log scale
pyplot.plot(numpy.log10(index), numpy.log10(word_freq))  
pyplot.ylabel('log(Frequency)')
pyplot.xlabel('log(Rank)')
pyplot.title('log(frequency) vs. log(rank)')