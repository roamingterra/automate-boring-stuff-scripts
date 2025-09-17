def commaCode (list):
    for i in range(len(list)):
        if i == int((len(list)-1)):
            print('and ' + list[i])
        else:
            print(list[i] + ', ', end = '')

spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)

        
        
