# Fetch the month by their counting.(3 ways)

# dict = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# input = int(input("Enter the number of the month: "))
# for key in dict:
#     if input == key:
#         print(dict[key])



# a = int(input("Enter the month number: "))
# if a==1:
#     print("January")
# elif a==2:
#     print("February")
# elif a==3:
#     print("March")
# elif a==4:
#     print("April")
# elif a==5:
#     print("May")
# elif a==6:
#     print("June")
# elif a==7:
#     print("July")
# elif a==8:
#     print("August")
# elif a==9:
#     print("September")
# elif a==10:
#     print("October")
# elif a==11:
#     print("November")
# elif a==12:
#     print("December")
# else:
#     print("Aapna kabhi 12 sa jayada months dekha hai ?")                                                


input = int(input("Enter the input value:"))
match input:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June") 
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")                                          