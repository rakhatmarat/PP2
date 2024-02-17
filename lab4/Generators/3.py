def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
start = int(input("Enter a number: "))
end  = int(input("Enter a number: "))
numbers = divisible_by_3_and_4(start, end)
for num in numbers:
    print(num)
