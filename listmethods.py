listno = [1,2,3,4,5,6,7,8,9,10]
print(listno)

# append (adds an element at the end of the list)
listno.append(11)
print(listno)

# extend (adds elements to the end of the list)

listno2 = [12,13,14,15,16,17,18,19,20]
listno.extend(listno2)
print(listno)

# insert (used to insert the element in the list at the given index)
listname = ['alex', 'brown', 'drex']
listname.insert(2, 'shawn') # inserts 'shawn' in the 2nd index number
print(listname)

# remove (removes the matching element from the list)
listname.remove('alex')
print(listname)

# count (used to count the number of particular element present in the list)
val = listname.count('brown')
print(val)

# clear (clear all the elements present in the list)
listtoclear = [10, 20, 30]
listtoclear.clear()
print(listtoclear)

# copy (return the new list, which is exactly the same)
listname.copy()
print(listname)

# index (returns the index of the specified elements from the list)
namexx = listname.index("brown")
print(namexx)

# reverse (used to reverse the element present in the list)
listname.reverse()
print(listname)

# pop (used to remove the specified item from the given index of a list)
id = [12,13,14,15]
id.pop(1)
print(id)

# sort (used to sort the list in ascending order by default it, doesn’t require an extra parameter to sort)
listname.sort()
print(listname)

# len (used for getting the total number of elements present in the list)
l = len(listname)
print(l)

