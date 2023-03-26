# Write a Python program to sum all counts in a collection.
list_a = []
a = int(input("Enter the number: "))
for b in range(a):
    c = int(input("Enter the elements: "))
    list_a.append(c)
print(list_a)
length = 0
for i in range(len(list_a)):
    length+=1
print(length)    




# list_1 = list(map(int,input("Enter the elements :").split()))
# print(list_1)
# length = 0
# while(length<len(list_1)):
#     length+=1
# print(length)    