# Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
# Sample filename : abc.java
# Output : java
# a = (input("Enter the filename :"))
# for i in range(len(a)):
#     if(a[i]=="."):
#         ex = a[i+1:]
#         print(ex)
#         break

a = (input("Enter the filename :"))
for i in range(len(a)-1,-1,-1):
    if(a[i]=="."):
        ex = a[i+1:]
        print(ex)
        break


# a = (input("Enter the filename :"))
# # b = ""
# # for  i in range (len(a)-1,-1,-1):
# #     b = b+a[i]
# # print(b)
# 
#   
# b = a[::-1]
# print(b)