# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

a  = input("Enter the numbers :").split(",")
print("List :",list(a))
print("Tuple :",tuple(a))


# a = input("Enter the file name :")
# for i in range (len(a)):
#     if a[i]==".":
#         print(a[i+1:])
#         break
