#This is a python training file 
# print("pizza")
# print("its really good")

# Varial = a container for a value (string , integer , float , boolean)
# A variable behaves as if it was the value it contains 


# Strings
first_name = "GRINDER"
food = "Pizza"
email = "nigga@gmail.com"
# print(f"hello {first_name}")
# print(f"You like {food}")
# print(f"your email is: {email}")


# Integers 
age = 16
quantity = 3 
num_of_students = 30
# print(f"you are {age} years old")
# print(f"you are buying {quantity} items")
# print(f"Your class has {num_of_students} students")


# Float
price = 10.99
gpa = 3.2
distance = 5.5
# print(f"the price is ${price}")
# print(f"your gpa is: {gpa}")
# print(f"you ran {distance}Km ")


# Boolean
is_student = True
for_sale = False
is_online = True
# if for_sale:
#     print("That item is for sale")
# else:
#     print("That item is not for sale ")


#Type Casting = the process of converting a variable from one datatype to another
#    str(), int(), float(), bool()
name = "GRINDER"
age = 16
gpa = 3.2
is_student = True
# print(type(is_student))
# name = bool(name)
# print(name)


#input() = A function that prompts the user to enter data 
#          Returns the entered data as a string

# name = input("What is your name?:")
# age = int(input("How old are you?:"))
age = age+1
# print(f"hello {name}")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age} years old")


#  Arithmatic Operators

friends = 10

# friends = friends + 1
# friends += 1   #augmented assignment operator
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 3

# print(remainder)


#Built in math functions

x = 3.14
y = 4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(4, 3)
# result = max (x, y, z)
# result = min (x, y, z)

# print(result)


# Import functions

import math

x = 9

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)


# print(result)


# If statement = do something only when the condition is true 
# else do something else
##### EX 1 #####
# age = int(input("Enter your age "))
# if age >=100:
#     print("You are too old to sign up")
# elif age >= 18:
#     print("You are now signed up")
# elif age < 0:
#     print("You are not born yet")
# else:
#     print("You must be 18+ to sign up")

##### EX 2 #####
# response = input("Would you like food (Y/N)?: ")
# if response == "Y" or "y":
#     print("Have some food ")
# else:
#     print("no problem not today then")

##### EX 3 #####
# name = input("Enter you name: ") 
# if name == "":
#     print("HEYY MFR PUT SOMETHING!")
# else:
#     print(f"Helo {name}")


# Boolean with if statements

##### 
for_sale = True
# if for_sale:
#     print("This item is for sale")
# else:
#     print("Tis item is not for sale")

#####
is_online = True
# if is_online:
#     print("The use is online")
# else:
#     print("The user is offline")


# Logical Operators = evaluate multiple condition (or, and, not)

##### OR example #####
# temp = 25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

##### and Not example #####
temp = 28
is_sunny = True

# if temp >= 28 and is_sunny:
#     print("It is hot outside")
#     print("It is sunny")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside")
#     print("It is sunny")
# elif 28 < temp > 0 and is_sunny:
#     print("It is warm outside")
#     print("It is sunny")
# if temp >= 28 and not is_sunny:
#     print("It is hot outside")
#     print("It is cloudy")
# elif temp <= 0 and not is_sunny:
#     print("It is cold outside")
#     print("It is cloudy")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is warm outside")
#     print("It is cloudy")


# Conditional expression = A short cut for if else statement  ## X if condition else Y

num = 6
a = 6
b = 7
age = 13 
temp = 30
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "even" if num % 2 == 0 else "Odd"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age > 18 else "Child"
# weather = "Hot" if temp > 20 else "It is cold" 
# access_role = "Full access" if user_role == "admin" else "Limited access"
# print(access_role)


# String methods 

# name = input("Enter you name: ")
# phone_number = input("Enter your phone number")

# result = len(name)
# result = name.find(" ")
# result = name.rfind("o")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-", " ")
# print(result)


