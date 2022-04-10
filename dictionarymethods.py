# clear (Removes all the elements from the dictionary)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print(car)

# copy (Returns a copy of the dictionary)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
copy = car.copy()
print(copy)

# fromkeys (Returns a dictionary with the specified keys and value)
brand = ("Apple", "Samsung", "OnePlus")
prodtype = "Phones"
dictionary = dict.fromkeys(brand, prodtype)
print(dictionary)

# get (Returns the value of the specified key)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
getter = car.get("model")
print(getter)

# items (Returns a list containing a tuple for each key value pair)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
items = car.items()
print(items)

# keys (Returns a list containing the dictionary's keys)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
keys = car.keys()
print(keys)

# pop (Removes the element with the specified key)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")
print(car)

# popitem (Removes the last inserted key-value pair)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.popitem()
print(car)

# setdefault (Returns the value of the specified key. If the key does not exist: insert the key, with the specified value)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.setdefault("model", "Bronco")
print(x)


# update (Updates the dictionary with the specified key-value pairs)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "White"})
print(car)

# values (Returns a list of all the values in the dictionary)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()
print(x)




