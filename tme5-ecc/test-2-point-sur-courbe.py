from ecc import *

print("\n\n----------------------------------------------\n\n")

print("Test 2 : Point sur courbe")

print("---------------------")

print("Test point_sur_courbe")
assert point_sur_courbe((), (17, 0, 1))
assert point_sur_courbe((0, 0), (13, 1, 0))
assert point_sur_courbe((4, 0), (17, 1, 0))
assert not point_sur_courbe((6, 0), (17, 1, 0))
assert point_sur_courbe((3, 7), (19, 1, 0))
assert point_sur_courbe((4, -7), (19, 1, 0))
assert point_sur_courbe((5, 4), (19, 1, 0))
assert point_sur_courbe((8, 11), (19, 1, 0))
assert point_sur_courbe((9, -4), (19, 1, 0))
assert point_sur_courbe((12, 7), (19, 1, 0))
assert point_sur_courbe((13, 5), (19, 1, 0))
assert point_sur_courbe((17, 3), (19, 1, 0))
assert point_sur_courbe((18, 6), (19, 1, 0))

print("Test point_sur_courbe : OK")


print("\n\n----------------------------------------------\n\n")
