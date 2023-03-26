# Write a Python program to calculate the hypotenuse of a right angled triangle. 
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
hypotenus = ((base**2)+ (height**2))**0.5   
print(f"Hypotenus of the triangle is {hypotenus}")