import re

with open("row.txt", "r") as file:
    text = file.read()

new_text = re.sub(r'[ ,.]', ':', text)

print(new_text)
