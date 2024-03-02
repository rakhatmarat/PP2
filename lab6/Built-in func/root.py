import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

# Sample input
number = 25100
milliseconds = 2123

# Call the delayed_square_root function
delayed_square_root(number, milliseconds)
