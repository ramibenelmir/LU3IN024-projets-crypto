from ecc import *

print("\n\n----------------------------------------------\n\n")

print("Test 9 : Echange de clé DH")

print("---------------------")

print("Test DH")

p = 1558360324771
n = 389590081193
E = (p,1,0) ##   #E = 4 n et n est un nombre premier
N_factors = ( (2,2),(n,1) )
N = 4*n
P = point_ordre(E,N,N_factors,n)
assert point_sur_courbe(P,E)
assert n == ordre(N,N_factors,P,E)
(sA,PA) = keygen_DH(P,E,n);
(sB,PB) = keygen_DH(P,E,n);
assert est_egal(echange_DH(sA,PB,E), echange_DH(sB,PA,E),p)


print("Test DH : OK")

print("\n\n----------------------------------------------\n\n")
