from indexation_of_cacm import parse_answers, parse_queries
from boolean_search import *

print("-------------------")
query = "Salut OR (bonjour AND hello) OR (Guten AND Tag)"
print("Test des fonctions de traitement de requête booléennes avec la requêtes suivante : " + query + "\n")


s1 = split_query(query)
print("La fonction split_query : ")
print(s1)

s2 = split_query_with_p(query)
print("La fonction split_query_with_p : ")
print(s2)

s3 = trimming(query)
print("La fonction trimming : ")
print(s3[0])

s4 = parentheses_blocks(query)
print("La fonction parentheses_blocks : ")
print(s4)


print("-------------------\n")

print("-------------------")
print("Test des fonctions de parsing des requêtes/documents pour CACM\n")

cacm_query = open('CACM/query.text', 'r')
cacm_answers = open('CACM/qrels.text', 'r')

queries = parse_queries(cacm_query)
answers = parse_answers(cacm_answers)

print("Dictionnaire des requêtes par ID :")
print(queries)
print("Dictionnaire des documents pertinents par ID des requêtes :")
print(answers)

print("-------------------\n")
