#  Write a Python program to calculate sum of digits of a number.

# using while loop
# digit = int(input("Enter the digit: "))#45341
# sum = 0
# while(digit!=0):
#     remainder = digit%10 
#     digit = digit//10  
#     sum = sum+remainder
# print(sum)    


# using for loop
digit = int(input("Enter the digit: "))#45341
string_form = str(digit)
sum = 0
for i in string_form:
     sum = sum+int(i)
print(sum)     
