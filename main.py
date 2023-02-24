# Importing math module and sys module
import math
import sys

# create an empty dictionary
adj_dictionary = {}
coord_dictionary = {}

# take input from user
# start = input("Enter your starting point: ")

# open the file in read mode
# the r is for read mode
# created a dictionary with the adjacencies
with open("Adjacencies.txt", "r") as file:
    for line in file:
        # split the line into words
        words = line.strip().split()
        # use the first word as the key and the rest of the line as the value
        key = words[0]
        value = " ".join(words[1:])
        # add the key-value pair to the dictionary
        adj_dictionary[key] = value

# open the file in read mode
# the r is for read mode
# created a dictionary with the coordinates
with open("coordinates.txt", "r") as file:
    for line in file:
        # split the line into words
        words = line.strip().split()
        # use the first word as the key and the rest of the line as the value
        key = words[0]
        value = " ".join(words[1:])
        # add the key-value pair to the dictionary
        coord_dictionary[key] = value

# # take input from user
# start = input("Enter your starting point: ")
# for key in coord_dictionary:
#     if start == key:
#         print("Starting point is valid")
#         break
# else:
#     sys.exit("Starting point is invalid, run the program again and enter a valid starting point")

# # take input from user
# end = input("Enter your ending point: ")
# for key in coord_dictionary:
#     if end == key:
#         print("Ending point is valid")
#         break
# else:
#     sys.exit("Ending point is invalid, run the program again and enter a valid ending point")



# This is the euclidean distance formula
# eDistance = math.dist([x1, y1], [x2, y2])

# print the dictionary
# print(adj_dictionary)
# print the value for the key "A"
# print(adj_dictionary["Attica"])

new_adj_dict = {}
for key1 in coord_dictionary:
    new_adj_dict[key1] = ""
# loop through the keys and values of the coordinates dictionary
for key1 in coord_dictionary:
    # new_adj_dict[key1] = coord_dictionary[key1]
    # key1 = key
    # coord_dictionary[key1] = value
    # loops through the keys and values of the adjacencies dictionary
    for key2, value2 in adj_dictionary.items():
        # towns splits the words in value2
        towns = value2.split()
        if key1 in key2:
            new_adj_dict[key1] += " " + value2
        if key1 in towns:
            new_adj_dict[key1] += " " + key2


officical_adj_dict = {}
# loop through the keys and values of the dictionary and remove duplicates
for key, value in new_adj_dict.items():
    towns = value.split()
    officical_adj_dict[key] = list(set(towns))
    
print(officical_adj_dict)
    # # check if the value-key pair exists with the same value
    # if key == adj_dictionary[value]:
    #     # if the pair exists, continue to the next pair
    #     new_dictionary[key] = value
    # else:
    #     # if the pair doesn't exist or has a different value, add the missing pair
    #     new_dictionary[value] = key

# print(new_adj_dict)
# print the dictionary
# print(coord_dictionary)
# print the value for the key "A"
# print(coord_dictionary["Harper"])
