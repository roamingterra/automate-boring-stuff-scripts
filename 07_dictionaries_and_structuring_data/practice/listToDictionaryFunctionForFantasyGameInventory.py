def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)): #Loops through list of dragonLoot
        if addedItems[i] in inventory: #Why is it inventory and not inventory.items
            inventory[addedItems[i]]+=1
        else:
            inventory.setdefault(addedItems[i], 1)
    return inventory

def displayInventory(inventory):
    print('Inventory:')
    totalItems = 0
    for i, j in inventory.items():
        print( str(j) + ' ' + i)
        totalItems = totalItems + j
    print('Total number of items: ' + str(totalItems))
        

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

