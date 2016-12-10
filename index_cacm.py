from get_token_list import *

cacm = open('CACM/cacm.all', 'r')

vocabulary = get_vocabulary_dict(cacm)[0]
reverse_index = get_reverse_index(vocabulary, cacm)

#print(reverse_index)
#print(len(reverse_index))

preresults = individual_results(reverse_index, "harvard AND (program OR computer)")
print(preresults)

#s = split_query("NOT harvard")

#e = evaluate_single_expression(preresults, s, reverse_index)
#print(e)

boolean_search(reverse_index, "harvard AND (paris OR computer)")