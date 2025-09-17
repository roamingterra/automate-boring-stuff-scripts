import re

def stripR(phrase, b=None):
    if b==None:
        stripR = re.compile(r'(\w+ +)+')
        mo = stripR.search(phrase)
        print(mo.group())
    else:
        mo1 = re.sub(b, "", phrase)
        mo2 = re.sub(" ", "", mo1) 
        print(mo2)
      
stringToStrip = '   xoxo love xoxo  '
b = ''
stripR(stringToStrip, b)

