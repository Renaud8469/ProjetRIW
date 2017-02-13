from collection import Collection
from useful_functions import get_docs
from indexation_of_cacm import *
import time
import pickle


cacm = open('CACM/cacm.all', 'r')

try:
    docs_cacm = open('static/docs_cacm.txt', 'r')
    print("Index détecté dans le dossier static/, chargement des fichiers détectés en cours...")
    index = pickle.load(open('static/index_cacm.p', 'rb'))
    docs = get_docs(docs_cacm)
    vocabulary = pickle.load(open('static/voc_cacm.p', 'rb'))
    id_to_doc = get_vocabulary_dict(cacm)[2]
    print("Index chargé !\n")
except FileNotFoundError:
    print("Index non trouvé dans le dossier static/, construction de l'index en cours...")
    vocabulary, number, id_to_doc = get_vocabulary_dict(cacm)
    index, docs = get_reverse_index(vocabulary, cacm)
    print("Index construit !\n")

cacm_collection = Collection(docs, vocabulary, index)

while 1:
    query = input("Entrez votre requête en utilisant les mots-clés séparés par une virgule : ")
    if query == "":
        print("Aucune requête n'a été faite, processus abandonné")
        break

    print("Recherche en cours... \n")

    search_time = time.time()
    results = cacm_collection.vector_search(query)
    finish_time = time.time()

    print(str(len(results)) + " publications correspondantes ont été trouvées: ")
    k = 1
    for i in results:
        print("\t" + str(k) + "\tPublication n°" + str(i[0]) + "\t- " + id_to_doc[i[0]])
        k += 1
        if k > 10:
            print("\n\t\tD'autres publications existent mais seuls les dix premiers résultats sont affichés")
            print("\t\tIl y a %s publications jugées pertinentes" % len(results))
            break

    print("\nRecherche effectuée en %s seconde(s) \n" % round(finish_time-search_time, 4))
