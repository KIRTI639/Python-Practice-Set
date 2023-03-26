# Write a Python program that checks whether a specified value is contained within a group of values. Go to the editor
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
a = []
b = int(input("Enter the numbers: "))
for i in range(b):
    c = int(input("Enter the numbers: "))
    a.append(c)
print(a)
d = int(input("Enter the number to see whether present in the list or not: "))
for i in range(len(a)):
    if a[i]==d:
        print("True")
        break
else:
    print("False")        