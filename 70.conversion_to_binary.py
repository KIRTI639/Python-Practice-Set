# Write a Python program to convert an integer to binary that keeps leading zeros. 
# Sample data : x=12
# Expected output : 00001100
# 0000001100
x = int(input("Enter the value: "))
y = bin(x)
print(y)
z = y.lstrip("0b")
print(z)
c = z.rjust(8,"0")
print(c)



# a = '######Kir#ti##'
# b = a.lstrip("#")
# print(b)
# c = a.rstrip("#")
# print(c)
# d = a.strip("#")
# print(d)

# b = "kirti"
# c = b.center(20,"*")
# print(c)
# d = b.ljust(7,"@")
# print(d)
# e = b.rjust(6,"&")
# print(e)