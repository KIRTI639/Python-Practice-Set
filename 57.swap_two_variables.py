# Write a Python program to swap two variables.(2 ways)


# first_number = int(input("Enter the first number:"))
# second_number = int(input("Enter the second number: "))
# print(f"Before swaping a = {first_number} and b = {second_number}")
# t = first_number
# first_number = second_number
# second_number = t
# print(f"After swaping a = {first_number} and b = {second_number}")
# print("After swaping a =" , first_number,"and b =",second_number)
# print("After swaping a = {} and b = {}".format(first_number,second_number))
# print("After swaping a = %d and b = %d" %(first_number,second_number))

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a = a+b
b = a-b
a = a-b
print(f"After swaping a = {a} and b = {b}")

