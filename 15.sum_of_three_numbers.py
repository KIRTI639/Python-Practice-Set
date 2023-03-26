#  Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c= int(input("Enter the third number:"))
d = a+b+c
if a==b and b==c:
    print(f"Sum of the numbers is {d*3}")
else:
    print(d)    
