# Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

a = input("Enter the Examination schedule date: ").split(" ")
b = tuple(a)
print(b)
x,y,z=b
print(x+"/"+y+"/"+z)
