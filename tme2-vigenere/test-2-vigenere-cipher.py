from cryptanalyse_vigenere import *
print("\n\n----------------------------------------------\n\n")

print("Test 2 : Vigenere Cipher")

print("---------------------")

print("Test chiffre_vigenere")
assert chiffre_vigenere("ALICE",[0]) == "ALICE"
assert chiffre_vigenere("ALICE",[3]) == "DOLFH"
assert chiffre_vigenere("ALICE",[1,2,3]) == "BNLDG"
assert chiffre_vigenere(read("data/text1.plain"),[10,9,7,0,24,22,0]) == read("data/text1.cipher")
print("Test chiffre_vigenere : OK")

print("---------------------")

print("Test dechiffre_cesar")
assert dechiffre_vigenere("ALICE",[0]) == "ALICE"
assert dechiffre_vigenere("DOLFH",[3]) == "ALICE"
assert dechiffre_vigenere("BNLDG",[1,2,3]) == "ALICE"
assert dechiffre_vigenere(read("data/text1.cipher"),[10,9,7,0,24,22,0]) == read("data/text1.plain")
print("Test dechiffre_vigenere : OK")

print("\n\n----------------------------------------------\n\n")
