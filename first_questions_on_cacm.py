import time
from indexation_of_cacm import *
from useful_functions import *


cacm = open('CACM/cacm.all', 'r')

start_time = time.time()

print("Construction du vocabulaire en cours...")
vocabulary = get_vocabulary_dict(cacm)
vocabulary_time = time.time()
print("Vocabulaire établi - Temps de construction : %s seconde(s)" % round(vocabulary_time-start_time, 4))
print("\tNombre de tokens : " + str(vocabulary[1]))
print("\tTaille du vocabulaire : " + str(len(vocabulary[0])))

print("\n ------------- \n")

second_start_time = time.time()
print("Indexation des fichiers en cours...")
index = get_reverse_index(vocabulary[0], cacm)
index_time = time.time()
print("Index établi - Temps de construction : %s seconde(s)" % round(index_time-second_start_time, 4))
print("\t%s documents ont été indexés" % len(docs_in_index(index)))
print("\t%s termes dans l'index inversé" % len(index))