# String indexing = accesing elements of a sequence useing the []
#        [star : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[4])
# print(credit_number[0 : 4])
# print(credit_number[5 : 9])
# print(credit_number[5 :])
# print(credit_number[-6])
# print(credit_number[::2])
# last_digits = credit_number[-4:]
# credit_number = credit_number[::-1]
# print(f"XXXX-XXXX-XXXX-{credit_number}")\


# Format specifiers = {value:flags} format a value based on the inserted flags

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# print(f"Price 1 is ${price1:+,.3f}")
# print(f"Price 2 is ${price2:+,.3f}")
# print(f"Price 3 is ${price3:+,.3f}")


# While loop = execute some code while some condition is true

# name = input("Enter you name: ")

# while name == "":
#     print("You did not ener your name")
#     name = input("Enter you name")
# print(f"Welcome {name}")


# food = input("Enter a food you like (press q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (press q to quit): ")
# print("bye")

# num = int(input("Enter a number between 1-10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1-10: "))
# print(f"Your number is {num}")


#   For loops = execute a block of code for fixed number of times
#               can be used on a string, range, sequence, second number is exclusive

credit_card = "1234-5678-9012-3456"
# for i in range(1 , 21):
#     if i == 13:
#         continue
#     print(i)


# Nested loops = a loop within another loop (outer , inner)
#                Outer Loop:
#                    Inner Loop:

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter the symbol to use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()


# Collections = single variable containing multiple values
# List = [] ordered and changeable. Dulicates OK
# Set = {} unordered and immutable, but Add/Rmove OK, NO Duplicates
# Tuple = () ordered and unchangeable. Dulicates OK. FASTER

fruits = ["Apple", "Orange", "Banana", "Coconut"]

# print(dir(fruits))
# print(len(fruits))
# print("Pineapple" in fruits )
# fruits[0]= "Pinapple"
# fruits.append("Pineapple")
# fruits.remove("Apple")
# fruits.insert(0, "Pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("Apple"))
# print(fruits.count("Apple"))


# print(fruits[::-1])
# for x in fruits:
#     print(x)


# Dictionaries = a collection of {key : value} pairs
#                ordered and changable. no dupliccates

