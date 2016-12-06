import os
import matplotlib.pyplot as plt
from useful_functions import *
from math import log

global_directory = "CS276/pa1-data/"

"""
    First functions are about going through the collection, counting the vocabulary and the word frequency.
"""


def count_tokens_and_vocabulary_in_dir(i, vocabulary, token_count):
    for filename in os.listdir(global_directory + str(i)):
        words = open(global_directory + str(i) + '/' + filename).readline()
        tokens = custom_tokenize(words)
        token_count += len(tokens)
        for word in lower_and_remove_common(tokens):
            if not vocabulary.get(word):
                vocabulary[word] = 1
            else:
                vocabulary[word] += 1
    return {'voc': vocabulary, 'count': token_count}


def count_tokens_and_vocabulary():
    vocabulary = {}
    token_count = 0
    for i in range(0, 5):
        result = count_tokens_and_vocabulary_in_dir(i, vocabulary, token_count)
        vocabulary = result['voc']
        token_count = result['count']
    print("This collection has " + str(token_count) + " tokens at half-collection (5 first directories).")
    print("Its vocabulary is made of " + str(len(vocabulary)) + " words at half-collection.")
    for i in range(5, 10):
        result = count_tokens_and_vocabulary_in_dir(i, vocabulary, token_count)
        vocabulary = result['voc']
        token_count = result['count']
    print("This collection has " + str(token_count) + " tokens.")
    print("Its vocabulary is made of " + str(len(vocabulary)) + " words.")
    return vocabulary

"""
    From the generated vocabulary, these functions get the word ranking by frequency and print a rank vs frequency plot.
"""


def get_voc_freq_rank(vocabulary):
    voc_freq_rank_cs76 = {}
    ranking = 1
    for item in sorted(vocabulary.items(), key=second, reverse=True):
        voc_freq_rank_cs76[item[0]] = (item[1], ranking)
        ranking += 1
    return voc_freq_rank_cs76


def show_plot_freq_rank(voc_freq_rank):
    sorted_items = sorted(voc_freq_rank.values(), key=second)
    array_freq = [item[0] for item in sorted_items]
    array_rank = [item[1] for item in sorted_items]
    plt.plot(array_rank, array_freq)
    plt.xlabel('Word rank')
    plt.ylabel('Word frequency')
    #plt.axis([0, 250000, 0, 365000])
    plt.show()


def show_plot_log_freq_rank(voc_freq_rank):
    sorted_items = sorted(voc_freq_rank.values(), key=second)
    array_freq = [log(item[0]) for item in sorted_items]
    array_rank = [log(item[1]) for item in sorted_items]
    plt.plot(array_rank, array_freq, 'bo')
    plt.xlabel('Word rank (log)')
    plt.ylabel('Word frequency (log)')
    plt.show()


"""
    Below is the main method for execution
"""


def main():
    vocabulary_cs76 = count_tokens_and_vocabulary()

    # This collection has 13611296 tokens at half-collection (5 first directories).
    # Its vocabulary is made of 150733 words at half-collection.
    # This collection has 23912191 tokens.
    # Its vocabulary is made of 244580 words.

    voc_freq_rank_cs76 = get_voc_freq_rank(vocabulary_cs76)

    show_plot_freq_rank(voc_freq_rank_cs76)
    show_plot_log_freq_rank(voc_freq_rank_cs76)


if __name__ == '__main__':
    main()
