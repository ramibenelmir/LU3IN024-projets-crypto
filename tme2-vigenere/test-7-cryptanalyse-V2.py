from cryptanalyse_vigenere import *

print("\n\n----------------------------------------------\n\n")

print("Test 7 : Cryptanalyse V2")

print("---------------------")

print("Test cryptanalyse_v2")
count = 0
for i in range(1,101):
    if cryptanalyse_v2(read("data/text"+str(i)+".cipher")) == read("data/text"+str(i)+".plain"):
        count+=1
        print("Cryptanalysis of data/text"+str(i)+" = SUCCESS")
    else:
        print("Cryptanalysis of data/text"+str(i)+" = FAILED")
print("\n"+str(count)+" texts successfully unciphered.")
assert count > 30
print("Test cryptanalyse_v2 : OK")

print("\n\n----------------------------------------------\n\n")
