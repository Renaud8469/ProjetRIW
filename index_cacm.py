from get_token_list import *

cacm = open('CACM/cacm.all', 'r')

vocabulary = get_vocabulary_dict(cacm)[0]
reverse_index = get_reverse_index(vocabulary, cacm)

print(reverse_index)
print(len(reverse_index))