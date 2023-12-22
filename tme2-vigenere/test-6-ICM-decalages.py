from cryptanalyse_vigenere import *

text1 = read("data/text1.cipher")
text2 = read("data/text2.cipher")

print("\n\n----------------------------------------------\n\n")

print("Test 6 : ICM décalages")

print("---------------------")

print("Test indice_coincidence_mutuelle")
assert indice_coincidence_mutuelle(freq("ABABAB"),freq("CDCDCD"),0) == 0
assert indice_coincidence_mutuelle(freq("ABABAB"),freq("CDCDCD"),2) == 0.5
assert abs(indice_coincidence_mutuelle(freq(text1),freq(text2),0)-0.0369) < 0.001
print("Test tableau_decalages_naif : OK")

print("---------------------")

print("Test tableau_decalages_ICM")
assert tableau_decalages_ICM("GHGHGH",2) == [0,1]
assert tableau_decalages_ICM(text1,7) == [0, 25, 23, 16, 14, 12, 16]
assert tableau_decalages_ICM(text2,10) == [0, 25, 5, 6, 13, 25, 1, 16, 4, 8]
print("Test tableau_decalages_ICM : OK")

print("\n\n----------------------------------------------\n\n")
