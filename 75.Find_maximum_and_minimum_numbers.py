#  Write a Python function to find the maximum and minimum numbers from a sequence of numbers. Go to the editor
# Note: Do not use built-in functions.
a =[]
b = int(input("Enter the input:"))
for i in range(b):
    c = int(input("Enter the numbers: "))
    a.append(c)
print(a)
large = -10**6
for j in range(len(a)):
    if large<a[j]:
        large=a[j]
print(large) 
small = 10**6
for k in range(len(a)):
    if small>a[k]:
        small=a[k]
print(small)              