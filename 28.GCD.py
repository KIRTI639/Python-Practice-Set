#  Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
GCD = 0
smaller = 0
if a>b:
    smaller = b 
else:
    smaller = a    
for i in range (1,smaller+1):
    if a%i==0 and b%i==0:
        GCD = i
print(GCD)        











