from collection import Collection
from indexation_of_cs276 import *
from first_questions_on_cs276 import get_vocabulary_cs276
import time


vocabulary = get_vocabulary_cs276()
docs, index = make_dictionary("CS276/pa1-data/")

cs276_collection = Collection(list(docs.keys()), vocabulary, index)

while 1:
    query = input("Entrez votre requête en utilisant les mots-clés séparés par une virgule : ")
    if query == "":
        print("Aucune requête n'a été faite, processus abandonné")
        break

    print("Recherche en cours... \n")

    search_time = time.time()
    results = cs276_collection.vector_search(query)
    finish_time = time.time()

    print(str(len(results)) + " publications correspondantes ont été trouvées: ")
    k = 1
    for i in results:
        print("\t" + str(k) + "\tPublication n°" + str(i[0]))
        k += 1
        if k > 10:
            print("\n\t\tD'autres publications existent mais seuls les dix premiers résultats sont affichés")
            print("\t\tIl y a %s publications jugées pertinentes" % len(results))
            break

    print("\nRecherche effectuée en %s seconde(s) \n" % round(finish_time-search_time, 4))
