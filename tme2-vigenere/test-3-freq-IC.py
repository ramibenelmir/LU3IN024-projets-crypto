from cryptanalyse_vigenere import *

text1 = read("data/text1.cipher")
text2 = read("data/text2.cipher")

print("\n\n----------------------------------------------\n\n")

print("Test 3 : Frequence et Indice de Coïncidence")

print("---------------------")

print("Test freq")
assert freq(alphabet) == [1]*26
assert freq("ALICE") == freq("LICEA")
assert freq(text1) == [37.0, 21.0, 22.0, 10.0, 39.0, 4.0, 7.0, 9.0, 12.0, 22.0, 16.0, 32.0, 11.0, 36.0, 27.0, 19.0, 16.0, 29.0, 19.0, 15.0, 13.0, 16.0, 19.0, 18.0, 20.0, 16.0]
print("Test freq : OK")

print("---------------------")

print("Test lettre_freq_max")
assert lettre_freq_max("AAA") == 0
assert lettre_freq_max("ALKINDI") == 8
assert lettre_freq_max(text1) == 4
assert lettre_freq_max(text2) == 3
print("Test lettre_freq_max : OK")

print("---------------------")

print("Test incide_coincidence")
assert indice_coincidence(freq("AAA"))==1
assert abs(indice_coincidence(freq(text1))-0.04487)<0.00001
assert abs(indice_coincidence(freq(text2))-0.04037)<0.00001
print("Test indice_coincidence : OK")

print("---------------------")

print("Test longueur_clef")
assert longueur_clef(text1) == 7
assert longueur_clef(text2) == 10
print("Test longueur_clef : OK")

print("\n\n----------------------------------------------\n\n")
