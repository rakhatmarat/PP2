import math
import random

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(word):
    return word == word[::-1]

def histogram(numbers):
    for num in numbers:
        print('*' * num)

def guess_the_number():
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break

    print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")

if __name__ == "__main__":
    print(sphere_volume(5))

    input_list = [1, 2, 3, 3, 4, 5, 5]
    print(unique_elements(input_list))

    word = "radar"
    print(is_palindrome(word))

    numbers = [4, 9, 7]
    histogram(numbers)

    guess_the_number()
