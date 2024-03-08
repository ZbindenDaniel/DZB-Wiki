# boot.py
"""
This files runs on boot.
Use cases:
# Run on Power up
# Run on reboot triggered by OTA

# Functionality:
    - Check if source is up to date (file 'upToDate' does not exist, got deleted by git-Pull)
    - if not copy the files from '/update' to '/' (override exisiting files)
    - Create File 'upToDate'
"""

import os
import machine

# Check if a specific file exists in the root directory
def file_exists(filename):
    if filename in os.listdir('/'):
        print(f'{filename} exists')
        return True
    return False

# Copy files from source directory to destination directory
def copy_files_from_to(src_dir, dest_dir):
    print(f'copy_files from {src_dir} to {dest_dir}')
    for file in os.listdir(src_dir):
        if file == 'lib': # Special case: don't copy external libraries
            continue
        if os.path.isdir(file):
            continue # TODO: so far only files in a folder get copied, subfolders are ignored
            #os.mkdir(f'{dest_dir}/{file}')
            #copy_files_from_to(file, f'{dest_dir}/{file}')
        print(f'write {file}')
        with open(src_dir + file, 'r') as source:
        
            with open(dest_dir + file, 'w') as dest:
                dest.write(source.read())
                dest.close()
            source.close()
    print('finish copying')

# Backup files to '/rollback' before updating
def backup_files():
    copy_files_from_to('/', '/rollback/')

# Rollback to previous state
def rollback():
    copy_files_from_to('/rollback/', '/')
    os.remove('notUpdatable')
    
# Fetch update by copying files and creating 'upToDate' file
def fetch_update():
    print('fetch_update')
    try:
        backup_files()
        if os.path.isdir('update'):
            copy_files_from_to('/update/', '/')
            with open('/upToDate', 'w') as f:
                f.write('Updated')
            machine.reset()
        print('Did not Update Firmware!')
    except Exception as e:
        print(e)
        with open('/notUpdatable', 'w') as f:
            print('could not update')
            f.write(str(e))



# Main execution
if file_exists('notUpdatable'):
    print('not Updatable')
    rollback()# Rollback to previous state if 'notUpdatable' exists
elif not file_exists('upToDate') and os.path.exists('update/main.py'):
    print('up to date')
    fetch_update()
