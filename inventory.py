import collections

def display_inventory(inventory):
    print('Inventory:')
    sum=0
    for each in inventory:
        print(inventory[each] , each)
        sum += inventory[each]
    print("Total number of items: ", sum,"\n")


def add_to_inventory(inventory,added_items):
    for each in added_items:
        new_item=True
        for item in list(inventory):
            if each == item:
                new_item=False
        if new_item:
            inventory[each] = 1
            added_items.remove(each)
            new_item=False

    for item in inventory:
        for  each in added_items:
            if item == each:
                inventory[item] += 1
            
    return inventory

#szét kéne még szedni h rövidebb legyen, NINCS SORREND RENDESEN, CSAK A SZIMPLA FORMÁZÁS,FURÁKRA NEM JÓ狼心狗肺
def print_table(inventory,order="normal"):
    #Getting the max lengthed string from our inventory
    max_length=0
    for each in inventory:
        if len(each)>max_length:
            max_length=len(each)

    print('Inventory:')
    print('count'.center(max_length),'item name'.center(max_length))

    #printing the line:
    for i in range(2*max_length):
        print('_',end="")
    print('_')
    sum=0

    if order == "count,asc":
        od = collections.OrderedDict(sorted(inventory.items(), key=lambda t: t[1]))
        #print(od)
        for k, v in od.items():
            print(str(v).rjust(max_length),str(k).rjust(max_length))
            sum += v
    elif order == "count,desc":
        vd = collections.OrderedDict(sorted(inventory.items(), key=lambda t: t[1], reverse=True))
        #print(vd)
        for f, d in vd.items():
            print(str(d).rjust(max_length),str(f).rjust(max_length))
            sum += d
    elif order == "normal":
        for each in inventory:
            print(str(inventory[each]).rjust(max_length) , str(each).rjust(max_length))
            sum += inventory[each]
    
    #printing the line:
    for i in range(2*max_length):
        print('_',end="")
    print('_')
    print("Total number of items: ", sum,"\n")


def import_inventory(inventory,filename='import_inventory.csv'):
    givenFile=open(filename,'r')
    data=[]
    newInv=[]
    firstLine=givenFile.readline()
    #print(firstLine)
    for line in givenFile:
        data.append(line)
    #print(data)
    for each in range(len(data)):
        darab=data[each]
        vmi=[]
        vmi=darab.split(',')
        for times in range(int(vmi[1])):
            newInv.append(vmi[0])
    #print(newInv)
    inventory=add_to_inventory(inventory,newInv)


def export_inventory(inventory,filename="export_inventory.csv"):
    newFile=open(filename,'w')
    newFile.write("item_name,count\n")
    for item in inventory:
        newFile.write(str(item)+","+str(inventory[item])+"\n")


def proba(inventory):
    od = collections.OrderedDict(sorted(inventory.items(), key=lambda t: t[1]))
    print(od)
    for k, v in od.items():
        print(v,k)

    vd = collections.OrderedDict(sorted(inventory.items(), key=lambda t: t[1], reverse=True))
    print(vd)
    for f, d in vd.items():
        print(d,f)



#KELL MAIN
def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    
    display_inventory(inv)
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)
    print_table(inv,"count,desc")
    import_inventory(inv)
    display_inventory(inv)
    export_inventory(inv)
    #proba(inv)

if __name__ == '__main__':
    main()

"""
for key in sorted(inv.values()):
    print(key)
vmi="fsf,dsfs,ds"
db=[]
db=vmi.split(',')
print(vmi.split(','))
print(db)
"""

