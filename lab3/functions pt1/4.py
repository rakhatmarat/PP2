def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)
