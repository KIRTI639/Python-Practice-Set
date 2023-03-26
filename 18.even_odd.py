# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

input = int(input("Enter the number :"))
if input%2==0:
    print(f"{input} is a Even number...")
else:
    print(f"{input} is a odd number...")    