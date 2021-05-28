# /usr/bin/env python

counter = int(input("How many numbers do you wish to input> "))
s = 0
for i in range(0,counter):
    number = int(input("Enter a number> "))
    s = s+number
avg = float(s/counter)

print(f"Average of these {counter} numbers is\n{avg}")
