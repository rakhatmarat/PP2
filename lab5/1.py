with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

import re
matches_task1 = re.findall(r'ab*', text)
print("Task 1 Matches:", matches_task1)
