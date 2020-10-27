from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from numpy import arange
from matplotlib import pyplot

# Task 1

corpus_root = 'C:/Users/Aapo' # Change this
wordlist = PlaintextCorpusReader(corpus_root, 'wiki.txt')

# This will take about 1 hour to run
fdist_words = FreqDist(wordlist.words('wiki.txt'))
  
# 30 most common words and their frequency as a tuple
fdist_words_30 = fdist_words.most_common(30)
  
# Selects only the words from the tuple
words_30 = [i[0] for i in fdist_words_30]
  
# Selects only the counts from the tuple
counts_30 = [i[1] for i in fdist_words_30]
    
# Function for the bar chart 
def bar_chart_million(words, counts):
    ind = arange(len(words))
    for c in range(len(words)):
        bars = pyplot.bar(ind, [element / 1000000 for element in counts], 
                          color='b')
    pyplot.xticks(ind, words, rotation = 90)
    pyplot.ylabel('Frequency (million)')
    pyplot.title('Frequency of 30 most common words')
 
bar_chart_million(words_30, counts_30) 

