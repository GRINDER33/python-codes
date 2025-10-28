# Practice program 6 finding the hypotnuse 

import math

perpendicular = float(input("Enter the pependicular of the Triangle: "))
base = float(input("Enter the base of the Triangle: "))

hypotnuse = math.sqrt(pow(perpendicular,2) + pow(base,2))
print(f"The hypotnuse of the Triangle is: {round(hypotnuse,2)}")