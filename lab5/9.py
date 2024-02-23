import re

with open("row.txt", "r") as file:
    text = file.read()

new_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

print(new_text)
