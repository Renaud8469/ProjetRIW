import time
import os
from indexation_of_cacm import *
import pickle


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
    size = os.stat("static/index_cacm.p").st_size / 1000000
    size_voc = os.stat("static/voc_cacm.p").st_size
    size_docs = os.stat("static/docs_cacm.txt").st_size
    print("\nIndex détecté dans le dossier static (taille %s Mo), l'index actuel n'a pas été conservé" % size)
except FileNotFoundError:
    answer = input("\nPas d'index détecté pour CACM dans le dossier static/. Enregistrer l'index permet de relancer plus rapidement les programmes de recherche, souhaitez-vous enregistrer l'index (espace occupé estimé à 1 Mo) ? [y/n]")
    if answer == "y":
        pickle.dump(index, open('static/index_cacm.p', 'wb'))
        size = os.stat("static/index_cacm.p").st_size / 1000000
        print("L'index a bien été enregistré dans le fichier static/index_cacm.p (taille %s Mo)" % size)
        static_docs = open('static/docs_cacm.txt', 'w')
        for doc in docs:
            static_docs.write(str(doc)+"\n")
        pickle.dump(vocabulary[0], open('static/voc_cacm.p', 'wb'))
    elif answer == "n":
        print("L'index n'a pas été enregistré.")
    else:
        print("Commande non reconnue, l'index n'a pas été enregistré")
