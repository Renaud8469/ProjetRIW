from get_token_list import *
from boolean_search import *
from useful_functions import *

cacm = open('CACM/cacm.all', 'r')

vocabulary = get_vocabulary_dict(cacm)[0]
reverse_index = get_reverse_index(vocabulary, cacm)

print(str(len(docs_in_index(reverse_index))) + " documents ont été indexés")
print(str(len(reverse_index)) + " termes dans l'index inversé \n")

query = input("Entrez votre requête en utilisant les mots-clés, AND, OR, NOT et des parenthèses : ")

print("Recherche en cours... \n")

boolean_search(reverse_index, query)
