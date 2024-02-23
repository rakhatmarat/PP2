import re

with open("row.txt", "r") as file:
    text = file.read()

pattern = r'a.*b$'

matches = re.findall(pattern, text)

print(matches)

