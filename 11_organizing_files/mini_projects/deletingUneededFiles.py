#! Python3
# deletingUnneededFiles - This program walks through a folder tree and
# searches for files that are larger than 1MB. It then prints the absolute
# paths of those files and sends them to the recycling bin

import shutil, os, send2trash

selectedFolder = 'C:\\bigSmallFolder'

for folderName, subfolders, filenames in os.walk(selectedFolder):
    for file in filenames:
            currentFile = os.path.join(selectedFolder, file)
            if (os.path.getsize(currentFile)>1000000):
                print(currentFile + ' was sent to trash')
                send2trash.send2trash(currentFile)
    
            
