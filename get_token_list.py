import nltk
from useful_functions import *


def get_id(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


def get_token_list(file):
    token_list = []
    latest_mark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if (".T" in latest_mark) or (".W" in latest_mark) or (".K" in latest_mark):
            if len(line) > 3:
                current_tokens = custom_tokenize(line)
                token_list = token_list + current_tokens
    return token_list

def get_token_list_half(file):
    token_list = []
    latest_mark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if (".T" in latest_mark) or (".W" in latest_mark) or (".K" in latest_mark):
            if len(line) > 3:
                current_tokens = custom_tokenize(line)
                token_list = token_list + current_tokens
        if id_paper >= 1602:
            print(id_paper)
            break
    return token_list

#Optimized function
def get_vocabulary_dict(file):
    token_dict = {}
    token_number = 0
    latest_mark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if (".T" in latest_mark) or (".W" in latest_mark) or (".K" in latest_mark):
            if len(line) > 3:
                total_tokens = custom_tokenize(line)
                current_tokens = lower_and_remove_common(custom_tokenize(line))
                token_number =+ len(total_tokens)
                for token in current_tokens:
                    word = token
                    if word in token_dict:
                        token_dict[word] += 1
                    else:
                        token_dict[word] = 1
    return token_dict, token_number

def get_reverse_index(vocabulary, file):
    reverse_index = {}
    for key in vocabulary.keys():
        reverse_index[key] = {}
    file.seek(0)
    latest_mark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (
            ".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if (".T" in latest_mark) or (".W" in latest_mark) or (".K" in latest_mark):
            if len(line) > 3:
                current_tokens = lower_and_remove_common(custom_tokenize(line))
                for token in current_tokens:
                    if id_paper in reverse_index[token].keys():
                        reverse_index[token][id_paper] += 1
                    else:
                        reverse_index[token][id_paper] = 1
    return reverse_index

def split_query(str):
    return str.replace("(", "").replace(")", "").split()

def individual_results(index, query):
    query_list = split_query(query)
    preresults = {} #dictionary containing results for each individual term different from AND, OR, NOT
    for item in query_list:
        if item not in ["AND", "OR", "NOT"]:
            if item in index.keys():
                preresults[item] = index[item].keys()
    return preresults

def evaluate_single_expression(index, query_list):
    all_docs = docs_in_index(index)
    for item in query_list:
        if item in ["AND", "OR", "NOT"]:
            if query_list.index(item) > 0:
                previous_word = query_list[query_list.index(item)-1]
                a = index[previous_word].keys()
            next_word = query_list[query_list.index(item)+1]
            b = index[next_word].keys()
            if item == "AND" and next_word != "NOT":
                results = intersect(a, b)
            elif item == "OR" and next_word != "NOT":
                results = unite(a, b)
            elif item == "AND" and next_word == "NOT":
                next_word = query_list[query_list.index(item) + 2]
                b = index[next_word].keys()
                results = remove_in_list(a, b)
            elif item == "OR" and next_word == "NOT":
                next_word = query_list[query_list.index(item) + 2]
                b = index[next_word].keys()
                temp = remove_in_list(all_docs, b)
                results = unite(a, temp)
            elif item == "NOT" and (query_list.index(item) == 0 or previous_word not in ["AND", "OR"]):
                results == remove_in_list(all_docs, b)
    return results

def parentheses_priority(str):
    """recursive function returning the string 'most surrounded'
    by parentheses which will be treated first later"""
    if ("(" not in str) and (")" not in str):
        return str
    else:
        s = str[str.find("(") + 1:str.rfind(")")]
        return parentheses_priority(s)

def boolean_search(index, query):
    query_list = split_query(query)
    preresults = individual_results(index, query)
    #We want to treat expressions according to the priority indicated by parentheses
    results = evaluate_single_expression(index, query_list)
    return results

