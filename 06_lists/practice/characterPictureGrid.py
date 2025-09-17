grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

j=0
for j in range(len(grid[j])):
    for i in range(len(grid)):
        if i < int((len(grid)-1)):
            print(grid[i][j], end='')
        else:
            print(grid[i][j])

#for j in range(6):
    #for i in range(9):
        #if i < 8:
            #print(grid[i][j], end='')
        #else:
            #print(grid[i][j])
    
    



