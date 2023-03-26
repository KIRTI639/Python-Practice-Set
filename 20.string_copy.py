#  Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2. 
m = input("Enter the string :")
n = int(input("Enter the integer number : "))
if len(m)<=2:
    print(m)
else:
    print(m[:2]*n)    

# Output:m = kirti
# n = 2
# kiki
# or

# m = ki
# n = ki
