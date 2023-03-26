#  Write a Python program to get the volume of a sphere with radius six.
#4/3pi*r*r*r
from math import pi
r = float(input("Enter the radius of the sphere :"))
print(f"Volume of the Sphere is {4/3*pi*r*r*r}")
print("Volume of the sphere is {}".format(4/3*pi*r*r*r))
print("Volume of the Sphere is %.2f" %(4/3*pi*r*r*r))
print("Volume of the Sphere is",4/3*pi*r*r*r)
