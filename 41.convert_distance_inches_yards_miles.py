#  Write a Python program to convert the distance (in feet) to inches, yards, and miles.
inches = float(input("Enter the distance in inches:"))
yards = float(input("Enter the distance in yards :"))
miles = float(input("Enter the ditance in miles: "))
inches_to_feet = inches*0.0833333
yards_to_feet = yards*3
miles_to_feet = miles*5280
print("Inches to feet: ",inches_to_feet)
print("Yards to feet:", yards_to_feet)
print("Miles to feet:",miles_to_feet)