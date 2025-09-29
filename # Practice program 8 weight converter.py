# Practice program 8 weight converter

weight = float(input("Enter weight: "))
unit = input("KiloGrams or Lbs? (K OR L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs"
    print(f"Your weight in {unit} is: {round(weight, 4)}{unit}") 
elif unit == "L":
    weight /= 2.205
    unit = "Kgs"
    print(f"Your weight in {unit} is: {round(weight, 4)}{unit}") 
else:
    print(f"{unit} was not valid")
  
