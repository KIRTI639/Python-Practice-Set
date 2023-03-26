# Write a Python program to count the number of occurrences of a specific character in a string.
string = input("Enter the string: ")
occurance_string = input("Enter the string whose occurance you wanted to count: ")
count = 0
for i in string:
    if i==occurance_string:
        count+=1
print(f"Count of {occurance_string} is {count}.")       