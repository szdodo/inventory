inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print('Inventory:')
    sum=0
    for each in inventory:
        print(inventory[each] , each)
        sum += inventory[each]
    print("Total number of items: ", sum,"\n")
        

def add_to_inventoryLL(inventory,added_items):
    exist=[]
    for each in added_items:
        for item in list(inventory):
            if item == each:
                exist=True
                #print(each,item,"elso")
                #inventory[item] = inventory[item]+1
                #print(each,inventory[each])
           #else
                #print(each,item,"masodik")
                #inventory[each] = 1
                #print(each,inventory[each])
       
    for each in added_items:
        print(4)
        print(each, )
        if exist:
            inventory[each] += 1
        else:
            inventory[each] = 1
    return inventory

def add_to_inventory(inventory,added_items):
    for item in inventory:
        for  each in added_items:
            if item == each:
                inventory[item] += 1
    
    for each in added_items:
        new_item=True
        for item in list(inventory):
            if each == item:
                new_item=False
        if new_item:
            inventory[each] = 1

    return inventory


display_inventory(inv)
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
