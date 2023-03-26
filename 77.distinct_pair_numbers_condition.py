# Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values. 
a =  list(map(int,input("Enter the elements: ").split()))
print(a)
b = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        product = a[i]*a[j]
        if product%2!=0 and product in a:
            print(True)
            b = 1
            break
    if b ==1:
        break        
else:
    print(False)        
