# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
import sys

y1 = int(input("Enter first year  : "))
m1 = int(input("Enter month : "))
d1 = int(input("Enter days : "))

y2 = int(input("Enter second year  : "))
m2 = int(input("Enter month : "))
d2 = int(input("Enter days : "))

# date1  = (2020/07/12)
# date2  = (2023/08/15)

print(f"Date 1 : ({y1}/{m1}/{d1})")
print(f"Date 2 : ({y2}/{m2}/{d2})")

if d1 < d2:
    d1 = d1 + 31
    m1 = m1 - 1
if m1 < m2:
    m1 = m1 + 12
    y1 = y1 - 1
if y1 < y2:
    print("Can't determine. Year 1 can not be less than year 2.")
    sys.exit()

y = y1 - y2
m = m1 - m2
d = d1 - d2

print(f"Final Result : \nYears = {y}\nMonths = {m}\nDays = {d}")
