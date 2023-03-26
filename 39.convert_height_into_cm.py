#  Write a Python program to convert height (in feet and inches) to centimeters. 
height = float(input("Enter the height in centimeters : "))
height_in_feet = height*0.0328
height_in_inches = height*0.3937
print(f"Height in feet is {height_in_feet} and height in inches is {height_in_inches}")
print("Height in feet is",height_in_feet,"and height in inches is",height_in_inches)
print("Height in feet is {} and height in inches is {}".format(height_in_feet,height_in_inches))
print("Height in feet is %.2f and height in inches is %.2f" %(height_in_feet,height_in_inches))


