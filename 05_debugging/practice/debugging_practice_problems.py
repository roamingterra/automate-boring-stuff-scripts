# Chapter 5: Debugging, practice problems

# Q1 
# spam = 9
# assert spam >= 10

# Q2
# eggs = 'hello'
# bacon = 'HELLO'
# assert eggs.lower() != bacon.lower()

# Q3
# assert False

# Q4
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.debug('Start of program')

# Q5
# import logging
# logging.basicConfig(filename='programLog.txt' ,level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.debug('Start of program')

# Q6
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.debug('Some minor code and debugging details.')
# logging.info('An event happened.')
# logging.warning('Something could go wrong.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to recover!')

# Q7
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)
# logging.debug('Some minor code and debugging details.')
# logging.info('An event happened.')
# logging.warning('Something could go wrong.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to recover!')

# Q8
# print statements are harder to remove once development is complete, because we sometimes need print
# statements in our regular code. This makes it confusing to parse through the debugging print statements
# and the print statements needed for our program logic. Logging messages also provide more details like time stamps.

# Q9
# Step Over: Will execute the next line of code, but will skip over lines of code in a function call (they will be executed,
# but the debugger will not pause for each line of code in a function call)
# Step In: Will execute the next line of code, then pause. This includes executing lines of code in a function call
# Step Out: Will execute all lines of code in a current function call, then step out of the function and pause at the next line of code

# Q10
# Clicking the continue button will cause the program to execute normally until it terminates, or until a break point is reached

# Q11
# A break point is a line of code that you tell the debugger to pause at after executing normally. Click on continue in the debugger to have the code execute
# until it reaches your break point

# Q12
# In IDLE, while the debugger is running, navigate to your python program window, right click on your desired line of code, and select "set breakpoint"


