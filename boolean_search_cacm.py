from indexation_of_cacm import *
from collection import Collection
import time
import json


cacm = open('CACM/cacm.all', 'r')

try:
    index_cacm = open('static/index_cacm.json', 'r')
    docs_cacm = open('static/docs_cacm.txt', 'r')
    voc_cacm = open('static/voc_cacm.json', 'r')
    print("Index détecté dans le dossier static/, chargement des fichiers détectés en cours...")
    index = json.load(index_cacm)
    docs = json.load(docs_cacm)
    vocabulary = json.load(voc_cacm)
    id_to_doc = get_vocabulary_dict(cacm)[2]
    print("Index chargé !\n")
except FileNotFoundError:
    print("Index non trouvé dans le dossier static/, construction de l'index en cours...")
    vocabulary, number, id_to_doc = get_vocabulary_dict(cacm)
    index, docs = get_reverse_index(vocabulary, cacm)
    print("Index construit !\n")

cacm_collection = Collection(docs, vocabulary, index)

while 1:
    query = input("Entrez votre requête en utilisant les mots-clés, AND, OR, NOT et des parenthèses : ")
    if query == "":
        print("Aucune requête n'a été faite, processus abandonné")
        break

    print("Recherche en cours... \n")

    search_time = time.time()
    results = cacm_collection.boolean_search(query)
    finish_time = time.time()

    print(str(len(results)) + " publications correspondantes ont été trouvées : ")
    k = 1
    for i in results:
        i = int(i)
        print("\t" + str(k) + "\tPublication n°" + str(i) + "\t- " + id_to_doc[i])
        k += 1

    print("Recherche effectuée en %s seconde(s) \n" % round(finish_time-search_time, 4))
