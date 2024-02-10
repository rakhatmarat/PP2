def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums_input = input("Enter a list of integers separated by spaces: ").split()
nums = [int(num) for num in nums_input]

result = has_33(nums)
print("Result:", result)
