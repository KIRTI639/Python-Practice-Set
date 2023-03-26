# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
a = input("Enter the sentencs :")
if a.startswith("Is"):
    print(a)
else:
    print("Is"+" "+a+"?")    