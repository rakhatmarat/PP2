from datetime import datetime

date1_input = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date1_input, "%Y-%m-%d %H:%M:%S")

date2_input = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.strptime(date2_input, "%Y-%m-%d %H:%M:%S")

difference_seconds = (date2 - date1).total_seconds()

print("Difference between date2 and date1 in seconds:", difference_seconds)
