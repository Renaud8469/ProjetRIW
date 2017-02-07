import nltk
from get_token_list import *
from useful_functions import *

cacm = open('CACM/cacm.all', 'r')

vocabulary_cacm = get_vocabulary_dict(cacm)
print("Nombre de tokens : " + str(vocabulary_cacm[1]))
print("Taille du vocabulaire : " + str(len(vocabulary_cacm[0])))

reverse_index_cacm = get_reverse_index(vocabulary_cacm[0], cacm)
print(reverse_index_cacm)
