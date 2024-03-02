import os

def check_path_access(path):
    # Check if path exists
    if os.path.exists(path):
        print(f"{path} exists.")
    else:
        print(f"{path} does not exist.")
        return

    # Check readability
    if os.access(path, os.R_OK):
        print(f"{path} is readable.")
    else:
        print(f"{path} is not readable.")

    # Check writability
    if os.access(path, os.W_OK):
        print(f"{path} is writable.")
    else:
        print(f"{path} is not writable.")

    # Check executability
    if os.access(path, os.X_OK):
        print(f"{path} is executable.")
    else:
        print(f"{path} is not executable.")

# Specify the path here
path = "/path/to/your/directory"

# Call the function to check path access
check_path_access(path)
