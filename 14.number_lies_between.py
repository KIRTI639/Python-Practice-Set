#  Write a Python program to test whether a number is within 100 of 1000 or 2000.
a = int(input("Enter the number :"))
if a<=100:    #2500<=100 f
    print(f"{a} lies under 100.")
elif a>100 and a<=1000: #2500>100 and 2500<=1000 f
    print(f"{a} lies between 100 and 1000.")
elif a>1000 and a<2000:  #2500>1000 and 2500<2000 f
    print(f"{a} given number lies betwwen 1000 and 2000.")
else:
    print("Give the input under 2000.")        
