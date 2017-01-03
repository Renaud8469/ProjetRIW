from get_token_list import *
from boolean_search import *
from useful_functions import *
import time

cacm = open('CACM/cacm.all', 'r')

start_time = time.time()

vocabulary = get_vocabulary_dict(cacm)[0]
reverse_index = get_reverse_index(vocabulary, cacm)

index_time = time.time()

print(str(len(docs_in_index(reverse_index))) + " documents ont été indexés")
print(str(len(reverse_index)) + " termes dans l'index inversé \n")
print("Index construit en %s seconde(s)\n" % round(index_time-start_time, 4))

query = input("Entrez votre requête en utilisant les mots-clés, AND, OR, NOT et des parenthèses : ")

print("Recherche en cours... \n")

search_time = time.time()
boolean_search(reverse_index, query)
finish_time = time.time()
print("Recherche effectuée en %s seconde(s)" % round(finish_time-search_time, 4))
