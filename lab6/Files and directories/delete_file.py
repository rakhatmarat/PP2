import os

def delete_file(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Check if the file is accessible
            if os.access(file_path, os.F_OK | os.R_OK | os.W_OK | os.X_OK):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"File '{file_path}' is not accessible.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
delete_file("example.txt")
