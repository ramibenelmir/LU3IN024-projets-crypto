from cryptanalyse_vigenere import *

text1 = read("data/text1.cipher")
text2 = read("data/text2.cipher")

print("\n\n----------------------------------------------\n\n")

print("Test 4 : Clef par decalages")

print("---------------------")

print("Test clef_par_decalages")
assert clef_par_decalages("GHGHGH",2) == [2,3]
assert clef_par_decalages(text1,7) == [10, 9, 7, 0, 24, 22, 0]
assert clef_par_decalages(text2,10) == [20, 11, 3, 4, 0, 23, 25, 14, 2, 6]
print("Test clef_par_decalages : OK")

print("\n\n----------------------------------------------\n\n")
