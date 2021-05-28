# /usr/bin/env python

num1 = int(input("Enter first number> "))
num2 = int(input("Enter second number> "))

num3 = num2
num2 = num1
num1 = num3

print(f"By swapping values,\nthe value of the 1st number = {num1} and\nthe value of the 2nd number = {num2}")