capitals = {"USA":"Washinton D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("The capital exists")
# else:
#     print("The capital doesnt exist")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in keys:
#     print(key)

# values = capitals.values()
# for value in values:
#     print(value)

# item = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")


# Random module

import random
low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
# random.shuffle(cards)

# print(cards)


#Functions

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

# happy_birthday("Bro", "20")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due: {due_date}")

# display_invoice("Bro", 42.59, "01/01")


# return = statement used to end a function 
#          and send the result back to the caller

def add(x, y):
    z = x + y
    return z
def sub(x, y):
    z = x - y
    return z
def multi(x, y):
    z = x * y
    return z
def div(x, y):
    z = x / y
    return z

# print(div(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" "+ last

full_name = create_name("bro", "jurmu")
# print(full_name)


# Default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional 2. DEFAULT 3. keyword 4. arbitary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

import time

def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

# count(30, 15)

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# hello("Hello", title= "Mr.", last = "Squarepants", first = "Spongebob")


# *args    = allows u to pass multiple non-key arguments
# **kwargs = allows u to pass multiple keyword arguments
#            * unpacking operator

def add(*args):
    total= 0
    for arg in args:
        total += arg
    return total

# print(add(1,2,3,4,5,6,7,8,9,10))

def display_name(*args):
    for arg in args:
        print(arg, end = " ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# **kwargs

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_address(street="123 Fake St.",
#                     apt="100",
#                     city="Detroit",
#                     state="MI",
#                     zip="54321")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III",
#                 street="123 Fake St.",
#                 apt="#100",
#                 pobox="1001",
#                 city="Detroit",
#                 state="MI",
#                 zip="54321")

# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

my_dictionary = {"A":1 , "B":2, "C":3}

# for key, value in my_dictionary.items():
#     print(f"{key}: {value}")


# Memberships operators = used to test whether a value or variable is found in a sequence
#                         (string, list, set, or dictionary) 
#                         1. in 
#                         2. not in 

students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of the student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not a student")

grades = {"Sandy":"A",
          "Spongebob":"B", 
          "Squidward":"C", 
          "Patrick":"D"}

# student = input("Enter the name of the student: ")

# if student in grades:
#     print(f"{student}'s grades is {grades[student]}")
# else:
#     print(f"{student} was not found")


# List compreshension = A concise way to create lists in python 
#                       Comact and easier to read than traditional loops
#                       [exression for value in iterables if condition]

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

# print(squares)

fruits = ["Apple", "Orange", "Banana", "Coconut"]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruits)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

# print(even_nums)

# grades = {85, 42, 79, 90, 56, 61, 30}
# passing_grades = [grade for grade in grades if grade >= 60]

# print(passing_grades)


# Match-case statement (switch) = an alternative to using many 'elif' statements
#                                 Execute some code if value matches a 'case'
#                                 Benefits: Cleaner and syntax more readable 

def is_weekend(day):
    match day: 
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Not a valid day"   
# print(is_weekend("Monday"))


# Modules = a file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program to reusable seperate files 

import math
# import math as m
# from math import pi

a, b, c, d, e = 1, 2, 3, 4, 5

# print(math.e ** a)
# print(math.e ** b) 
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)


# Variable scope = Where a variable is visible and accessible
# Scope resolution = "LEGB" Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1 
    print(x)
    def func2():
        x = 2
        print(x)
    func2()
# func1()


# if __name__ == __main__: (this script cant be imported OR run standalone)
#                          Funtions and classes in this module can be reused
#                          without the main block of code executing
#                          Good practice (code is modular,
#                                         hels readability,
#                                         leaves no global variable,
#                                         avoid unintended executions)

# def main():
    # Your program goes here

#   if __name__ == '__main__':
#     main()


# Object = A "bundle" of related attributes (variables) and methods (funtions)
#          Ex. phone, cup, book
#          You need a "class" to vreate many objects
# Class = (blueprint) used to design the structure and layout of an object 

from car import Car
car1 = Car("MERQADES", 2025, "Blue Black", False)
car2 = Car("SF-25 tractor", 2025, "Red", True)
car3 = Car("Slow Bull", 2025, "Blue", True)

# car1.describe()
# car3.describe()


# Class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

# Student1 = Student("Spongebob", 30)
# Student2 = Student("Patrickḍ", 35)
# Student3 = Student("Squidward", 55)
# Student4 = Student("Sandy", 27)

# print(f"My graduating class of {Student.class_year} has {Student.num_students} Students")
# print(Student2.name)
# print(Student2.age)
# print(Student.class_year)

# print(Student.num_students)


# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
     
#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")
    
# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")
# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Mouse(Animal):
#     def speak(self):
#         print("SQUEEK!")

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")

# cat.speak()                   


# Multiple inheritance = inherit from more than one parent class
#                        C(A, B)
# Multi level inheritance = inherit from a parent which inherits from another parent
#                           C(B) <- B(A) <- A

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name}l is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# hawk.eat()


# Super() = Funtion used in a child class to call methods from a parent class (superclassḍḍ)
#           Allows you to extend the functionality of the inherited methods

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
    
#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius
    
#     def describe(self):
#         Shape.describe(self)
#         print(f"It is a circle with the area of {math.pi*self.radius**2:.1f} cm^2")

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width

#     def describe(self):
#         Shape.describe(self)
#         print(f"It is a square with the area of {self.width**2:.1f} cm^2")
        
# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height

#     def describe(self):
#         Shape.describe(self)
#         print(f"It is a triangle with the area of {1/2*self.width*self.height:.1f} cm^2")       

# circle = Circle(color = "Red",is_filled =  True,radius =  5)
# square = Square(color = "Blue",is_filled =  False,width =  6)
# triangle = Triangle(color = "Yellow",is_filled =  True,width =  7, height = 8)

