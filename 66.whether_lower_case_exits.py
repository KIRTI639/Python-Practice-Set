#  Write a Python program to check whether lowercase letters exist in a string.
# output:-
# kirti = True
# KIRTI = False
# KIRTi = True
string = input("Enter the string here: ")
for i in range(len(string)):
    if string[i].islower():
        print("True")
        break
else:
    print("False")

    
