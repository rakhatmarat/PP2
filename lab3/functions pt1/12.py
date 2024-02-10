def histogram(numbers):
    for num in numbers:
        print('*' * num)

input_numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in input_numbers]

histogram(numbers)
