from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from matplotlib import pyplot
import numpy
import scipy


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


def getPairStats(x, y):
    
    #calculate means
    x_bar = numpy.mean(x)
    y_bar = numpy.mean(y)
    #get number of entries
    n = len(x)
    
    #calculate sums
    x_sum = numpy.sum(x)
    x_sum_square = numpy.sum([xi**2 for xi in x])
    y_sum = numpy.sum(y)
    y_sum_square = numpy.sum([yi**2 for yi in y])
    xy_sum = numpy.sum([xi*yi for xi, yi in zip(x, y)])
    
    #calculcate remainder of equations
    s_xx  = x_sum_square - (1/n)*(x_sum**2)
    s_yy = y_sum_square - (1/n)*(y_sum**2)
    s_xy = xy_sum - (1/n)*x_sum*y_sum
    
    return s_xx, s_yy, s_xy  

# Fitting linear regression
def pair_regression(x, y):
    
    #calculate means
    x_bar = numpy.mean(x)
    y_bar = numpy.mean(y)
    #get number of entries
    n = len(x)
    
    #get stats
    s_xx, s_yy, s_xy = getPairStats(x, y)
    
    #calculcate coefficients
    beta_hat = s_xy / s_xx
    alpa_hat = y_bar - beta_hat * x_bar
    
    return alpa_hat, beta_hat

alpha, beta = pair_regression(numpy.log10(index), numpy.log10(word_freq))

# Run these at the same time and you get Zipf's law curve and fitting from
# the linear regression on the same plot
pyplot.plot(numpy.log10(index), numpy.log10(word_freq))  
pyplot.plot(numpy.log10(index), (beta*numpy.log10(index)) + alpha)
pyplot.xlabel('log(Rank)')
pyplot.ylabel('log(Frequency')
pyplot.title("Zipf's Law curve and fit from linear regression")


# Confidence intervals
def simple_regression_conf(x, y, alpha=0.05):
    
    n = len(x)
    #calculate stats
    s_xx, s_yy, s_xy = getPairStats(x, y)
    
    #get regression coefficients
    alpha_hat, beta_hat = pair_regression(x, y)
    
    #maximim likelihood estimator
    sigma_hat = numpy.sqrt((1/n)*(s_yy-beta_hat*s_xy))
    
    #calculcate t statistic
    t_limit = scipy.stats.t.ppf(1-alpha/2, n-2)
    #interval term
    interval_val = t_limit*sigma_hat*numpy.sqrt(n/((n-2)*s_xx))
    
    #calculcate intervals
    beta_upper = beta_hat + interval_val
    beta_lower = beta_hat - interval_val
    
    return beta_lower, beta_upper

beta_low_95, beta_up_95 = simple_regression_conf(numpy.log10(index), numpy.log10(word_freq))
beta_low_90, beta_up_90 = simple_regression_conf(numpy.log10(index), numpy.log10(word_freq), alpha = 0.1)
beta_low_80, beta_up_80 = simple_regression_conf(numpy.log10(index), numpy.log10(word_freq), alpha = 0.2)

pyplot.plot(numpy.log10(index), numpy.log10(word_freq))  
pyplot.plot(numpy.log10(index), (beta*numpy.log10(index)) + alpha)

pyplot.plot(numpy.log10(index), numpy.log10(word_freq))  
pyplot.plot(numpy.log10(index), (beta*numpy.log10(index)) + alpha, label = 'OLS Fit', color='orange')
pyplot.plot(numpy.log10(index), (beta_low_95*numpy.log10(index)) + (alpha+beta_low_95), label = 'Lower 95% conf', color='green')
pyplot.plot(numpy.log10(index), (beta_up_95*numpy.log10(index)) + (alpha-beta_up_95), label = 'Upper 95% conf', color='red')
#pyplot.plot(numpy.log10(index), (beta_low_90*numpy.log10(index)) + (alpha+beta_low_90), label = 'Lower 90% conf', color='blue')
#pyplot.plot(numpy.log10(index), (beta_up_90*numpy.log10(index)) + (alpha-beta_up_90), label = 'Upper 90% conf', color='grey')
#pyplot.plot(numpy.log10(index), (beta_low_80*numpy.log10(index)) + (alpha+beta_low_80), label = 'Lower 80% conf', color='purple')
#pyplot.plot(numpy.log10(index), (beta_up_80*numpy.log10(index)) + (alpha-beta_up_80), label = 'Upper 80% conf', color='yellow')
pyplot.legend()

pyplot.show()

# Here we calculate lists that we need when we try to identify how many
# points are between the upper and the lower confidence interval.
freq_log = numpy.log10(word_freq)
low_limit_95 = (beta_low_95*numpy.log10(index) + (alpha+beta_low_95))
up_limit_95 = (beta_up_95*numpy.log10(index) + (alpha-beta_up_95))

low_limit_90 = (beta_low_90*numpy.log10(index) + (alpha+beta_low_90))
up_limit_90 = (beta_up_90*numpy.log10(index) + (alpha-beta_up_90))

low_limit_80 = (beta_low_80*numpy.log10(index) + (alpha+beta_low_80))
up_limit_80 = (beta_up_80*numpy.log10(index) + (alpha-beta_up_80))

i = 0
count = 0

# Counts how many points lies between upper and lower limit
for x in freq_log:
    if x <= up_limit_95[i] and x >= low_limit_95[i]:
        count = count
        i = i + 1
    else: 
        count = count + 1
        i = i + 1

count