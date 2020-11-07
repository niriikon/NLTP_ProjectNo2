import os
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from numpy import arange
#from matplotlib import pyplot
from matplotlib import figure

# Stays running -> use figure.Figure

# Task 1
#os.path.join('path', 'to', 'directory')

if __name__ == '__main__':
    main(os.path.join('..', '..', 'corpus'), 'small.txt')

def main(path, dataset):
    #corpus_root = 'C:/Users/Aapo' # Change this
    wordlist = PlaintextCorpusReader(path, dataset)

    # This will take about 1 hour to run
    fdist_words = FreqDist(wordlist.words(dataset))
      
    # 30 most common words and their frequency as a tuple
    fdist_words_30 = fdist_words.most_common(30)
      
    # Selects only the words from the tuple
    words_30 = [i[0] for i in fdist_words_30]
      
    # Selects only the counts from the tuple
    counts_30 = [i[1] for i in fdist_words_30]


    # Function for the bar chart 
    def bar_chart_million(words, counts):
        fig = figure.Figure()
        ax = fig.add_subplot(111)
        ind = arange(len(words))
        for c in range(len(words)):
            bars = ax.bar(ind, [element / 1000000 for element in counts], color='b')
        #ax.set_xticks(ind, words, rotation = 90)
        ax.set_xticks(ind)
        ax.set_xticklabels(words, rotation=90)
        ax.set(ylabel='Frequency (million)')
        ax.set_title('Frequency of 30 most common words')

        return fig
     
    return bar_chart_million(words_30, counts_30)

