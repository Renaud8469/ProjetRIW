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


def second(tuple_word_freq):
    return tuple_word_freq[1]


def rank(tuple_word_freq_rank):
    return tuple_word_freq_rank[1][1]


def intersect(a, b):
    return [val for val in a if val in b]


def unite(a, b):
    return list(set().union(a,b))


def remove_in_list(a, b):
    """a is the original list and b is the
    list whose items you want to remove from a
    if there are items in common"""
    final_list = []
    for item in a:
        if item not in b:
            final_list = final_list + [item]
    return final_list


def docs_in_index(index):
    """Returns a list of all documents indexed"""
    docs = []
    for item in index:
        docs = unite(docs, index[item].keys())
    return docs


def is_single_exp(l):
    """Returns True if the query_list is considered to be a single
    expression that can be used by evaluate_single_expression"""
    if len(l) == 2:
        if l[0] == "NOT":
            return True
    elif len(l) == 3:
        if l[1] in ["AND", "OR"]:
            return True
    elif len(l) == 4:
        if l[1] in ["AND", "OR"] and l[2] == "NOT":
            return True
    else:
        return False


def remove_key(d, key):
    r = dict(d)
    del r[key]
    return r


def remove_duplicates(l):
    seq = ["AND", "OR"]
    for i in range(0, len(l)-2):
        if (l[i] in seq) and (l[i+1] in seq):
            del l[i]
            print("duplicat trouvé")
    if l[len(l)-1] in seq:
        del l[len(l)-1]
    return l
