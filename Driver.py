# Evan Johanns
# stock sales assignment 8

from StackandQueue import Stack, Queue

one = 1
method_choice = 0
while method_choice != 1 or method_choice != 2:
    print("""Which method would you like to use?
    1. Stack(FIFO)
    2. Queue(LIFO)""")
    method_choice = int(input(">>"))
    if method_choice == 1:
        Num_stock = Stack()
        Price = Stack()
        print(" hi ")
        # Num_stock.push(10)
        # print(Num_stock)
    else:
        Num_stock = Queue()
        Price = Queue()
        print(" hello ")

total_inventory = 0
total_profit = 0.0
total_value_sold = 0


menu_choice = 0
while menu_choice != 5:
    print("""Please enter the number of the action you want.
    1. Add stock
    2. Sell stock
    3. Check Total
    4. Check Profit""")

    if menu_choice == 1:
        qty = int(input("How much is being added?: "))
        price = int(input("How much does each share cost?: "))
        total_cost = float(price * qty)
        Num_stock.push(qty)