# triangle.describe()


# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = many 
#                morphe = Form
#               
#                TWO WAYS TO ACHEIVE POLYMORPHISM
#                1. Inheritance = An objecy could be trated as the same type as a parent class
#                2. "Duck Typing" = Object must have necessary attributes/methods


from abc import ABC, abstractmethod
class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius     

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side  
     
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 1/2 * self.base * self.height
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super.__init__(radius)
        self.topping = topping
        


# shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]    

# for shape in shapes:
#     print(shape.area())


# "Duck Typing" = Another way to acheive polymorphism besides inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quack like a duck it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = False

    def speak(self):
        print("HONK!")

animals= {Dog(), Cat(), Car()}

# for animal in animals:
#     animal.speak()
#     print(animal.alive)


# Static methods = A method that belongs to a class rather than any object from that class (instance)
#                  Usually used for general utility funtions

# Instance Methods = Best for operations on instances of the class (objects)
# Static Methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name 
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions  
    
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")
    
# print(Employee.is_valid_position("Rocket Science"))

# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())

# Class Methods = Allow operations related to the class itself
#                 Take cls as the first parameter, which represents the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INCTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total numbe of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)
    
# print(Student.get_count())
# print(Student.get_avg_gpa())
    

# Magic methods = Dunder methods __init__, __str__, __eq__ 
#                 They are automatically called by many pythons built-in operations.
#                 They allow the developer to define or customise the behaivior of objects.


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages


    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} Pages"
    
    def __contains__(self, keyword):
        return keyword in self.title
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
    

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

# print(book2['title'])


# @Property = Decorator used to define a method as a property (it can be accessed like an attribute)
#            Benefit: Add additional logic when read, write, or delete attributes
#            Gives you getter, setter, and deleter method

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return f"{self._width:.1f} cm"
    
    @property
    def height(self):
        return f"{self._height:.1f} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width cant be less than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height cant be less than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")


rectangle = Rectangle(3, 4)

# rectangle.width = -1
# rectangle.height = 1


# print(rectangle.width)
# print(rectangle.height)


# Decorator = A function that extends the behaviour of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("Vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream ")

# get_ice_cream("Vanilla")


# Exceptions = An event that interrupts the flow of a program
#              (ZeroDivisionError, TypeError, ValueError)
#              1. try 2. except 3. finally

# try:
#     number = int(input("Enter a number:" ))
#     print(1/number)
# except ZeroDivisionError:
#     print("You cant divide by zero IDIOT!")
# except ValueError:
#     print('Enter only number please')
# except Exception:
#     print("Something went wrong")
# finally:
#     print("Do some cleanup here")


# Python file detection

import os

# file_path = "C:\\Users\\ARSHG\\OneDrive\\Desktop\\test.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
        
# else:
#     print("That location doesnt exist")


# Python Writing files (.txt, .jsonn, .csv)

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# file_path = "C:/Users/ARSHG/OneDrive/Desktop/output.txt"

# try:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path} was created")
# except FileExistsError:
#     print("That File already exists!")

# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file '{file_path} was created")
# except FileExistsError:
#     print("That File already exists!")

        
#JSON files = JavaScript Object Notation
#             Collection of key-value pairs

import json

# Employee_data = {
#     "name": "Spongebob",
#     "age": 30,
#     "position": "Cook",
# }

# file_path = "C:/Users/ARSHG/OneDrive/Desktop/employee.json"

# try:
#     with open(file_path, "w") as file:
#         json.dump(Employee_data, file, indent=4)
#         print(f"json file '{file_path} was created")
# except FileExistsError:
#     print("That File already exists!")


# CSV files = Comma Separated Values
#             Used to store tabular data (spreadsheets, databases)

import csv

# employees = [["Name", "Age", "Job"],
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 37, "Manager"],
#              ["Sandy", 27, "Scientist"],
#              ]

