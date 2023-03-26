#  Write a python program to convert decimal to hexadecimal.
# Sample decimal number: 30, 4
# Expected output: 1e, 04

# a = int(input("Enter the num: "))
# b = hex(a)
# print(b)
# c = b.lstrip("0x")
# print(c)

a = list(map(int,input("Enter the number: ").split(",")))
print(a)
for i in range(len(a)):
    b = hex(a[i]).lstrip("0x").rjust(2,"0")
    print(b,end=" ")    
