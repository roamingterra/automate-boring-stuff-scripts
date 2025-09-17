#! Python3
# fillingInTheGaps - This program finds files with a given prefix in a folder
# such as spam001.txt and spam002.txt, and renames them if there are gaps in
# the numbering (ex: spam001.txt and spam003.txt)

import re, os, shutil

# Regex declarations
regex1 = re.compile(r'[a-z,A-Z]*')
regex2 = re.compile(r'\d{3}')

# declaration of some variables
selectedFolder = 'C:\\spam'
previous = 0

# walk-through of folder
for foldername, subfolders, filenames in os.walk(selectedFolder):
    for filename in filenames:

        # display file path
        print(selectedFolder + '\\' + filename, end='')
        
        # match numbered part of file
        go2 = regex2.search(filename)
        mo2 = go2.group()
        strip = int(mo2.lstrip("0"))
        #print(strip)
        
        if (previous != 0) and (strip != previous + 1 ):
            # Display a message to notify user that the current file will be renamed
            print(' ---> Renaming file')
            
            # match first part of file
            go1 = regex1.search(filename)
            mo1 = go1.group()
            leadingName = str(mo1)

            # rename file
            strip = str(previous + 1)
            x = strip.zfill(3)
            shutil.move(selectedFolder + '\\' + filename, selectedFolder + '\\' + leadingName + x + '.txt')

        # variable representing the previous file number gets assigned the new file number    
        previous = int(strip)
        print('\n')
        
        

