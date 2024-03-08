#fileHandler.py

import os

# Check if a specific file exists in the root directory
def file_exists(filename):
    if filename in os.listdir('/'):
        return True
    return False

# Copy files from source directory to destination directory
def copy_files_from_to(src_dir, dest_dir):
    for file in os.listdir(src_dir):
        with open(src_dir + file, 'r') as source:
            with open(dest_dir + file, 'w') as dest:
                dest.write(source.read())

def is_directory(path):
  try:
    return (os.stat(path)[8] == 0)
  except:
    return False