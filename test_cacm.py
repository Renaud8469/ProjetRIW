import nltk
from get_token_list import *
from common_words_comp import *

cacm = open('CACM/cacm.all', 'r')

token_cacm = get_token_list(cacm)
print("Nombre de tokens : ")
print(len(token_cacm))

token_no_duplicates = lower_and_remove_common(token_cacm)
print("Sans les duplicats : ")
print(len(token_no_duplicates))

vocabulary = set(token_no_duplicates)
print("Taille du vocabulaire : ")
print(len(vocabulary))