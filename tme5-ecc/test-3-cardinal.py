from ecc import *

print("\n\n----------------------------------------------\n\n")

print("Test 3 : Cardinal d'un courbe")

print("---------------------")

print("Test symbole de Legendre")

assert symbole_legendre(0, 19) == 0
assert symbole_legendre(-1, 19)  == -1 % 19
assert symbole_legendre(238178147069545409811713624143625858086, 340282366920938463463374607905636635233) == 1
assert symbole_legendre(15531934617505683567, 18446744547577975423) == -1 % 18446744547577975423

print("Test symbole de Legendre : OK\n")

print("Test cardinal")

E = (19, 1, 0)
assert cardinal(E) == 20

E = (1048583, 255245, 630385)
assert cardinal(E) == 1048398

print("Test cardinal : OK")

print("\n\n----------------------------------------------\n\n")
