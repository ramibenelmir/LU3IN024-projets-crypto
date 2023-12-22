from ecc import *

print("\n\n----------------------------------------------\n\n")

print("Test 7 : Multiplication scalaire")

print("---------------------")

E = (19,1,0)
p =19

print("Test multiplication scalaire")
assert est_egal((),multiplication_scalaire(10,(),E),p)
assert est_egal((),multiplication_scalaire(2,(0,0),E),p)
assert est_egal((5,4),multiplication_scalaire(1,(5,4),E),p)
assert est_egal((),multiplication_scalaire(0,(5,4),E),p)
assert est_egal((5,15),multiplication_scalaire(-1,(5,4),E),p)
assert est_egal((17,16),multiplication_scalaire(7,(4,12),E),p)
assert est_egal((17,3),multiplication_scalaire(-7,(4,12),E),p)
assert est_egal((),multiplication_scalaire(10,(4,12),E),p)
assert est_egal((),multiplication_scalaire(20,(4,12),E),p)

E = (98175052450778425556766364659684988681, 53428953385477770830953790266770459660, 90651943953048698831952209306618640600)
p, a, b = E
P = (40053801806340741673028224443096949294, 14721339076191281245200637780767808295)
Q = (2763741046070728013346642120224285580, 87567442272109043290164268359821786768)

assert est_egal(Q, multiplication_scalaire(22944262879064599906526149625178051433, P, E), p)


print("Test multiplication scalaire : OK")

print("\n\n----------------------------------------------\n\n")
