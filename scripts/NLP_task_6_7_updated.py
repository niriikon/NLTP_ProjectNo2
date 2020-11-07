import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
import matplotlib.pyplot as plt

text_f1 = 'communism_final_1000.txt' #need to change these to actual files
text_f2 = 'capitalism_final_1000.txt'
path = r'C:/Users/Käyttäjä/Desktop/Python38/' #change this
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
#ttxt1 = nltk.word_tokenize(txt1)
#ttxt2 = nltk.word_tokenize(txt2)

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
    result = len(words_in_numerator)/len(intersect_of_words)
    return(result)


#by changing the freq upper and lower value, we get words for freq > value_lower and freq < value_upper
#by changing the numerator and nominator we get R1(i) and R2(i)

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



#etc. maeby loop throgh function to save from copy/pasting
print([R1_1,R1_2,R1_3,R1_4,R1_5,R2_1,R2_2,R2_3,R2_4,R1_5])

plt.plot([R1_1,R1_2,R1_3,R1_4,R1_5],'r',[R2_1,R2_2,R2_3,R2_4,R1_5],'b')
plt.xlabel("index")
plt.ylabel("proportion of words")
plt.xticks([0,1,2,3,4])
plt.show()
#,R1_4,R1_5,R1_6,R1_7,R1_8,R1_9
#,R2_4,R2_5,R2_6,R2_7,R2_8,R2_9
