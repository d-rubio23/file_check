# Diego Rubio
# 05/01/2025
# comparison.py

import file_signatures
import os
import logging




def compare(filename):
    # get the file extension with the given filename
    extension = file_signatures.get_file_extension(filename)

    # pull the signature from the given filename
    signature = file_signatures.get_file_signature(filename)

    # this will be used to compare the file signature and see if it matches any in the dictionary
    # it is the expected signature from the dictionary of file signatures
    expected_sig = file_signatures.match(signature)

    # compare the file signature to the expected signature in the dictionary
    if expected_sig == extension:
        print(f"File {filename} is a {extension} file.")
    elif expected_sig is not None:
        print(f"File {filename} is a {expected_sig} file, with a {extension} extension.")
    else:
        print(f"File {filename} UNKNOWN.")

def main():
    while True:
        file_name = input("Enter the file name (or exit to quit): ")
        if file_name.lower() == 'exit':
            print("Goodbye!")
            break
        if os.path.isfile(file_name):
            compare(file_name)
        else:
            print("File not found. Check the file name and try again please.")

if __name__ == "__main__":
    main()