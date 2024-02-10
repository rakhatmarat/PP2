def spy_game(nums):
  
    has_0 = False
    has_00 = False

    for num in nums:
        if num == 0:
            if has_00:
               
                return True
            elif has_0:
             
                has_00 = True
            else:
             
                has_0 = True
        elif num == 7 and has_0 and has_00:
            return True
    return False

nums_input = input("Enter a list of integers separated by spaces: ").split()
nums = [int(num) for num in nums_input]

result = spy_game(nums)
print("Result:", result)
