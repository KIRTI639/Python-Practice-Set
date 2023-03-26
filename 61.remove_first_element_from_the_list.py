# Write a Python program to remove the first item from a specified list.
list = input("Enter the numbers: ").split()
print(list)
list.remove(list[0])
print(list)

del list[0]
print(list)

list.pop(0)
print(list)