# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years. 
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

p = float(input("Enter the principle: "))
r = float(input("Enter the rate :"))
t = float(input("Enter the time :"))
simple_interest = (p*r*t)/100
print(simple_interest)
amount = p + simple_interest
print(amount)

