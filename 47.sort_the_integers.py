# Write a Python program to sort three integers without using conditional statements and loops. 17 41 20   17 20 41
# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
# third_number = int(input("Enter the third number: "))
# list_1 = []
# list_1.append(first_number)
# list_1.append(second_number)
# list_1.append(third_number)
# print(list_1)
# list_1.sort()
# print(list_1)


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))
list_1 = list((first_number,second_number,third_number))
# list_1.sort()
sorting = sorted(list_1)
print(sorting)

