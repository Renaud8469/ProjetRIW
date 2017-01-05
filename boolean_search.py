from useful_functions import *

# Here is the strategy to implement the boolean search model ("divide and conquer" strategy):
# 1. We filter our results with individual results of terms to only work with terms
# relevant to our query and not all of them since that would not be optimized at all
# 2. We handle the query properly, generally by decomposing it in different blocks:
#   - "single_expression" blocks (e.g. 'harvard AND research'), most elementary blocks
#   - "multiple_expressions" blocks (e.g. 'harvard AND research AND program'), next level
#   - parentheses blocks (i.e. surrounded by parentheses) and we go from inside to outside
# 3. Each time we go through these blocks, the temporary results will be adjusted to minimize
# the time taken and to always work with the same structure. Eventually, once we arrived at
# the last block, which is the whole query, we will have all the results required to handle it.


def individual_results(index, query):
    """Returns documents relevant to each term of the query (except boolean operators) according
    to the index provided in arguments"""
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
    """Returns the results of the most elementary block, i.e. a single expression"""
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
    """Returns the results for an expression with more than two terms using the previous function"""
    if len(expr) == 1:
        temporary_results = preresults[expr[0]]
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
        new = []
        for el in l:
            if el == l[0]:
                new = el
            else:
                new = new + " " + el  # constructing string linked to the expression
        preresults[new] = temporary_results  # adding said string
        for item in l:
            if item not in ["AND", "OR", "NOT"]:
                preresults = remove_key(preresults, item)  # removing old keys

        # We do the same to the multiple expression list to take into account the evaluation we did in the next loop
        for item in l:
            if item not in ["AND", "OR"]:
                expr = remove_in_list(expr, [item])
            if item == "NOT":
                expr = remove_in_list(expr, [item])
        expr = [new] + expr
        expr = remove_duplicates(expr)

    return temporary_results


def boolean_search(index, query):
    """Returns the documents relevant to a query according to an index provided in argument"""
    preresults = individual_results(index, query)

    #We want to treat expressions according to the priority indicated by parentheses
    blocks = parentheses_blocks(query)
    for expr in blocks:
        if "(" not in expr:
            temp = split_query(expr)
            temporary_results = evaluate_multiple_expressions(preresults, temp, index)
            preresults[expr] = temporary_results
        else:
            temp = split_query_with_p(expr)
            temporary_results = evaluate_multiple_expressions(preresults,temp, index)

    final_results = list(set(temporary_results))

    print(str(len(final_results)) + " publications correspondantes ont été trouvées : ")
    k = 1
    for i in final_results:
        print("\t" + str(k) + "\t Publication n°" + str(i))
        k += 1
    return final_results
