# Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference.

m = int(input("Enter the number :"))
n = 17
p = m-n
print(p)
if m>n:
    print(p*2) 
else:
    print(abs(p))       