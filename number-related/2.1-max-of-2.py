# /usr/bin/env python

num1 = float(input("Enter 1st number> "))
num2 = float(input("Enter 2nd number> "))

if num1 > num2:
    print(f"\n{num1} is greater than {num2}")
elif num2 > num1:
    print(f"\n{num2} is greater than {num1}")
else:
    print(f"\n{num1} is equal to {num2}")
