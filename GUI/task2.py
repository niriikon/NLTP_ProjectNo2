from os.path import join as os_join
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from numpy import arange
#from matplotlib import pyplot
from matplotlib import figure
import numpy

# Stays running, use figure.Figure

if __name__ == '__main__':
    main(os_join('..', '..', 'corpus'), 'small.txt')

def main(path, dataset):
    #corpus_root = 'C:/Users/Aapo' # Change this
    wordlist = PlaintextCorpusReader(path, dataset)

    # This will take about 1 hour to run
    fdist_words = FreqDist(wordlist.words(dataset))


    # Number of distinct words in the corpus
    words_distinct = [i[0] for i in fdist_words]

    word_len = len(words_distinct)
      
    # Index vector from 1 to number of distinct words
    index = list(range(1, word_len + 1))  
      
    word_freq = [i[1] for i in fdist_words.most_common()]
    
    #fig = pyplot.figure()
    fig = figure.Figure()
    ax = [fig.add_subplot(211), fig.add_subplot(212)]

    # Fitting Zipf's law
    ax[0].plot([element / 1000000 for element in index], [element / 1000000 for element in word_freq])
    ax[0].set(ylabel='Frequency (million)')
    ax[0].set(xlabel='Rank (million)')
    ax[0].set_title('Term frequency vs. rank ')
     
    # Fitting Zipf's law on log-log scale
    ax[1].plot(numpy.log10(index), numpy.log10(word_freq))  
    ax[1].set(ylabel='log(Frequency)')
    ax[1].set(xlabel='log(Rank)')
    ax[1].set_title('log(frequency) vs. log(rank)')
    fig.subplots_adjust(hspace=0.8)

    return fig
