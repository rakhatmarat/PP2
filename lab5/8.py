import re

with open("row.txt", "r") as file:
    text = file.read()

parts = re.findall('[A-Z][^A-Z]*', text)

print(parts)
