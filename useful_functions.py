import nltk
from math import *

common_words_file = open('CACM/common_words')
common_words = {}
for line in common_words_file:
    common_words[line.rstrip('\n')] = 1
common_words_file.close()


def lower_and_remove_common(word_list):
    token_list = []
    for word in word_list:
        if not common_words.get(word):
            token_list.append(word.lower())
    return token_list


def custom_tokenize(entry_string):
    tokenizer = nltk.tokenize.RegexpTokenizer('[a-zA-Z]+')
    return tokenizer.tokenize(entry_string)

def get_b(T, T_prime, M, M_prime):
    b = log(M_prime / M) / log(T_prime / T)
    return b

def get_k(T, M, b):
    k = M/(T**b)
    return k


