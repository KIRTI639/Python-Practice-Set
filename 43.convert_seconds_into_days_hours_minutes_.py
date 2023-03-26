#  Write a Python program that converts seconds into days, hours, minutes, and seconds.

seconds = int(input("Enter the seconds: "))
days = seconds/(24*60*60)
hours = seconds/(60*60)
minutes = seconds/60
print("days:",days)
print("hours:",hours)
print("minutes:",minutes)
