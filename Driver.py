# Evan Johanns
# stock sales assignment 8

from StackandQueue import Stack, Queue

choice = 0

while choice != 1 or choice != 2: # the loop here is broken and i am not sure how to fix it, i have spent the lst 4 hours on this loop alone trying to figure out why it wont work
    print("""Which method would you like to use?
    1. Stack(FIFO)
    2. Queue(LIFO) """)
    choice = int(input(">> ")) # after creating these Linked lists it then somehow resets the 'choice' variable to 0 and reruns the loop, it refuses to exit even if the choice is now 1 or 2
    if choice == 1:
        Num_stock = Stack()
        Price = Stack()

    else:
        Num_stock = Queue()
        Price = Queue()



total_stock = 0
total_profit = 0.0
total_value_sold = 0


menu_choice = 0
while menu_choice != 5:
    print("""Please enter the number of the action you want.
    1. Add stock
    2. Sell stock
    3. Check Total
    4. Check Profit
    5. Exit""")
    menu_choice = int(input(">> "))
    if menu_choice == 1:
        qty = int(input("How much is being added?: "))
        price = int(input("How much does each share cost?: "))
        total_cost = float(price * qty)
        Num_stock.push(qty)
        Price.push(price)

        total_stock += qty
    elif menu_choice == 2:
        qty_popped = Num_stock.pop()
        price_of_pop = Price.pop()
        print(f"Removed {qty_popped} from stock. ")











