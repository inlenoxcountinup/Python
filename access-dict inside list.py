# accessing key values of a dictionary in a list

dict1 = {"one" : 1, "two" : 2, "three" : 3, "four" : 4}
list1 = list(dict1)
print(list1)


# accessing values of a dictionary in a list

dict1 = {"one" : 1, "two" : 2, "three" : 3, "four" : 4}
list1 = list(dict1.values())
print(list1)


# accessing values of a list in a dictionary
listx = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
dictx = dict(listx[0:3])
print(dictx)