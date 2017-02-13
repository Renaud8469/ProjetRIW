from collection import Collection
from indexation_of_cs276 import *
from first_questions_on_cs276 import get_vocabulary_cs276
import time


# try:
#     index_cs276 = open('static/index_cs276.txt', 'r').read()
#     docs_cs276 = open('static/docs_cs276.txt', 'r')
#     vocabulary_cs276 = open('static/voc_cs276.txt', 'r').read()
#     print("Index détecté dans le dossier static/, chargement des fichiers détectés en cours...")
#     index = index_cs276
#     vocabulary = vocabulary_cs276
#     docs = get_docs(docs_cs276)
#     print("Index chargé !\n")
# except FileNotFoundError:

print("Construction de l'index en cours...")
vocabulary = get_vocabulary_cs276()[0]
docs, index = make_dictionary("CS276/pa1-data/")
docs = list(docs.keys())
print("Index construit !\n")

id_to_doc = make_doc_id_to_doc("CS276/pa1-data/")[0]

cs276_collection = Collection(docs, vocabulary, index)

while 1:
    query = input("Entrez votre requête en utilisant les mots-clés, AND, OR, NOT et des parenthèses : ")
    if query == "":
        print("Aucune requête n'a été faite, processus abandonné")
        break

    print("Recherche en cours... \n")

    search_time = time.time()
    results = cs276_collection.boolean_search(query)
    finish_time = time.time()

    print(str(len(results)) + " publications correspondantes ont été trouvées : ")
    k = 1
    for i in results:
        i = int(i)
        print("\t" + str(k) + "\tPublication n°" + str(i) + "\t- " + id_to_doc[i])
        k += 1

    print("Recherche effectuée en %s seconde(s) \n" % round(finish_time-search_time, 4))
