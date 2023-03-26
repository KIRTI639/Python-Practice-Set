#  Write a Python program to test whether all numbers in a list are greater than a certain number.
list = list(map(int,input("Enter the elements:").split()))
print(list)
number_to_test = int(input("Enter the number:"))
for i in range(len(list)):
    if list[i]>number_to_test:
        pass
    else:
        print("False")
        break
else:
    print("True")    