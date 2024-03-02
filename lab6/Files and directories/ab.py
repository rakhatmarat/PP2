import string
import os

def generate_files():
    try:
        # Create a directory if it doesn't exist
        if not os.path.exists("files"):
            os.makedirs("files")
        
        # Generate files from A.txt to Z.txt
        for letter in string.ascii_uppercase:
            filename = f"files/{letter}.txt"
            with open(filename, 'w') as file:
                file.write(f"This is file {letter}.txt")
        
        print("Text files generated successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Call the function to generate files
generate_files()
