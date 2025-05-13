# Diego Rubio
# 05/01/2025
# comparison.py

import file_signatures
import os
import logging


# this will set up the log
logging.basicConfig(
    filename='file_checker.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def compare(filename, user):
    # get the file extension with the given filename
    extension = file_signatures.get_file_extension(filename)

    # pull the signature from the given filename
    signature = file_signatures.get_file_signature(filename)

    # this will be used to compare the file signature and see if it matches any in the dictionary
    # it is the expected signature from the dictionary of file signatures
    expected_sig = file_signatures.match(signature)

    # compare the file signature to the expected signature in the dictionary
    if expected_sig == extension:
        msg = f"{user} checked for {filename}"
        print(f"File {filename} is a {extension} file.")
    elif expected_sig is not None:
        msg = f"{user} for {filename}"
        print(f"File {filename} is a {expected_sig} file, with a {extension} extension.")
    else:
        msg = f"{user} checked for {filename}"
        print(f"File {filename} UNKNOWN.")

    logging.info(msg)

def main():
    user = input("Enter your name: ")
    logging.info(f"{user} logged in.")
    while True:
        file_name = input("Enter the file name (or exit to quit): ")
        if file_name.lower() == 'exit':
            print("Goodbye!")
            logging.info(f"{user} has logged out.")
            break
        if os.path.isfile(file_name):
            compare(file_name, user)
        else:
            print("File not found. Check the file name and try again please.")
            logging.info(f"{user} checked for {file_name} but file was not available or found.")

if __name__ == "__main__":
    main()