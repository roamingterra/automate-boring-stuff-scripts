stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    totalItems = 0
    for i, j in inventory.items():
        print( str(j) + ' ' + i)
        totalItems = totalItems + j
    print('Total number of items: ' + str(totalItems))

displayInventory(stuff)

