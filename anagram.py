def is_anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)


word1 = input("input first word: ")
word2 = input("input second word: ")
if is_anagram(word1, word2):
    print("{} and {} is anagram".format(word1, word2))
else:
    print("{} and {} is not anagram".format(word1, word2))
