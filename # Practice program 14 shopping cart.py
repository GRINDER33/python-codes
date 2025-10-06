# Practice program 14 shopping cart

items = []
prices = []
quantities = []
total = 0
while True:
    try:
        item = input("Enter the item to buy (q to quit for cart summary): ") 
        if item.lower() == "q":
           break
        else:
            price = float(input(f"Enter the price of a {item}: $"))
            prices.append(price)
            items.append(item)
            quantity = int(input(f"Enter the amount of {item} you would like to buy: ")) 
            quantities.append(quantity)
    except ValueError:
            print("Invalid input. Enter numbers") 
                      
    

print("----- YOUR CART -----")

for i in range(len(items)):
     item_total = prices[i] * quantities[i]
     total += item_total
     print(f"{items[i]} x {quantities[i]} = ${item_total:,.2f}")
print("---------------------")
print(f"Your cart total is : ${total:,.2f}")