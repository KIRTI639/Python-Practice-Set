# Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number.

#Using for loop
n = int(input("Enter the integer: "))
sum = 0
for i in range(n-1,0,-1):
    sum=sum+i**3
print(sum) 

#using while loop
n = int(input("Enter the number: "))
sum = 0
while(n>0):
    sum = sum+(n-1)**3
    n=n-1
print(sum)    

