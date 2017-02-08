from collection import Collection
from indexation_of_cs276 import *
from first_questions_on_cs276 import get_vocabulary_cs276
import time


vocabulary = get_vocabulary_cs276()[0]
docs, index = make_dictionary("CS276/pa1-data/")
id_to_doc = make_doc_id_to_doc("CS276/pa1-data/")[0]

cs276_collection = Collection(list(docs.keys()), vocabulary, index)

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
        print("\t" + str(k) + "\tPublication n°" + str(i) + "\t- " + id_to_doc[i])
        k += 1

    print("Recherche effectuée en %s seconde(s) \n" % round(finish_time-search_time, 4))
