import re

exampleRegex = re.compile('([A-Z][a-z]*\sNakamoto)')
print(exampleRegex.findall('Satoshi Nakamoto and Mr. Nakamoto and Daniel Nakamoto'))
#print(mo)