# file_path = "C:/Users/ARSHG/OneDrive/Desktop/employee.csv"

# try:
#     with open(file_path, "w", newline = "") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path} was created")
# except FileExistsError:
#     print("That File already exists!")



# Python Reading files (.txt, .json, .csv)

file_path = "C:/Users/ARSHG/OneDrive/Desktop/employee.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        # for line in content:
            # print(line[1])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have permission to read that file")


# Datetime module = used to work with dates and times

import datetime

date = datetime.date(2025, 1 , 2)
today = datetime.date.today()

time = datetime.time(12 , 30 , 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2030 , 1 , 2 , 12 , 30 , 1)
current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("The target date has  passed")
# else:
#     print("The target date is in the future")


# Multithreading = Used to perform tasks concurrently (multitasking)
#                  Good for I/O tasks like reading files or fetching data from API
#                  threading.Thread(target=my_function)


import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finished walking {first}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print(("You get the mail"))

# chore1 = threading.Thread(target = walk_dog, args = ("Scooby","Doo"))
# chore1.start()

# chore2 = threading.Thread(target = take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target = get_mail)
# chore3.start()

# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are complete")


# Connect to API using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    responce = requests.get(url)

    if responce.status_code == 200:
        pokemon_data = responce.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {responce.status_code}")


# pokemon_name = "pikachu"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")


# PyQt5 Introduction

