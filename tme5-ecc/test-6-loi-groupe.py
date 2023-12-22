from ecc import *

print("\n\n----------------------------------------------\n\n")

print("Test 6 : Loi de groupe")

print("---------------------")

print("Test egalite")
assert est_egal((1, 2), (20, 21), 19)
assert not est_egal((1, 2), (-1, 2), 19)
assert not est_egal((3, 4), (-3, 4), 19)
assert est_egal((), (), 19)
assert not est_egal((), (2, 3), 19)
assert not est_egal((2, 3), (), 19)
print("Test egalite : OK")

print("---------------------")
p = 19
E = (p, 1, 0)

print("Test addition")

assert est_egal((), addition((), (), E), p)
assert est_egal((4, 7), addition((), (4, 7), E), p)
assert est_egal((5, 4), addition((5, 4), (), E), p)
assert est_egal((), addition((8, 11), (8, 8), E), p)
assert est_egal((18, 6), addition((9, 4), (12, 7), E), p)
assert est_egal((13, 14), addition((0, 0), (3, 7), E), p)


print("Test addition : OK")

print("\n\n----------------------------------------------\n\n")
