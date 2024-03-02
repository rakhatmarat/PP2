def write_list_to_file(lst, filename):
    try:
        with open(filename, 'w') as file:
            for item in lst:
                file.write(str(item) + '\n')
        print(f"List has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage:
my_list = [1, 2, 3, 4, 5]  # Your list
output_file = "output.txt"  # Output file name
write_list_to_file(my_list, output_file)
