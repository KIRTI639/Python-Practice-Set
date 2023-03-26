# Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user. 
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number:"))
if input_1%input_2==0:
    print("Yes first number is divisible by second number")
else:
    print("No first number is not divisible by second number.")    