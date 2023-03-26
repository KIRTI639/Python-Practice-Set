# Write a Python program to extract a single key-value pair from a dictionary into variables.
dictionary = {1:"Apple",2:"Banana",3:"grapes",4:"orange",5:"papaya"}
print(dictionary)
# key = dictionary.keys()
# values = dictionary.values()
# items = dictionary.items()
# print(key)
# print(values)
# print(items)


# for i in items:
#     print(i)

for k in dictionary:
    print(k,dictionary[k])
# for items in dictionary.items():
#     print(items[0],items[1])
for items in dictionary.items():
    print(items)        

