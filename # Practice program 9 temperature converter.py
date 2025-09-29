# Python program 9 temperature converter

temp = float(input("Enter the temperature: "))
unit = input("Is the temperature in celcius or faremheit? (C/F): ")

if unit == "C":
    temp = round((temp * 9/5) + 32, 2)
    print(f"The temperature in Farenheit is {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5/9)
    print(f"The temperature in Celcius is {temp}°C")
else:
    print("unit is invalid")
