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
e_measure = []
f_measure = []
alpha = 1/2
beta = 1
r_measure = [None]*(nb_docs_max+1)

print("Traitement en cours...")

for nb_docs in range(1, nb_docs_max+1):
    print(str(nb_docs*100/nb_docs_max) + "%")
    p = []
    r = []
    r_measure[nb_docs] = []
    for j in range(1, 65):
        r_measure_last = 1
        results = cacm_collection.vector_search(queries[j])

        k = 1
        p.append(0)
        r.append(0)
        for i in results:
            doc = i[0]
            try:
                if doc in answers[j]:
                    p[j-1] += 1
                    r[j-1] += 1/len(answers[j])
                    r_measure_last = k
            except KeyError:
                pass
            k += 1
            if k >= nb_docs:
                break

        r_measure[nb_docs].append(p[j-1] / r_measure_last)

    moy_p = 0
    moy_r = 0
    for i in p:
        moy_p += i / (64 * nb_docs)
    for i in r:
        moy_r += i/64

    tot_p.append(round(moy_p, 4))
    tot_r.append(round(moy_r, 4))

for i in range(nb_docs_max):
    try:
        current_f = 1/(alpha/tot_p[i] + (1-alpha)/tot_r[i])
        current_e = 1 - current_f
        f_measure.append(current_f)
        e_measure.append(current_e)
    except ZeroDivisionError:
        pass

"""Decomment to plot graph of E-measure or F-measure"""
# plt.plot(e_measure)
# plt.plot(f_measure)
# plt.show()

r_measure_mean = []
for l in r_measure:
    if type(l) == list:
        r_measure_mean.append(sum(l)/float(len(l)))

plt.plot(r_measure_mean)
plt.show()
