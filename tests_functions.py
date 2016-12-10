from useful_functions import *
from boolean_search import *

query = "Salut OR (bonjour AND hello) OR (Guten AND Tag)"

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
