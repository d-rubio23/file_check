# Diego Rubio
# 05/01/2025
# file_signatures.py

# This file contains the functions used to check file signatures and extension
import os

# This dictionary contains the file signatures for different file types
file_signatures = {
    "jpg": [b'\xff\xd8\xff'],
    "png": [b'\x89PNG\r\n\x1a\n'],
    "pdf": [b'%PDF-'],
    "zip": [b'PK\x03\x04'],
}


# this function will get the file signature of a file using the file name
def get_file_signature(filename, bytes=8):
    with open(filename, 'rb') as f:
        return f.read(bytes)
    
# this will get the extension with the argument of the file name
def get_file_extension(filename):
    return os.path.splitext(filename)[1][1:].lower()

def match(bytes):
    # match the file signature with the expected signature from the dictionary
    for extension, sig_list in file_signatures.items():
        if bytes.startswith(tuple(sig_list)):
            return extension
    return None

