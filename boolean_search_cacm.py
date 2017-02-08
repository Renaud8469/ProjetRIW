from indexation_of_cacm import *
from collection import Collection
import time


cacm = open('CACM/cacm.all', 'r')
vocabulary = get_vocabulary_dict(cacm)[0]
index = get_reverse_index(vocabulary, cacm)

cacm_collection = Collection(vocabulary, index)

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
        print("\t" + str(k) + "\tPublication n°" + str(i))
        k += 1

    print("Recherche effectuée en %s seconde(s) \n" % round(finish_time-search_time, 4))
