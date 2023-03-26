# Write a Python program to filter positive numbers from a list. 
list = list(map(int,input("Enter the numbers: ").split()))
list_1 =[]
for i in range(len(list)):
    if list[i]>=0:
        list_1.append(list[i])
print(list_1)

      