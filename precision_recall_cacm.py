from collection import Collection
from indexation_of_cacm import *


cacm = open('CACM/cacm.all', 'r')
vocabulary, number, id_to_doc = get_vocabulary_dict(cacm)
index, docs = get_reverse_index(vocabulary, cacm)

cacm_collection = Collection(docs, vocabulary, index)

cacm_query = open('CACM/query.text', 'r')
cacm_answers = open('CACM/qrels.text', 'r')


queries = parse_queries(cacm_query)
answers = parse_answers(cacm_answers)
tot_p = []
tot_r = []
nb_docs_max = 100

print("Traitement en cours...")

for nb_docs in range(1, nb_docs_max+1):
    print(str(nb_docs*100/nb_docs_max) + "%")
    p = []
    r = []
    for j in range(1, 64):
        results = cacm_collection.vector_search(queries[j])

        k = 1
        p.append(0)
        r.append(0)
        for i in results:
            doc = i[0]
            k += 1
            try:
                if doc in answers[j]:
                    p[j-1] += 1
                    r[j-1] += 1/len(answers[j])
            except KeyError:
                pass
            if k > nb_docs:
                break

    moy_p = 0
    moy_r = 0
    for i in p:
        moy_p += i / (64 * nb_docs)
    for i in r:
        moy_r += i/64

    tot_p.append(round(moy_p, 4))
    tot_r.append(round(moy_r, 4))

print("\nPrécision maximale : " + str(max(tot_p)) + " pour " + str(tot_p.index(max(tot_p)) + 1) + " documents")
print("Rappel maximal : " + str(max(tot_r)) + " pour " + str(tot_r.index(max(tot_r)) + 1) + " documents\n")

cheap_graph(nb_docs_max, tot_p, tot_r)

plt.plot(tot_r, tot_p)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.show()
