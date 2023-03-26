#  Write a Python program to get numbers divisible by fifteen from a list.
list = list(map(int,input("Enter the numbers: ").split()))
print(list)
b = []
for i in range(len(list)):
    if list[i]%15==0:
        b.append(list[i])
print(b)        