# Importing math module and sys module
import math
import sys

# create an empty dictionary
adj_dictionary = {}
coord_dictionary = {}

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

# take input from user
start = input("Enter your starting point: ")
for key in coord_dictionary:
    if start == key:
        print("Starting point is valid")
        break
else:
    sys.exit("Starting point is invalid, run the program again and enter a valid starting point")

# take input from user
end = input("Enter your ending point: ")
for key in coord_dictionary:
    if end == key:
        print("Ending point is valid")
        break
else:
    sys.exit("Ending point is invalid, run the program again and enter a valid ending point")


officical_adj_dict = {}
for key1 in coord_dictionary:
    officical_adj_dict[key1] = ""
# loop through the keys and values of the coordinates dictionary
for key1 in coord_dictionary:
    # key1 = key of the coordinates dictionary
    # coord_dictionary[key1] = value of the coordinates dictionary

    # loops through the keys and values of the adjacencies dictionary
    for key2, value2 in adj_dictionary.items():
        # towns splits the words in value2
        towns = value2.split()
        if key1 in key2:
            officical_adj_dict[key1] += " " + value2
        if key1 in towns:
            officical_adj_dict[key1] += " " + key2

# remove duplicates of towns
for key, value in officical_adj_dict.items():
    towns = value.split()
    officical_adj_dict[key] = list(set(towns))

SUCCESS = True
FAILURE = False
State = FAILURE

def euclideanDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# this function checks if the node is the goal state
def GOALTEST(N):
    if N == end:
        return True
    else:
        return False

# this function adds the adjacent towns to the node
def AddAdj(NodeTown):
    New_list = list()
    if NodeTown in officical_adj_dict.keys():
        New_list = officical_adj_dict[NodeTown]

    return New_list

# this function appends the list from the OPEN list to the CLOSED list
def APPEND(L1, L2):
    New_list = list(L1)+list(L2)
    return New_list

# this function sorts the OPEN list depending on the euclidean distance
def SORT(Open, Closed):
    DistanceDictionary = {}
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    distance = Closed[-1]
    if Closed[-1] in coord_dictionary:
        x1, y1 = coord_dictionary[Closed[-1]].split()
        x1 = float(x1)
        y1 = float(y1)

    for i in range(len(Open)):
        if Open[i] in coord_dictionary:
            x2, y2 = coord_dictionary[Open[i]].split()
            x2 = float(x2)
            y2 = float(y2)
            DistanceDictionary[Open[i]] = euclideanDistance(x1, y1, x2, y2)

    Open = sorted(DistanceDictionary.keys())

    if end in Open:
        index = Open.index(end)
        Open = [Open[index]] + Open[:index] + Open[index+1:]


    return Open


def BestFirstSearch():
    OPEN = [start]
    CLOSED = []
    global State
    global Closed

    # this means that when when the OPEN list is not empty and the state is not SUCCESS
    while (State != SUCCESS):

        print("------------")
        # get the first element of the OPEN list
        NodeTown = OPEN[0]
        print("NodeTown=", NodeTown)
        # remove the first element of the OPEN list
        OPEN.remove(NodeTown)
        # if the first element of the OPEN list is the goal state then set the state to SUCCESS
        if GOALTEST(NodeTown) == True:
            State = SUCCESS
            CLOSED = APPEND(CLOSED, [NodeTown])
            OPEN.clear()
            print("CLOSED=", CLOSED)
            break
        # else if the first element of the OPEN list is not the goal state then set the state to FAILURE
        # and append the first element of the OPEN list to the CLOSED list
        else:
            # closed is set to the first element of the OPEN list
            CLOSED = APPEND(CLOSED, [NodeTown])
            print("CLOSED=", CLOSED)
            Adj = AddAdj(NodeTown)
            print("Adjacent Towns=", Adj)
            for val in CLOSED:
                if val in Adj:
                    Adj.remove(val)
            for val in OPEN:
                if val in Adj:
                    Adj.remove(val)
            OPEN = APPEND(Adj, OPEN)  # append movegen elements to OPEN
            print("Unsorted OPEN=", OPEN)
            OPEN = SORT(OPEN, CLOSED)
            print("Sorted OPEN=", OPEN)

    print("***************************************************")
    return CLOSED


PathSearched = BestFirstSearch()
# This is the first element in the list
Beginning = PathSearched[0]
# # THis is the last element in the list
End = PathSearched[-1]


OfficialPath = []
for i in reversed(range(len(PathSearched))):
    # print(i, PathSearched[i])
    for j in reversed(range(len(PathSearched))):
        # this means if the current element is in the definition of the prev element
        if PathSearched[i] in officical_adj_dict[PathSearched[j]]:
            OfficialPath.append(PathSearched[i])
            break
        else:
            i -= 1

OfficialPath.reverse()
OfficialPath.pop(0)
OfficialPath.append(End)
OfficialPath.insert(0, Beginning)
print("OfficialPath=", OfficialPath)
