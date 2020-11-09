from nltk.corpus import PlaintextCorpusReader
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from matplotlib import figure as plt
from pandas import DataFrame
from pandas import read_csv
from pandas import merge

if __name__ == '__main__':
    main(path_1, path_2, dataset_1, dataset_2)

def main(path_1, path_2, dataset_1, dataset_2):
    wordlist_1 = PlaintextCorpusReader(path_1, dataset_1)
    wordlist_2 = PlaintextCorpusReader(path_2, dataset_2)

    words_1 = wordlist_1.words(dataset_1)
    words_2 = wordlist_2.words(dataset_2)

    # Version 1 uses the PorterStemmer for standardization
    porter = PorterStemmer()
    words_1_porter = [porter.stem(t) for t in words_1]
    words_2_porter = [porter.stem(t) for t in words_2]

    # Common words
    def Filter_common(list1, list2):
        return [n for n in list1 if any(m in n for m in list2)]

    common_words = Filter_common(words_1_porter, words_2_porter)

    # Distinct words
    words_in_1_not_in_2 = [x for x in words_1_porter if all(y not in x for y in words_2_porter)]
    words_in_2_not_in_1 = [x for x in words_2_porter if all(y not in x for y in words_1_porter)]

    # Create dataframes
    df_common = DataFrame(common_words, columns = ['word'])
    df_in_1_not_2 = DataFrame(words_in_1_not_in_2, columns = ['word'])
    df_in_2_not_1 = DataFrame(words_in_2_not_in_1, columns = ['word'])

    # File which consists words and their categories
    categories = read_csv('inquirerbasic.csv', sep = ";")

    # Lowercases the words
    categories = categories.assign(Entry = categories['Entry'].str.lower())

    # Removes duplicate rows
    categories = categories.drop_duplicates('Entry', keep='first')

    categories = categories[['Entry', 'Othtags']]

    # Left joins categories to common words based on the word. This is basically 
    # same as assigning category for each word. NAN-values are replaced by Noun
    df_common_categ = merge(df_common, categories, 
                  left_on = 'word', right_on = 'Entry', 
                  how = "left").fillna('Noun')

    # Removes duplicate rows
    df_common_categ = df_common_categ.drop_duplicates('word', keep='first')

    # Creates column called Tag based on the first word of Othtags column
    df_common_categ = df_common_categ.assign(Tag = df_common_categ['Othtags'].str.split().str.get(0))

    # Counts the categories
    df_common_categ['Tag'].value_counts()

    # Repeat the same for the remaining dataframes

    df_in1not2_categ = merge(df_in_1_not_2, categories, 
                  left_on = 'word', right_on = 'Entry', 
                  how = "left").fillna('Noun')

    df_in1not2_categ = df_in1not2_categ.drop_duplicates('word', keep='first')

    df_in1not2_categ = df_in1not2_categ.assign(Tag = df_in1not2_categ['Othtags'].str.split().str.get(0))

    df_in1not2_categ['Tag'].value_counts()

    df_in2not1_categ = merge(df_in_2_not_1, categories, 
                  left_on = 'word', right_on = 'Entry', 
                  how = "left").fillna('Noun')

    df_in2not1_categ = df_in2not1_categ.drop_duplicates('word', keep='first')

    df_in2not1_categ = df_in2not1_categ.assign(Tag = df_in2not1_categ['Othtags'].str.split().str.get(0))

    df_in2not1_categ['Tag'].value_counts()

    fig = plt.Figure()
    ax = [fig.add_subplot(131), fig.add_subplot(132), fig.add_subplot(133)]
    df_common_categ.groupby('Tag')['Tag'].agg('count').plot(kind='bar', ax=ax[0])
    ax[0].set_title('V1∩V2')
    df_in1not2_categ.groupby('Tag')['Tag'].agg('count').plot(kind='bar', ax=ax[1])
    ax[1].set_title('V1 but not in V1∩V2')
    df_in2not1_categ.groupby('Tag')['Tag'].agg('count').plot(kind='bar', ax=ax[2])
    ax[2].set_title('V2 but not in V1∩V2')

    return fig
