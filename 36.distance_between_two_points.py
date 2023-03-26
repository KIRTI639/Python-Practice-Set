# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
x1 = int(input("Enter the value of the x1 :"))
x2 = int(input("Enter the value of the x2 :"))
y1 = int(input("Enter the value of the y1 :"))
y2 = int(input("Enter the value of the y2 :"))
distance = ((x2-x1)**2+ (y2-y1)**2)**0.5
print("%.2f" %(distance))