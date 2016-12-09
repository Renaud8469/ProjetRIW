from get_token_list import *

cacm = open('CACM/cacm.all', 'r')

vocabulary = get_vocabulary_dict(cacm)[0]
reverse_index = get_reverse_index(vocabulary, cacm)

print(reverse_index)
print(len(reverse_index))

print(docs_in_index(reverse_index))

#boolean_search(reverse_index, "computation OR east")