#! Python3
# selectiveCopy - This program walks through a folder tree, and
# searches for files with .pdf and .jpg file extensions.
# These files are then copied and pasted to another folder created by
# the program, to be located in the same location as the original folder

import shutil, os

# Create new folder in same location

resultFolder = os.path.abspath('C:\\testFolderFiles')

if not os.path.exists(resultFolder):
    os.mkdir(resultFolder)

# Walk through folder tree

for folderName, subfolders, filenames in os.walk('C:\\testFolder'):

    for file in filenames:
        
        if (file.endswith('.pdf') | file.endswith('.jpg')):
            print(file + ' sent to ' + resultFolder + '\n')
            filePath = os.path.join(os.path.abspath(folderName), file)
            shutil.copy(filePath, resultFolder)
