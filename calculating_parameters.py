from useful_functions import *

# Number of tokens in CACM
T = 189832
# Number of tokens in half-CACM
T_prime = 53947
# Vocabulary size for CACM
M = 8997
# Vocabulary size for half-CACM
M_prime = 5041

b = get_b(T, T_prime, M, M_prime)
k = get_k(T, M, b)

print("Pour CACM, Valeur de b : " + str(b))
print("Pour CACM, Valeur de k : " + str(k))

# Estimating vocabulary size for a collection with one million tokens
M_second = k*(1000000**b)

print("Pour CACM, Estimation de la taille du vocabulaire pour une collection d'un million de tokens : " + str(int(M_second)))

# ----------------------------------------------------------------------------
# Number of tokens and vocabulary size in CS76
t_cs76 = 23912191
m_cs76 = 244580
# number of tokens and vocabulary size in half of CS76
t_prime_cs76 = 13611296
m_prime_cs76 = 150733

b_cs76 = get_b(t_cs76, t_prime_cs76, m_cs76, m_prime_cs76)
k_cs76 = get_k(t_cs76, m_cs76, b_cs76)

print("Pour CS76, valeur de b : " + str(b_cs76))
print("Pour CS76, valeur de k : " + str(k_cs76))

# Estimating vocabulary size for a CS76-collection with one million tokens
m_second_cs76 = k_cs76*(1000000**b_cs76)

print("Pour CS76, Estimation de la taille du vocabulaire pour une collection d'un million de tokens : " + str(int(m_second_cs76)))

