# Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
# Original sequence: 01010101
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
# Original sequence: 000111000111
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00011100011
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
a = input("Enter the number: ")
print(a)
count_zero = 0
count_ones = 0
for i in range(len(a)):
    if a[i]=="0":
        count_zero+=1
    elif a[i]=="1":
        count_ones+=1
    else:
        pass 
print(count_ones)
print(count_zero)
if count_zero==count_ones:
    print(True) 
else:
    print(False)         



 


