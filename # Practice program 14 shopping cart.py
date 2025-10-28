# Practice program 14 shopping cart

import time

def slow_print(text, delay=0.02):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()


items = []
prices = []
quantities = []
total = 0
while True:
    try:
        item = input("Enter the item to buy (q to quit for cart summary): ") 
        if item.lower() == "q":
           break

        # Loop until a valid price is entered
        while True:
            try:
                price = float(input(f"Enter the price of {item}: $"))
                break
            except ValueError:
                print("Invalid price. Enter a number.")

        # Loop until a valid quantity is entered
        while True:
            try:
                quantity = int(input(f"Enter the quantity of {item}: "))
                break
            except ValueError:
                print("Invalid quantity. Enter a number.")

        items.append(item)
        prices.append(price)
        quantities.append(quantity)
                      
    except ValueError:
            print("Invalid input. Enter numbers") 

    

print("----- YOUR CART -----")

for i in range(len(items)):
    item_total = prices[i] * quantities[i]
    total += item_total
    slow_print(f"{items[i]} x {quantities[i]} = ${item_total:,.2f}")
print()
print("---------------------")
slow_print(f"Your cart total is : ${total:,.2f}")