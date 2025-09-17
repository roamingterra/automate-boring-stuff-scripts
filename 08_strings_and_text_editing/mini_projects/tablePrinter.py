# Takes a list of lists of strings and displays it in a well-organized table with each column right- justified

def printTable(data):
    #Funtion code
    colWidths = [0]*len(data) #Created list to eventually store longest
                              #string from each sub list in TableData
    #Store longest string from each sublist into our new list
    for x in range(len(data)):
        for i in range(len(data[x])):
            if len(str(data[x][i])) > len(str(colWidths[x])):
                colWidths[x] = data[x][i]

    #Convert set of longest strings into integers            
    for t in range(len(colWidths)):
        colWidths[t] = len(colWidths[t])

    #Print data into three columns, right adjusted according to longest string in each column
    for y in range(len(data[0])):#4
        for j in range(len(data)):#3
            if j == 0:
                print(data[j][y].rjust(colWidths[j]) + ' ', end='')
            elif j == 1:
                print(data[j][y].rjust(colWidths[j]) + ' ', end='')
            elif j == 2:
                print(data[j][y].rjust(colWidths[j]) + ' ')
                

TableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(TableData)
