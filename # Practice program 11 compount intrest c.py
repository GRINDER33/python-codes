# Practice program 11 compount intrest calc

import time

principal = 0
interest = 0 
time_ = 0

while True:
    time.sleep(0.3)
    while True:
        try:
            principal = float(input("Enter the Principal amount: "))
            if principal < 0:
                print("Principal cant be less than zero")
                time.sleep(0.2)
            else:
                break
            time.sleep(0.3)
        except ValueError:
            print("Invalid value entered. Please enter the value again")
            time.sleep(0.2)
    while True:
        try:
            interest = float(input("Enter the Interest Rate: "))
            if interest < 0:
                print("Interest cant be less than zero")
                time.sleep(0.2)
            else:
                break
            time.sleep(0.3)
        except ValueError:
            print("Invalid value entered. Please enter the value again")
            time.sleep(0.2)
    while True:
        try:
            time_ = int(input("Enter the amount of time for the intrest to be calculated: "))
            if time_ < 0:
                print("Time cant be less than zero")
                time.sleep(0.2)
            else:
                break
            time.sleep(0.3)
        except ValueError:
            print("Invalid value entered. Please enter the value again")
            time.sleep(0.2)
            
    total = principal * pow(1 + interest / 100, time_)
    print(f"The Balance after {time_} Years would be ${total:,.2f}")
    time.sleep(0.3)

    show_yby = input("Do you want the year by year list?: ").lower()

    if show_yby.startswith('y'):
        print("\nYear-by-year balance:")

        for year in range(1, time_ + 1):
            balance = principal * pow(1 + interest / 100, year)
            time.sleep(0.3)

            yby_list = f" Year {year}: ${balance:,.2f}"
            for letter in yby_list:
                print(letter, end="", flush=True)
                time.sleep(0.05)
            print()
    else:
        time.sleep(0.3)
        print("Skipping year-by-year balance...")

    time.sleep(0.3)
    x = input("Press q to exit or enter to stay: ")
    if x.lower() == "q":
        break
    