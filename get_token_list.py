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
    preresults = {} #Dictionary containing results for each individual term different from AND, OR, NOT
    for item in query_list:
        if item not in ["AND", "OR", "NOT"]:
            if item in index.keys():
                preresults[item] = index[item].keys()
            else:
                preresults[item] = [] #If the word is not in index, we state that no document are relevant for it
    return preresults


def evaluate_single_expression(preresults, single_expr, index):
    all_docs = docs_in_index(index)
    for item in single_expr:
        if item in ["AND", "OR", "NOT"]:
            if single_expr.index(item) > 0:
                if single_expr[single_expr.index(item)-1] in ["AND", "OR"]:
                    previous_word = single_expr[single_expr.index(item) - 2]
                else:
                    previous_word = single_expr[single_expr.index(item) - 1]
                a = preresults[previous_word]
            if single_expr[single_expr.index(item)+1] == "NOT":
                next_word = single_expr[single_expr.index(item) + 2]
            else:
                next_word = single_expr[single_expr.index(item) + 1]
            b = preresults[next_word]
            if item == "AND" and next_word != "NOT":
                results = intersect(a, b)
            elif item == "OR" and next_word != "NOT":
                results = unite(a, b)
            elif item == "AND" and next_word == "NOT":
                next_word = single_expr[single_expr.index(item) + 2]
                b = preresults[next_word]
                results = remove_in_list(a, b)
            elif item == "OR" and next_word == "NOT":
                next_word = single_expr[single_expr.index(item) + 2]
                b = preresults[next_word]
                temp = remove_in_list(all_docs, b)
                results = unite(a, temp)
            elif item == "NOT" and (single_expr.index(item) == 0 or previous_word not in ["AND", "OR"]):
                results = remove_in_list(all_docs, b)
    return results

def evaluate_multiple_expressions(preresults, expr, index):
    while len(expr) > 1:

        # We build a single expression
        l = []
        i = 0
        while not is_single_exp(l):
            l = l + [expr[i]]
            i += 1
            if i > len(expr):
                print("Erreur dans la formation d'expressions unitaires")
                break

        # We evaluate the single expression and get temporary results
        temporary_results = evaluate_single_expression(preresults, l, index)

        # We now replace the original expression in preresults (which is a dictionary) with a new single key
        # so we can then work on new terms next to original expression
        new = l[0]
        for i in (1, len(l) - 1):
            if i > 0:
                new = new + " " + l[i]  # constructing string linked to the expression
        preresults[new] = temporary_results  # adding said string
        for item in l:
            if item not in ["AND", "OR", "NOT"]:
                preresults = remove_key(preresults, item)  # removing old keys

        # We do the same to the multiple expression list to take into account the evaluation we did in the next loop
        for item in l:
            if item not in ["AND", "OR", "NOT"]:
                expr = remove_in_list(expr, [item])
        expr = [new] + expr
        expr = remove_duplicates(expr)

    return temporary_results


def parentheses_priority(str):
    """recursive function returning the string 'most surrounded'
    by parentheses which will be treated first later"""
    if ("(" not in str) and (")" not in str):
        return str
    else:
        s = str[str.find("(") + 1:str.rfind(")")]
        return parentheses_priority(s)


def boolean_search(index, query):
    preresults = individual_results(index, query)
    
    #We want to treat expressions according to the priority indicated by parentheses
    s = parentheses_priority(query)
    temp = split_query(s)

    while 1:

        s = parentheses_priority(query)

        #We handle an expression WITHOUT parentheses
        temporary_results = evaluate_multiple_expressions(preresults, temp, index)

        if s == query:
            break #Implementation of "else" still needed

    final_results = list(set(temporary_results))

    print(str(len(final_results)) + " publications correspondent à votre recherche : ")
    k = 1
    for i in final_results:
        print("\t" + str(k) + "\t Publication n°" + str(i))
        k += 1
    return final_results

