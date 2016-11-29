import nltk
from get_token_list import *
from useful_functions import *

cacm = open('CACM/cacm.all', 'r')

token_cacm = get_token_list(cacm)
print("Nombre de tokens : " + str(len(token_cacm)))

token_no_common = lower_and_remove_common(token_cacm)
print("Sans les common-words : " + str(len(token_no_common)))

vocabulary = set(token_no_common)
print("Taille du vocabulaire : " + str(len(vocabulary)))