import sys 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                             QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setWindowIcon(QIcon("download.jpeg"))  
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        # self.line_edit = QLineEdit(self)
        # self.button = QPushButton("Submit", self)
        # self.radio1 = QRadioButton("Visa", self)
        # self.radio2 = QRadioButton("MasterCard", self)
        # self.radio3 = QRadioButton("Gift Card", self)
        # self.radio4 = QRadioButton("In-Store", self)
        # self.radio5 = QRadioButton("Online", self)
        # self.button_group1 = QButtonGroup(self)
        # self.button_group2 = QButtonGroup(self)
        # self.button = self.button = QPushButton("Click me", self)
        # self.label = QLabel("Hello", self)
        # self.checkbox = QCheckBox("Do you like food", self)
        self.initUI()

        # TEXT AND BACKGROUND
        
        # label = QLabel("Noice", self)
        # label.setFont(QFont("Monocraft Nerd Font", 20))
        # label.setGeometry(0, 0 , 800 , 800)
        # label.setStyleSheet("color:blue;"
        #                     "background-color: green;"
        #                     "text-decoration: underline;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;")
        
        # label.setAlignment(Qt.AlignTop)  # ALIGN VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom)  # ALIGN VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter)   # ALIGN VERTICALLY CENTER

        # label.setAlignment(Qt.AlignRight) # ALIGN HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter) # ALIGN HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft) # ALIGN HORIZONTALLY LEFT

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER AND TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER AND BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER AND CENTER

        # label.setAlignment(Qt.AlignCenter)


        # ADDING IMAGES

        # label = QLabel(self)
        # label.setGeometry(0, 0, 300, 300)

        # pix_map = QPixmap("download.jpeg")
        # label.setPixmap(pix_map)

        # label.setScaledContents(True)

        # label.setGeometry((self.width() - label.width()) // 2,
        #                    (self.height() - label.height()) // 2, 
        #                    label.width(), 
        #                    label.height())


        
    # def initUI(self):
    #     central_widget = QWidget()
        # self.setCentralWidget(central_widget)

    #     # LAYOUTS

        # label1 = QLabel("#1", self)
        # label2 = QLabel("#2", self)
        # label3 = QLabel("#3", self)
        # label4 = QLabel("#4", self)
        # label5 = QLabel("#5", self)

        # label1.setStyleSheet("background-color: red;")
        # label2.setStyleSheet("background-color: yellow;")
        # label3.setStyleSheet("background-color: green;")
        # label4.setStyleSheet("background-color: blue;")
        # label5.setStyleSheet("background-color: purple;")

        # grid = QGridLayout()

        # grid.addWidget(label1, 0, 0)
        # grid.addWidget(label2, 0, 1)
        # grid.addWidget(label3, 1, 0)
        # grid.addWidget(label4, 1, 1)
        # grid.addWidget(label5, 2, 2)

        # central_widget.setLayout(grid)

    
    # BUTTONS

    # def initUI(self):
    #     self.button.setGeometry(150, 200, 200, 100)
    #     self.button.setStyleSheet("font-size: 30px;")
    #     self.button.clicked.connect(self.on_click)

    #     self.label.setGeometry(150, 300, 200, 100)
    #     self.label.setStyleSheet("font-size: 50px;")

    # def on_click(self):
    #     self.label.setText("Goodbye")


    # CHECKBOXES 

    # def initUI(self):
    #     self.checkbox.setGeometry(10, 0, 500, 100)
    #     self.checkbox.setStyleSheet("font-size:30px;"
    #                                 "font-family:Monocraft Nerd Font;")
        
    #     self.checkbox.setChecked(False)
    #     self.checkbox.stateChanged.connect(self.checkbox_changed)
    
    # def checkbox_changed(self, state):
    #     if state == Qt.Checked:
    #         print("You like food")
    #     else:
    #         print("You do not like food")


    # RADIO BUTTONS

    # def initUI(self):
    #     self.radio1.setGeometry(0, 0, 350, 100)
    #     self.radio2.setGeometry(0, 100, 350, 100)
    #     self.radio3.setGeometry(0, 200, 350, 100)
    #     self.radio4.setGeometry(0, 300, 350, 100)
    #     self.radio5.setGeometry(0, 400, 350, 100)

    #     self.setStyleSheet("QRadioButton{" 
    #                        "font-size: 40px;" 
    #                        "font-family: Monocraft Nerd Font;"
    #                        "padding: 10px;"
    #                        "}")

    #     self.button_group1.addButton(self.radio1)
    #     self.button_group1.addButton(self.radio2)
    #     self.button_group1.addButton(self.radio3)
    #     self.button_group2.addButton(self.radio4)
    #     self.button_group2.addButton(self.radio5)

    #     self.radio1.toggled.connect(self.radio_button_changed)
    #     self.radio2.toggled.connect(self.radio_button_changed)
    #     self.radio3.toggled.connect(self.radio_button_changed)
    #     self.radio4.toggled.connect(self.radio_button_changed)
    #     self.radio5.toggled.connect(self.radio_button_changed)


    # def radio_button_changed(self):
    #     radio_button = self.sender()
    #     if radio_button.isChecked():
    #         print(f"{radio_button.text()} is selected ")


    # TEXT BOXES

    # def initUI(self):
    #     self.line_edit.setGeometry(10, 10, 200, 40)
    #     self.line_edit.setStyleSheet("font-size: 20px;"
    #                                  "font-family: Monocraft Nerd Font")
    #     self.button.setGeometry(210, 10, 100, 40)
    #     self.button.setStyleSheet("font-size: 20px;"
    #                                  "font-family: Monocraft Nerd Font")
        
    #     self.line_edit.setPlaceholderText("Enter you name")
        
    #     self.button.clicked.connect(self.submit)

    # def submit(self):
    #     text = self.line_edit.text()
    #     print(f"Hello {text}")


    # SET STYLE SHEETS

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
        QPushButton{
            font-size: 20px;   
            font-family: Monocraft Nerd Font;
            padding: 15px 75px;  
            margin: 10px; 
            border: 3px solid;    
            border-radius: 15px;     
        }
        QPushButton#button1{
            background-color: red;
        }
        QPushButton#button2{
            background-color: green;
        }
        QPushButton#button3{
            background-color: blue;
        }
        QPushButton#button1:hover{
            background-color: #de3c3c;
        }
        QPushButton#button2:hover{
            background-color: #185426;
        }
        QPushButton#button3:hover{
            background-color: #181f54;
        }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()







