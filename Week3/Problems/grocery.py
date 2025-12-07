#A diccionary is created where the fruit and the quantity are saved.
lst = {}

while True:
    try:
        #Makes it uppercase because the problem asked for it that way.
        product = input("").upper()

        #If the product is not in the list, adds it.
        if product in lst:
            #If the product was already there, now add the number of times the user types it.
            lst[product] = lst[product] + 1

        else:
            #If the product was not in list, now adds it.
            lst[product] = 1

    except EOFError:
        break

#Sort the list items in alphabetical order.
sortlst = sorted(lst.items())

#For each i being the item and for each c being the quantity, print first the quantity and then the item.
for i, c in sortlst:
    print(c, i, sep=" ")
