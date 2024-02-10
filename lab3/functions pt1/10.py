def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = input("Enter a list of elements separated by spaces: ").split()

unique_list = unique_elements(input_list)
print("Unique elements of the list:", unique_list)
