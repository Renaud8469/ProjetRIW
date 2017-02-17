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
mean_average_p = []
nb_docs = 100

print("Traitement en cours...")

for j in range(1, 65):
    d = 0  # Indicating number of relevant documents returned
    k = 1  # Indicating number of documents returned
    results = cacm_collection.vector_search(queries[j])
    mean_average_p.append([])

    for i in results:
        doc = i[0]
        try:
            if doc in answers[j]:
                d += 1
                mean_average_p[j-1].append(d/k)
        except KeyError:
            pass
        k += 1
        if k >= nb_docs:
            break

temp = []
for q in mean_average_p:
    try:
        temp.append(sum(q)/float(len(q)))
    except ZeroDivisionError:
        pass

print(len(temp))

mean_average_precision = sum(temp)/float(len(temp))

print("On obtient une Mean Average Precision de %s en testant sur %i documents" % (round(mean_average_precision, 4), nb_docs))
