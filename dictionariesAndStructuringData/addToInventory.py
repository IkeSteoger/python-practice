from inventory import displayInventory

def addToInventory(inventory, addedItems):
    for k in range(len(addedItems)):
        inventory.setdefault(addedItems[k], 0)
        inventory[addedItems[k]] += 1
    return(inventory)

inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)