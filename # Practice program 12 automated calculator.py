# Practice program 12 automated calculator

while True:
    try:
        num1 = float(input("Enter the first number: "))
        opr = input("Enter the operator: ")
        num2 = float(input("Enter the second number: "))

        if opr == "+":
            result = num1 + num2
        elif opr == "-":
            result = num1 - num2
        elif opr == "*":
            result = num1 * num2 
        elif opr == "/":
            if num2 == 0:
                print("Error: Division by zero isn't allowed.")  
                continue
            result = num1 / num2
        elif opr =="^":
            if num1 > 1e6 or num2 > 1e3:   #Prevent the code from crashing when a large number is entered
                print("Error : Number too large for exponentation!")
                continue
            result = num1 ** num2
        elif opr =="%":
            result = num1 % num2
        else:
            print("Invalid operation please enter ( + or - or * or / or ^ or % ).")
            continue
        print(round(result, 3))
    except ValueError:                      #re-runs the program when faced with an error of invalid entry
        print("Invalid input. Please enter the value again.")
    except OverflowError:                   #re-runs the program when faced with an error of too large value
        print("Number too large.")
        
    exit_fnc = input("Press q to exit or enter to continue: ")   
    if exit_fnc.lower().startswith("q"):
        break
