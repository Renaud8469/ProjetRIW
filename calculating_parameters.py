from math import *

#Number of tokens in CACM
T = 217847
#Number of tokens in half-CACM
T_prime = 60272
#Vocabulary size for CACM
M = 11654
#Vocabulary size for half-CACM
M_prime = 6078

b = log(M_prime/M)/log(T_prime/T)
k = M/(T**b)

print("Valeur de b : " + str(b))
print("Valeur de k : " + str(k))

#Estimating vocabulary size for a collection with one million tokens
M_second = k*(1000000**b)

print("Estimation de la taille du vocabulaire pour une collection d'un million de tokens : " + str(int(M_second)))
