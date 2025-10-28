# Practice program 7 basic operations calculator

num1 = float(input("Enter the first number: "))
opr = input("Enter operator (+ - * /): ")
num2 = float(input("Enter second number: "))

if opr == "+":
    result = num1 + num2
    print(round(result, 3))
elif opr == "-":
    result = num1 - num2
    print(round(result, 3))
elif opr == "*":
    result = num1 * num2 
    print(round(result, 3))
elif opr == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print("ERROR")