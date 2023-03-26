#  Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20. 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = a+b
if c>=15 and c<=20:
    print(20)
else:
    print(c)    