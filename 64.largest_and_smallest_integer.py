# Write a Python program to determine the largest and smallest integers.

# list = list(map(int,input("Enter the numbers: ").split()))
# print(list)

a = []
b = int(input("Enter the number of element: "))
for i in range(b):
    c = int(input("Enter the elements: "))
    a.append(c)
print(a)  
large = -10**6 #99999
for d in range(len(a)):
    if large<a[d]:
        large = a[d]
print(large)
small = 10**6 #9999999
for e in range(len(a)):
    if small>a[e]:
        small = a[e]
print(small)        



