from collection import Collection
from indexation_of_cacm import *
from useful_functions import lower_and_remove_common, custom_tokenize
import time


cacm = open('CACM/cacm.all', 'r')
vocabulary, number, id_to_doc = get_vocabulary_dict(cacm)
index, docs = get_reverse_index(vocabulary, cacm)

cacm_collection = Collection(docs, vocabulary, index)

cacm_query = open('CACM/query.text', 'r')
cacm_answers = open('CACM/qrels.text', 'r')


def parse_queries(query_file):
    query_dict = {}
    latest_mark = ""
    current_query_id = 0
    for line in query_file:
        if ".I" in line:
            current_query_id = get_id(line)
            query_dict[current_query_id] = ""
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if ".W" in latest_mark and len(line) > 3:
            current_tokens = lower_and_remove_common(custom_tokenize(line))
            for token in current_tokens:
                if len(token) > 1:
                    query_dict[current_query_id] += token + " "
    return query_dict


def parse_answers(answer_file):
    answer_dict = {}
    for line in answer_file:
        current_id = int(line[0:2])
        if current_id in answer_dict.keys():
            answer_dict[current_id].append(int(line[3:7]))
        else:
            answer_dict[current_id] = [int(line[3:7])]
    return answer_dict


queries = parse_queries(cacm_query)
answers = parse_answers(cacm_answers)
tot_p = []
tot_r = []


for nb_docs in range(1, 21):
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

    moy = 0
    moy_r = 0
    for i in p:
        moy += i/(64 * nb_docs)
    for i in r:
        moy_r += i/64

    print("Précision moyenne pour %i documents retournés : %s" % (nb_docs, moy))
    print("Rappel moyen pour %i documents retournés : %s" % (nb_docs, moy_r))
    tot_p.append(moy)
    tot_r.append(moy_r)

print(tot_p)
print(tot_r)
