#  Write a Python program to count the number 4 in a given list.
# a = [4,6,5,4,8,4,23,4,0]
# count = 0
# for i in range(len(a)):
#     if a[i]==4:
#         count = count+1
# print(count)            
        
a = []
b = int(input("How many numbers you want in list ? "))
for i in range(b):
    c =  int(input("Enter the elements : "))
    a.append(c)
print(a)
count = 0
for i in range(len(a)):
    if a[i]==4:
        count=count+1
print(count)        


       