stuff = {'rope': 1, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def showInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))        

def addToInventory(inventory, items):
    for it in items:
        inventory[it] = inventory.get(it, 0) + 1 
        # inventory.get(it, str(it)) 

def gameDemo():
    showInventory(stuff)
    print(f"Slayed Red Dragon. Adding dragon\'s loot: {loot} to inventory")
    addToInventory(stuff, loot)
    print("Done. Inventory Updated.")
    showInventory(stuff)

if __name__ == '__main__':
    print('''Dear Alice,
    
    Eve's cat has been arrested for catnapping.
    And extortion.

    Sincerely,        
    \tBob''')

