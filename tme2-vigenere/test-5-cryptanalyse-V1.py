from cryptanalyse_vigenere import *

print("\n\n----------------------------------------------\n\n")

print("Test 5 : Cryptanalyse V1")

print("---------------------")

print("Test cryptanalyse_v1")
count = 0
for i in range(1,101):
    if cryptanalyse_v1(read("data/text"+str(i)+".cipher")) == read("data/text"+str(i)+".plain"):
        count+=1
        print("Cryptanalysis of data/text"+str(i)+" = SUCCESS")
    else:
        print("Cryptanalysis of data/text"+str(i)+" = FAILED")
print("\n"+str(count)+" texts successfully unciphered.")
assert count > 10
print("Test cryptanalyse_v1 : OK")

print("\n\n----------------------------------------------\n\n")
