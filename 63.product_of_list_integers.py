# Write a Python program to compute the product of a list of integers (without using a for loop).

# input_list = []
# a = int(input("Enter the numbers of elements you want to enter: "))
# for i in range(a):
#     b = int(input("Enter the elements: "))
#     input_list.append(b)
# print(input_list) 
# print("list:",input_list) 
# print(f"list: {input_list}") 
# print("list {}".format(input_list)) 

#while loop
# list = list(map(int,input("Enter the elements:").split()))
# print(list)
# i = 0
# product = 1
# b = []
# while(i<len(list)):
#     product = product*list[i]
#     i+=1
# b.append(product)    
# print(b)

#for loop
list = list(map(int,input("Enter the elements:").split()))
print(list)
product = 1
b =[]
for i in range(len(list)):
    product = product*list[i]
b.append(product)
print(b)    




