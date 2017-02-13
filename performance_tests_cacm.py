import time
import json
import os
from indexation_of_cacm import *


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
index, docs = get_reverse_index(vocabulary[0], cacm)
index_time = time.time()
print("Index établi - Temps de construction : %s seconde(s)" % round(index_time-second_start_time, 4))
print("\t%s documents ont été indexés" % len(docs))
print("\t%s termes dans l'index inversé" % len(index))

try:
    size = os.stat("static/index_cacm.json").st_size / 1000000
    print("\nIndex détecté dans le dossier static (taille %s Mo), l'index actuel n'a pas été conservé" % size)
except FileNotFoundError:
    answer = input("\nPas d'index détecté pour CACM dans le dossier static/, souhaitez-vous enregistrer l'index ? [y/n]")
    if answer == "y":
        static_index = open('static/index_cacm.json', 'w')
        static_index.write(json.dumps(index))
        size = os.stat("static/index_cacm.json").st_size / 1000000
        print("L'index a bien été enregistré dans le fichier static/index_cacm.json (taille %s Mo)" % size)
        static_docs = open('static/docs_cacm.txt', 'w')
        static_docs.write(str(docs))
        static_voc = open('static/voc_cacm.json', 'w')
        static_voc.write(json.dumps(vocabulary))
    elif answer == "n":
        print("L'index n'a pas été enregistré.")
    else:
        print("Commande non reconnue, l'index n'a pas été enregistré")
