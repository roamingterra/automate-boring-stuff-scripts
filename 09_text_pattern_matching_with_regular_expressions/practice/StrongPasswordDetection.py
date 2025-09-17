import re

def strongPassDetect(password):
    eightCharactersRegex = re.compile(r'.{8,}') 
    upperCaseRegex = re.compile(r'[A-Z]')
    lowerCaseRegex = re.compile(r'[a-z]')
    atLeastOneDigitRegex = re.compile(r'\d')

    if eightCharactersRegex.search(password) == None:
        return False
    elif upperCaseRegex.search(password) == None:
        return False
    elif lowerCaseRegex.search(password) == None:
        return False
    elif atLeastOneDigitRegex.search(password) == None:
        return False
    else:
        return True

print('Create a password')
userPassword = input()
if strongPassDetect(userPassword) == True:
    print('Strong password')
else:
    print('Weak password')
