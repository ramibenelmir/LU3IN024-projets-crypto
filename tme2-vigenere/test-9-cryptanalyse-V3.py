from cryptanalyse_vigenere import *

print("\n\n----------------------------------------------\n\n")

print("Test 9 : Cryptanalyse V3")

print("---------------------")

print("Test cryptanalyse_v3")
count = 0
for i in range(1,101):
    if cryptanalyse_v3(read("data/text"+str(i)+".cipher")) == read("data/text"+str(i)+".plain"):
        count+=1
        print("Cryptanalysis of data/text"+str(i)+" = SUCCESS")
    else:
        print("Cryptanalysis of data/text"+str(i)+" = FAILED")
print("\n"+str(count)+" texts successfully unciphered.")
assert count > 70
print("Test cryptanalyse_v3 : OK")

print("\n\n----------------------------------------------\n\n")
