import re

# Read the contents of the file
with open("row.txt", "r") as file:
    text = file.read()

# Define the pattern
pattern = r'[a-z]+_[a-z]+'

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
print(matches)
