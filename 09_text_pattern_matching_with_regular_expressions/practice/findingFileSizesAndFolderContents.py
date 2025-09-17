import os

totalSize = 0
for filename in os.listdir(r"C:\Users\Daniel\Documents\Monty Python's Wizarding School for Codecraft and Coding Arts"):
	totalSize = totalSize + os.path.getsize(os.path.join(r"C:\Users\Daniel\Documents\Monty Python's Wizarding School for Codecraft and Coding Arts", filename))

	
print(totalSize)

#os.path.getsize() when called on for a folder, will give the size
#in bytes of the folder only, and not of it's contents.
#In other words, the amount of bytes is required for
#that folder, and only that folder, to exist,
#regardless of any files within the folder.

#In order to get the size of a folder's contents,
#you must use the code written above, loop through all
#of the folder's contents.
