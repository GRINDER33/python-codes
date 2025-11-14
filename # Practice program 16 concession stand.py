# Practice program 16 concession stand

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []
quantities = []
total = 0

print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("----------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None: 
        while True:
                try:
                    quantity = int(input(f"Enter the amount of {food} would like to have: "))
                    if quantity <= 0:
                        print("Please enter a value greater than zero")
                        continue
                    cart.append(food)
                    quantities.append(quantity)
                    break
                except ValueError:
                        print("Invalid value entered. please enter again")

    else:
        print("Item not found! Please choose something from the menu.")
print()
print("----------- YOUR CART -----------")
print()
for i in range(len(cart)):
    quantity = quantities[i]
    item_total = menu[cart[i]]*quantity
    total += item_total
    print(f"{cart[i]:8}  | ${menu[cart[i]]:,.2f} x {quantity} = ${item_total:,.2f}")
print()
print("---------------------------------")
print(f"Your cart total is : ${total:,.2f}")
print("---------------------------------")