from ecc import *

print("\n\n----------------------------------------------\n\n")

print("Test 1 : Est elliptique")

print("---------------------")

print("Test est_elliptique")

assert est_elliptique((19, 1, 0))
assert est_elliptique((73, 7, 30))
assert est_elliptique((79, 30, 54))
assert est_elliptique((31, 19, 21))
assert est_elliptique((89, 56, 82))
assert est_elliptique((17, 11, 15))
assert est_elliptique((5, 1, 1))
assert est_elliptique((739, 41, 728))
assert est_elliptique((167, 84, 155))
assert est_elliptique((193, 51, 152))

assert not est_elliptique((3, 0, 2))
assert not est_elliptique((2, 0, 0))
assert est_elliptique((761, 315, 24))
assert not est_elliptique((3, 0, 1))
assert not est_elliptique((7, 0, 0))
assert not est_elliptique((2, 0, 0))
assert est_elliptique((11, 1, 5))
assert est_elliptique((23, 3, 2))
assert est_elliptique((967, 164, 939))
assert est_elliptique((13, 4, 10))
assert est_elliptique((41, 12, 25))


print("Test est_elliptique : OK")


print("\n\n----------------------------------------------\n\n")
