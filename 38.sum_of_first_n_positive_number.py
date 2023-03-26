# Write a Python program to sum the first n positive integers.
n = int(input("Enter the positive integer :"))
sum = 0
for i in range(1,n+1):
    sum+=i
print("Sum of the first",n,"positive integers is :",sum)
print(f"Sum of the first {n} positive integers is {sum}.")
print("Sum of the first {} positive numbers is {}".format(n,sum))  
print("Sum of the first %d positive numbers is %d" %(n,sum))  

