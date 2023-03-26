#Sum of squares of  digits of an integers.
digit = int(input("Enter the digit: "))
sum = 0
while(digit!=0): 
    remainder = digit%10    
    digit = digit//10       
    sum = sum+(remainder**2)  
print(sum)   