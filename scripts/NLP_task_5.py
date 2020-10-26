
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from matplotlib import pyplot
import numpy

# Calculates frequency of 1 000 the most common words and creates index vector
def calculate_freq_rank(corpus_root, text_file):
    
    wordlist = PlaintextCorpusReader(corpus_root, text_file)

    # This will take about 1 hour to run
    fdist_words = FreqDist(wordlist.words(text_file))

    # 30 most common words and their frequency as a tuple
    fdist_words_1000 = fdist_words.most_common(1000)
  
    # Selects only the words from the tuple
    words_1000 = [i[0] for i in fdist_words_1000]
  
    # Selects only the counts from the tuple
    counts_1000 = [i[1] for i in fdist_words_1000]

    word_len = len(words_1000)
  
    # Index vector from 1 to number of distinct words
    index = list(range(1, word_len + 1))  
    
    return index, counts_1000
   
# Plots a Zipf's Law    
def zipf_law(index, counts):
    pyplot.plot(index, counts)
    pyplot.ylabel('Frequency')
    pyplot.xlabel('Rank')
    pyplot.title('Term frequency vs. rank ')
 
# Plots a Zipf's Law on log-log-scale   
def zipf_law_loglog(index, counts):
    pyplot.plot(numpy.log10(index), numpy.log10(counts))  
    pyplot.ylabel('log(Frequency)')
    pyplot.xlabel('log(Rank)')
    pyplot.title('log(frequency) vs. log(rank)')
    
corpus_root = 'C:/Users/Aapo' # Change this
text_file_1 = 'capitalismversuscommunism_final.txt'
    
index_1, counts_1000_1 = calculate_freq_rank(corpus_root, text_file_1)

# Fitting Zipf's law
zipf_law(index_1, counts_1000_1)
    
# Fitting Zipf's law on log-log scale
zipf_law_loglog(index_1, counts_1000_1)


# Repeat the same for the other document

text_file_2 = 'file.txt'

index_2, counts_1000_2 = calculate_freq_rank(corpus_root, text_file_2)

# Fitting Zipf's law
zipf_law(index_2, counts_1000_2)
    
# Fitting Zipf's law on log-log scale
zipf_law_loglog(index_2, counts_1000_2)