def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word or phrase: ")

if is_palindrome(word):
    print("The word or phrase is a palindrome.")
else:
    print("The word or phrase is not a palindrome.")
