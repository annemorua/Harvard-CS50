menu = {"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}

#An empty conuter is started to add the price of the items that the user writes.
total = 0

while True:
    try:
        #It has to be made titled because that's how it is the dictionary.
        item = input("Item: ").title()

        #If the item is on the menu, the price is taken and a variable is assigned to it.
        if item in menu:
            price = menu[item]

            total = total + price

            print(f"Total: ${total:.2f}")

    except EOFError:
        break
