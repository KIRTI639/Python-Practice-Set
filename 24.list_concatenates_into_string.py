#  Write a Python program that concatenates all elements in a list into a string and returns it.
a = []
b = int(input("Enter the number :"))
for i in range(b):
    c = input("Enter the elements : ")
    a.append(c)
print(a)
d = " ".join(a)  
print(d)  