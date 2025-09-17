# This program takes a snapshot of the current working directory, and saves the new backup to a zip file
from pathlib import Path
import os, re, zipfile, shutil, sys

# Determine the folder to backup
folder_path = "" # This variable will contain the project folder path that the user wishes to backup

try:
    user_defined_path = Path(sys.argv[1]) 
    if user_defined_path.exists and user_defined_path.is_dir: # verify folder path validity
        folder_path = user_defined_path
except IndexError as error:
    sys.exit('User defined path is not valid, exiting program.')

# Create backup folder if it doesn't already exist (create it in the same directory where the current working directory exists
folder_name = folder_path.name
folder_backup_name = folder_name + '_backup'

parent_folder_path = folder_path.parent
backup_folder_path = parent_folder_path / folder_backup_name
    
if backup_folder_path.exists() == False: # Check if the backup folder exists
    backup_folder_path.mkdir() # Create backup folder
    print('Created backup folder ' + str(backup_folder_path))
    
# Decide on the zipfile name by looking through the current backup files in the backup folder. Name it something like folder_name_1.zip
backup_folder_file_list = []

for entry in os.listdir(backup_folder_path):
    file_full_path = Path(os.path.join(backup_folder_path, entry)) # Get the full file path of each file in the backup folder
    if os.path.isfile(file_full_path):
        backup_folder_file_list.append(file_full_path.name) # Add a file name to the list 

if len(backup_folder_file_list) == 0: # If the backup folder list is empty, number the zip file as number 1
    zip_file_name = folder_name + "_1"
else: # If the backup folder list is not empty, itterate through the list, and extract out the largest number of the file names, and number the zip file as the largest number incremented by one
    zip_file_number = 0
    for file_name in backup_folder_file_list:
        zipfile_numbering_pattern_obj = re.compile(r'_\d+') # Make use of regex, return the last number in the file (ex: _10)
        mo = zipfile_numbering_pattern_obj.search(file_name) 
        current_number = int(mo.group()[1:])
        if current_number > zip_file_number:
            zip_file_number = current_number
    zip_file_name = folder_name + "_" + str(zip_file_number + 1)   

# Write working directory and it's contents into a zip file
with zipfile.ZipFile(backup_folder_path / (zip_file_name + ".zip"), 'w') as zip_file: # Open a new zip file in 'w' mode. The close() method is automatically called after leaving the with statement's block
    for folder_name, subfolders, filenames in os.walk(folder_path): # Walk the folder tree and .write() each file, specifying its relative path
        for filename in filenames:
            file_path = Path(folder_name) / filename
            zip_file.write(file_path, arcname=file_path.relative_to(folder_path))

print('Created backup zip file: ' + str(backup_folder_path / (zip_file_name + '.zip')))
    
