from math import *

T=217847
T_prime=108935
M=11654
M_prime=8221

b = log(M_prime/M)/log(T_prime/T)
k = M/(T**b)

print(b)
print(k)