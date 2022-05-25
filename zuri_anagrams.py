def find_anagrams(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

a = find_anagrams("race", "acer")
b = find_anagrams("racecar", "carace")
x = find_anagrams("dormitory", "dirtyroom")
y = find_anagrams("casing", "scaning")
print(a)
print(b)
print(x)
print(y)
