principal = 0
interest = 0 
time = 0

while True:
    while True:
        try:
            principal = float(input("Enter the Principal amount: "))
            if principal < 0:
                print("Principal cant be less than zero")
            else:
                break
        except ValueError:
            print("Invalid value entered. Please enter the value again")
    while True:
        try:
            interest = float(input("Enter the Interest Rate: "))
            if interest < 0:
                print("Interest cant be less than zero")
            else:
                break
        except ValueError:
            print("Invalid value entered. Please enter the value again")
    while True:
        try:
            time = int(input("Enter the amount of time for the intrest to be calculated: "))
            if time < 0:
                print("Time cant be less than zero")
            else:
                break
        except ValueError:
            print("Invalid value entered. Please enter the value again")
    total = principal * pow(1 + interest / 100, time)
    print(f"The Balance after {time} Years would be ${total:,.2f}")

    show_yby = input("Do you want the year by year list?: ").lower()
    if show_yby.startswith('y'):
        print("\nYear-by-year balance:")
        for year in range(1, time + 1):
            balance = principal * pow(1 + interest / 100, year)
            print(f" Year {year}: ${balance:,.2f}")
    else:
        print("Skipping year-by-year balance...")

    x = input("Press q to exit or enter to stay: ")
    if x.lower() == "q":
        break
    