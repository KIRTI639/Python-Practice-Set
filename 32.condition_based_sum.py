# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5. 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = a+b
d = abs(a-b)
if a==b or c==5 or d==5:
    print("True")
else:
    print("Enjoy your day!")    