# Write a Python program to calculate the midpoints of a line.
# x1,y1 = (2,3)
#x2,y2 = (3,6)
x1, y1= list(map(int,input("Enter space separated values: ").split()))
x2, y2 = list(map(int,input("Enter space separated values: ").split()))
x = (x1+x2)/2
y = (y1+y2)/2
print(f"Midpoints of the line is ({x} , {y})")
