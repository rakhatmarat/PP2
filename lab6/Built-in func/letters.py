def count_upper_lower(string):
    # Count the number of upper case letters
    upper_count = sum(1 for char in string if char.isupper())

    # Count the number of lower case letters
    lower_count = sum(1 for char in string if char.islower())

    return upper_count, lower_count

# Example string
string = "Hello World! How Are You?"

# Calculate the number of upper case and lower case letters
upper_count, lower_count = count_upper_lower(string)

# Print the results
print("Number of upper case letters:", upper_count)
print("Number of lower case letters:", lower_count)
