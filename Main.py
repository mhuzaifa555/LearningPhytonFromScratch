# this is my first code
# print("i like pizza")
# print ("i like burger too")
#these all are strings except age
name = "huzaifa"
email = "huzaifaisleraning@gmail.com"
# INTEGERS
phone = 32213213213
age = 20
#float
GPA = 3.0
CGPA = 2.9
#Boolean
nationalaity = False
# if nationalaity:
#     print("YOU ARE A PAKISTANI")
# else:
#     print("You ARE NOT PAKISTANI")
# mobile = input("Which mobile are you using?: ")
# price = int(input("its price is?: "))
# print(f"WOHOOOO, your mobile is {mobile} and is amazingly at ${price}")

# Day 02:
# Exercise 01: Rectangle area calculator

# lenght  = float(input("Enter lenght: "))
# breadth = float(input("Enter breadth: "))
# area = lenght * breadth
# print(f"The area of your rectangle is : {area}cm²")

# Exercise 02: Shopping Bill
#
# item = input("Please select an item: ")
# quantity = int(input("Quantity: "))
# price = 10
# Total = quantity*price
# print(f"You have bought {quantity} x {item}/s")
# print(f"Total is ${Total}")

# Exercise 03: Madlibs Game (make a story by filling blanks with random words)
# noun1 = input("Enter a noun (a place): ")
# noun2 = input("Enter a noun (anything): ")
# adjective1 = input("Enter an adjective: ")
# adjective2 = input("Enter an adjective again: ")
#
# print(f"Today I went to {noun1}")
# print(f"There I saw {noun2}, it was {adjective1}")
# print(f"I {adjective2} it so much")


# if statments
# age = int(input("Please Enter your age: "))
# if age > 18:
#     print("You can access this.")
#
# elif age < 0:
#     print("You havent been born yet")
# else:
#     print("You must be above 18")
# If Statement Practice Challenges
# Even or Odd

# value = int(input("Please enter a value to check, if its odd or even (value =/ 0): "))
# if value ==0:
#     print("The value can not be 0")
# elif value % 2 == 0:
#     print("The value is Even")
# else:
#     print("The value is Odd")
#
# Leap Year Checker

# year = int(input("Enter a year to check if its a leap year or not: "))
# # if year < 0:
# #     print("Year can't be negative")
# # elif year % 400 ==0:
# #     print("Its a leap year")
# # elif year % 100 ==0:
# #     print("Its not a leap year")
# # elif year % 4 ==0:
# #     print("Its a leap year")
# # else:
# #     print("Its not a leap year")

# Password Lenght Checker

# password = input("Please enter a password: ")
#
# if len(password) < 6:
#     print("Please enter a password consisting of minimum 6 characters")
# elif len(password) > 15:
#     print("Please enter a password consisting of maximum 15 characters")
# else:
#     print("Success, Your password has been set")

# Mini Login System

# username = "huzaifa"
# password = "coding231"
#
# user = input("Enter your username: ")
#
# if user==username:
#      pass1 = input("Enter your password: ")
#      if pass1 == password:
#         print("Successfully logged in!")
#      else:
#         print("Can not logged in, Incorrect Password!")
# else:
#     print("username does not exist")

# Phyton Simple calculator using IF
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter an operator {+,-,*,/,%: ")
# if operator == "+":
#     sum = num1+num2
# elif operator == "-":
#     sum = num1 - num2
# elif operator == "*":
#     sum = num1 * num2
# elif operator == "/":
#     sum = num1 / num2
# elif operator == "%":
#     sum = num1 % num2
# else:
#     print(f"{operator} is not a valid operator: ")
# print(f"The answer is {sum}")

# Temperature converting Program:

# unit = input("Is the temperature is in {C/F}?: ")
# temp = float(input("Enter the temperature: "))
# if unit == "C":
#     F = (temp * 9/5) + 32
#     print(f"The Temperature in Fahrenheit is {round(F, 1)}°F")
#
# elif unit == "F":
#     C = (temp - 32) * 5 / 9
#     print(f"The Temperature in Celsius is {round(C , 1)}°C")
# else:
#     print(f"{unit} is not a correct unit")

# Conditional Statements

# Temperature Checker
# temperature = int(input("Enter the temperature: "))
# temp = "Hot Day" if temperature >= 30 else "Not a Hot Day"
# print(temp)

# Score checker
# score = int(input("Type run you scored Today!: "))
# check = "Well Played Man!" if score >50 else "Hard Luck Man!"
# print(check)

# DAY 03:
# String Methods
# Username Validation
# Conditions: Only alphabets and numbers allowed (no spaces, no special chars).Must be at least 5 characters.

# name = input("Enter a username: ")
#
# if not name.isalnum() :
#     print("Username can contain only alphanumeric values, and no spaces")
# elif len(name) <5 or len(name) > 10:
#     print("Username must be consists of 5-10 characters")
# else:
#     print(f"Welcome {name}")

# String Indexing
# getting last 4 digits of Credit Card
# cc_number = input("Enter your CC number Format (****-****-****-****): ")
# get_dig = cc_number[-4:]
# print(f"Your Last 4 digit of CC is:{get_dig}")

# Day 04
# While loop
# any number type, 0 to exit

# Correct password
# password = "huzaifa123"
# user_input = input("Enter password: ")
# while user_input != password:
#     print("Wrong password, try again.")
#     user_input = input("Enter password: ")
#
# print("Access Granted ✅")

# num = 0
# while num < 100:
#     num = num +1
#     print(f"{num}")
# print("loop is finished")

num = 1
while num <= 50:
    if num % 2 == 0:
     print(f"Even {num}")
    num +=1