#  Write a Python program to convert all units of time into seconds.
hour = int(input("Enter the time in hours: "))
minutes = int(input("Enter the time in minutes: "))
hour_to_second = 60*60*hour
minutes_to_seconds = 60*minutes
total_seconds = hour_to_second + minutes_to_seconds
print(total_seconds)
