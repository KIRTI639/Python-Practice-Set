# Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
list = list(map(int,input("Enter the values:").split()))
# list_1 = input("Enter the values:").split()
sum = 0
print(list)
for i in list:
    sum = sum+(i)
    # sum = sum+int(i)
print(sum)    


