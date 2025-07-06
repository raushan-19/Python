# write a python program to print the contents of a directory using the OS module. Search online for the function which does that.

import os

# Specify the path of the directory you want to list
directory_path = "/JavaScript"

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")

except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")

except Exception as e:
    print(f"An error occurred: {e}")
