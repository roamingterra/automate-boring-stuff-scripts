import re

exampleRegex = re.compile('(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)
mo = exampleRegex.search('RoboCop eats apples.')
print(mo.group())
