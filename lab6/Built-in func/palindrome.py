def is_palindrome(string):
    # Remove whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Example strings
string1 = "Madam"
string2 = "Racecar"
string3 = "Hello World"

# Check if the strings are palindromes
print(string1, "is palindrome:", is_palindrome(string1))
print(string2, "is palindrome:", is_palindrome(string2))
print(string3, "is palindrome:", is_palindrome(string3))
