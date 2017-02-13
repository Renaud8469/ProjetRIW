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
    """Returns the list of a ∩ b"""
    return [val for val in a if val in b]


def unite(a, b):
    """Returns the list of a ∪ b"""
    return list(set().union(a,b))


def remove_in_list(a, b):
    """Returns the list of a \ b
    a is the original list and b is the
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
        if l[1] in ["AND", "OR"] and l[2] != "NOT":
            return True
    elif len(l) == 4:
        if l[1] in ["AND", "OR"] and l[2] == "NOT":
            return True
    else:
        return False


def remove_key(d, key):
    """Properly removes key from dictionary following
    immutability principle"""
    r = dict(d)
    del r[key]
    return r


def remove_duplicates(l):
    """Removes duplicates in case there are two boolean
    operators AND or OR following each other"""
    seq = ["AND", "OR"]
    for i in range(0, len(l)-2):
        if (l[i] in seq) and (l[i+1] in seq):
            del l[i]
    if l[len(l)-1] in seq:
        del l[len(l)-1]
    return l


def split_query(str):
    """Returns a list where each element is a word from the str argument
    Parentheses are removed if there are some"""
    return str.replace("(", "").replace(")", "").split()


def split_query_with_p(str):
    """Returns a list where each element is either a word or a block
    surrounded by parentheses if there are some
    e.g. input : 'harvard OR (program AND computer) OR (paris AND ECP)'
    output : ['harvard', 'OR', 'program AND computer', 'OR', 'paris AND ECP']"""
    s = str.split()
    to_delete = 0
    i = -1
    l = []
    for el in s:
        if "(" in el:
            to_delete += el.count("(")
        elif ")" in el:
            to_delete -= el.count(")")
            i += el.count(")")
            if to_delete == 0:
                l = l + [parentheses_blocks(str)[i]]
        elif to_delete == 0:
            l = l + [el]
    return l


def parentheses_priority(query):
    """Recursive function returning the string 'most surrounded'
    by parentheses which will be treated first later
    NB: this function is not used anymore in boolean_search.py"""
    if ("(" not in query) and (")" not in query):
        return query
    else:
        s = query[query.find("(") + 1:query.rfind(")")]
        return parentheses_priority(s)


def trimming(query):
    """Gets rid of what is outside of the 'largest' parentheses block
    e.g. input : 'harvard AND (computer OR (program AND software))'
    output : 'computer OR (program AND software)'
    NB: if there are several blocks at the same level, the first one is returned"""
    if "(" not in query:
        return query
    else:
        i = 0
        while query[i] != "(":
            i += 1
        first_pos = i+1
        i += 1
        j = 0
        k = i
        for c in query[i:]:
            k += 1
            if c == "(":
                j += 1
            elif c == ")":
                j -= 1
                if j == -1:
                    last_pos = k-1
                    break
        return query[first_pos:last_pos], last_pos


def parentheses_blocks(query):
    """Function identifying the different blocks surrounded by parentheses
    to have a proper order of priority. We go from the blocks the most inside
    and work our way to the 'largest' block"""
    blocks = []
    s = query
    n = 0
    if query[0] != "(":
        blocks = blocks + [query]
    for c in query:
        if c == "(":
            n += 1
    for i in range(n):
        new = trimming(s)[0]
        last_pos_new = trimming(s)[1]
        blocks = blocks + [new]
        if trimming(new) == new:
            s = s[last_pos_new+1:]
        else:
            s = new
    list_final = list(reversed(blocks))
    if blocks[0] != query:
        list_final = list_final + [query]
    return list_final


def cheap_graph(nb_docs_max, tot_p, tot_r):
    print("nb_docs\t* : Précision | ~ : Rappel")
    for i in range(nb_docs_max):
        x = int(tot_p[i] * 100)
        y = int(tot_r[i] * 100)
        p_g = ""
        r_g = ""
        for j in range(x):
            p_g += "*"
        for k in range(y):
            r_g += "~"
        print(str(i + 1) + " - \t" + p_g)
        print(str(i + 1) + " - \t" + r_g)


def get_docs(file):
    docs = []
    for line in file:
        docs.append(int(line))
    return docs
