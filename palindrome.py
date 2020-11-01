def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word


word = input("input a word: ")
if is_palindrome(word):
    print("{} is palindrome".format(word))
else:
    print("{} is not palindrome".format(word))
