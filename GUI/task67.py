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
    txt1 = wordlist_t1.words(text_f1)
    txt2 = wordlist_t2.words(text_f2)

    fdist_text1 = FreqDist(txt1)
    fdist_text2 = FreqDist(txt2)
    fdist_text1.pprint(maxlen = 30)
    fdist_text2.pprint(maxlen = 30)

    def my_counter(numerator, nominator, freq_lower,freq_upper):
        words_in_numerator = set(list(filter(lambda x: x[1] >= freq_lower and x[1] <= freq_upper,numerator.items())))
        words_in_nominator = set(list(filter(lambda x: x[1] >= freq_lower and x[1] <= freq_upper,nominator.items())))
        output_r1 = [tuple(j for j in i if not isinstance(j, int)) for i in words_in_numerator]
        output_r2 = [tuple(j for j in i if not isinstance(j, int)) for i in words_in_nominator]
        intersect_of_words = set(output_r1) & set(output_r2)
        try:
            result = len(words_in_numerator)/len(intersect_of_words)
        except ZeroDivisionError:
            result = len(words_in_numerator) / 0.0000000001

        return(result)

    #by changing the freq value, we get words for freq > value
    #by changing the numerator and nominator we get R1(i) and R2(i)
    #have to use small freqs for this example, small data set
    R1_1 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq_lower = 50, freq_upper = 1000) 
    R2_1 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq_lower = 50, freq_upper = 1000)

    R1_2 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq_lower = 10, freq_upper = 49)
    R2_2 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq_lower = 10, freq_upper = 49)

    R1_3 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq_lower = 5, freq_upper = 9)
    R2_3 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq_lower = 5, freq_upper = 9)

    R1_4 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq_lower = 2, freq_upper = 4)
    R2_4 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq_lower = 2, freq_upper = 4)

    R1_5 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq_lower = 0, freq_upper = 1)
    R2_5 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq_lower = 0, freq_upper = 1)

    #R1_6 = my_counter(numerator = fdist_text1,nominator = fdist_text2 ,freq_lower = 10, freq_upper = 11)
    #R2_6 = my_counter(numerator = fdist_text2,nominator = fdist_text1 ,freq_lower = 10, freq_upper = 11)

    #etc. maby loop throgh function to save from copy/pasting
    print([R1_1,R1_2,R1_3,R1_4,R1_5,R2_1,R2_2,R2_3,R2_4,R1_5])

    fig = figure.Figure()
    ax = [fig.add_subplot(211), fig.add_subplot(212)]
    ax[0].plot([R1_1,R1_2,R1_3,R1_4,R1_5],'r', label = "R1") #and something like this
    ax[1].plot([R2_1,R2_2,R2_3,R2_4,R1_5],'b', label = "R2")

    #ax.legend(loc = "upper right")
    ax[0].set(xlabel="index", ylabel="proportion of words")
    ax[1].set(xlabel="index", ylabel="proportion of words")
    ax[0].set_xticks([0, 1, 2, 3, 4])
    ax[0].set_xticklabels(['0', '1', '2', '3', '4'])
    ax[1].set_xticks([0, 1, 2, 3, 4])
    ax[1].set_xticklabels(['0', '1', '2', '3', '4'])
    
    #plt.xticks([0,1,2,3,4])
    #plt.show()
    ax[0].legend()
    ax[1].legend()
    fig.subplots_adjust(hspace=0.8)

    return (jd_texts, fig)
