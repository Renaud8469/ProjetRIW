import time
from first_questions_on_cs276 import get_vocabulary_cs276
from indexation_of_cs276 import make_dictionary


start_time = time.time()

print("Construction du vocabulaire en cours...")
vocabulary = get_vocabulary_cs276()
vocabulary_time = time.time()
print("Vocabulaire établi - Temps de construction : %s seconde(s)" % round(vocabulary_time-start_time, 4))
print("\tNombre de tokens : " + str(vocabulary[1]))
print("\tTaille du vocabulaire : " + str(len(vocabulary[0])))

print("\n ------------- \n")

second_start_time = time.time()
print("Indexation des fichiers en cours...")
docs, index = make_dictionary("CS276/pa1-data/")
index_time = time.time()
print("Index établi - Temps de construction : %s seconde(s)" % round(index_time-second_start_time, 4))
print("\t%s documents ont été indexés" % len(docs))
print("\t%s termes dans l'index inversé" % len(index))
