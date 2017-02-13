import time
import os
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

try:
    size = os.stat("static/index_cs276.txt").st_size / 1000000
    print("\nIndex détecté dans le dossier static (taille %s Mo), l'index actuel n'a pas été conservé" % size)
except FileNotFoundError:
    answer = input("\nPas d'index détecté pour CS276 dans le dossier static/, souhaitez-vous enregistrer l'index ? [y/n]")
    if answer == "y":
        static_index = open('static/index_cs276.txt', 'w')
        static_index.write(str(index))
        size = os.stat("static/index_cs276.txt").st_size / 1000000
        print("L'index a bien été enregistré dans le fichier static/index_cs276.txt (taille %s Mo)" % size)
        static_docs = open('static/docs_cs276.txt', 'w')
        for doc in list(docs.keys()):
            static_docs.write(str(doc)+"\n")
        static_voc = open('static/voc_cs276.txt', 'w')
        static_voc.write(str(vocabulary))
    elif answer == "n":
        print("L'index n'a pas été enregistré.")
    else:
        print("Commande non reconnue, l'index n'a pas été enregistré")
