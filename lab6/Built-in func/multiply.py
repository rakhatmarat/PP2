from functools import reduce

def multiply_list(numbers):
    # Use reduce() with a lambda function to multiply all numbers in the list
    result = reduce(lambda x, y: x * y, numbers)
    return result

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Multiply all numbers in the list
result = multiply_list(numbers)

# Print the result
print("Result:", result)
