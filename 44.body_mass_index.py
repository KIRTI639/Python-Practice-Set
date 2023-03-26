# Write a Python program to calculate the body mass index.
weight = float(input("Enter the weight in kilograms: "))  
height = float(input("Enter the height in centimetres: "))
height_square = (height**2)/10000                  #height**height , height**2, height*height
body_mass_index = weight/height_square              #  5*5*5*5*5,    5*5,         5*5
print(f"Body mass index is {body_mass_index}")
print("Body mass index is", body_mass_index)
print("Body mass index is {}".format(body_mass_index))
print("Body mass index is %.2f" %(body_mass_index))
