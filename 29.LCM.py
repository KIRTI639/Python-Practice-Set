# Write a Python program to find the least common multiple (LCM) of two positive integers.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
LCM = 0
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        LCM = i
        break
print(LCM)                
