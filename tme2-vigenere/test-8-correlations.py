from cryptanalyse_vigenere import *

text1 = read("data/text1.cipher")
text2 = read("data/text2.cipher")

print("\n\n----------------------------------------------\n\n")

print("Test 8 : Correlations")

print("---------------------")

print("Test correlations")
assert correlation([1,2,3,4],[2,4,6,8]) == 1.0
assert abs(correlation([1,2,3,4,5],[5,4,1,7,9]) - 0.5734) < 0.0001
assert abs(correlation(freq(text1),freq(text2)) + 0.2522) < 0.0001
print("Test correlations : OK")

print("---------------------")

print("Test clef_correlations")
(score0, key0) = clef_correlations("ALKINDI",2)
assert abs(score0-0.34)<0.01
assert key0 == [22, 25]
(score1, key1) = clef_correlations(text1,7)
assert abs(score1-0.89)<0.01
assert key1 == [10, 9, 7, 0, 24, 22, 0]
(score2, key2) = clef_correlations(text2,10)
assert abs(score2-0.81)<0.01
assert key2 == [24, 23, 3, 4, 11, 23, 25, 14, 2, 6]
print("Test clef_correlations : OK")

print("\n\n----------------------------------------------\n\n")
