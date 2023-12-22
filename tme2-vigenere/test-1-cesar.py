from cryptanalyse_vigenere import *
print("\n\n----------------------------------------------\n\n")

print("Test 1 : Cesar")

print("---------------------")

print("Test chiffre_cesar")
assert chiffre_cesar("ALICE",0) == "ALICE"
assert chiffre_cesar("ALICE",3) == "DOLFH"
print("Test chiffre_cesar : OK")

print("---------------------")

print("Test dechiffre_cesar")
assert dechiffre_cesar("ALICE",0) == "ALICE"
assert dechiffre_cesar("ALICE",23) == "DOLFH"
print("Test dechiffre_cesar : OK")

print("\n\n----------------------------------------------\n\n")
