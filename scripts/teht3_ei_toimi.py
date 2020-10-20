from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from numpy import arange
import matplotlib.pyplot as plt
import numpy
import scipy
from collections import Counter
corpus_root = r'C:\Users'
wordlist = PlaintextCorpusReader(corpus_root, 'wiki_en1.txt')
fdist_words = FreqDist(wordlist.words('wiki_en1.txt'))
words_distinct = [i[0] for i in fdist_words]
word_len = len(words_distinct)
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

alpha_hat, beta_hat = pair_regression(x=numpy.log10(index), y=numpy.log10(word_freq))
print("The vertical axis intercept alpha hat is equal to: {}".format(alpha_hat))
print("The slope beta hat is equal to: {}".format(beta_hat))

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

beta_lower_05, beta_upper_05 = simple_regression_conf(x=numpy.log10(index), y=numpy.log10(word_freq), alpha=0.05)
beta_lower_10, beta_upper_10 = simple_regression_conf(x=numpy.log10(index), y=numpy.log10(word_freq), alpha=0.1)
beta_lower_20, beta_upper_20 = simple_regression_conf(x=numpy.log10(index), y=numpy.log10(word_freq), alpha=0.2)

print("beta_lower at 95% conf: {:.4f}".format(beta_lower_05))
print("beta_upperat 95% conf: {:.4f}".format(beta_upper_05))

print("beta_lower at 90% conf: {:.4f}".format(beta_lower_10))
print("beta_upperat 90% conf: {:.4f}".format(beta_upper_10))

print("beta_lower at 80% conf: {:.4f}".format(beta_lower_20))
print("beta_upperat 80% conf: {:.4f}".format(beta_upper_20))

y_pred = [alpha_hat + beta_hat*xi for xi in numpy.log10(index)]
y_upper_05 = [alpha_hat + beta_upper_05*xi for xi in numpy.log10(index)]
y_lower_05 = [alpha_hat + beta_lower_05*xi for xi in numpy.log10(index)]

y_upper_10 = [alpha_hat + beta_upper_10*xi for xi in numpy.log10(index)]
y_lower_10 = [alpha_hat + beta_lower_10*xi for xi in numpy.log10(index)]

y_upper_20 = [alpha_hat + beta_upper_20*xi for xi in numpy.log10(index)]
y_lower_20 = [alpha_hat + beta_lower_20*xi for xi in numpy.log10(index)]

plt.scatter(x=numpy.log10(index), y=numpy.log10(word_freq), label = 'Data')
plt.plot(numpy.log10(index), y_pred, label = 'OLS Fit', color='orange')
plt.plot(numpy.log10(index), y_upper_05, label = 'Upper prediction, 95% conf', color='red')
plt.plot(numpy.log10(index), y_lower_05, label = 'Lower Prediction 95% conf', color='green')
plt.plot(numpy.log10(index), y_upper_10, label = 'Upper prediction 90% conf', color='blue')
plt.plot(numpy.log10(index), y_lower_10, label = 'Lower Prediction 90% conf', color='grey')
plt.plot(numpy.log10(index), y_upper_20, label = 'Upper prediction 80% conf', color='purple')
plt.plot(numpy.log10(index), y_lower_20, label = 'Lower Prediction 80% conf', color='yellow')

plt.legend()


plt.show()



