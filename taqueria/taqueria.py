from sys import exit

# items dictionary
items = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

# declare total
total = 0.00

#while condition is true
while True:
    try:
        # ask user for input
        uinpt = input("Item: ").lower().strip()
        while uinpt not in items:
            uinpt = input("Item: ").lower().strip()

        #add item to total
        total += items.get(uinpt)
        # print total
        print(f"${total:.2f}")

    #except if there's an EOFerror or KeyError
    except EOFError or KeyError:
        print()
        # exit with code 0
        exit(0)
