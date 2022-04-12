# center (The center() method center aligns a string. The alignment is done using a specified character (whitespace is default))
sentence = 'algorithm'
print(sentence.center(15,'#'))


# count (The count() method returns the count or the number of times a particular value appears in a string.)
sentence = 'She sells seashells by the seashore. The shells she sells are surely seashells'
print(sentence.count('seashells'))
print(sentence.count('seashells',9,25))


# find (The find() method returns the lowest index of a particular substring in a string. If the substring is not found, -1 is returned.)
sentence = 'She sells seashells by the seashore. The shells she sells are surely seashells'
print(sentence.find('seashells'))
print(sentence.find('seashells',0,9))
print(sentence.find('s',5,10))
print(sentence.rfind('seashells')) # The rfind() method is similar to find() except that it returns the highest index value of the substring


# swapcase (The swapcase() method returns a copy of the string with all its uppercase letters converted into lower case and vice versa.)
sentence = 'Queue IS another FUNDAMENTAL data STRucture AND IS a close COUSIN of the STACK'
print(sentence.swapcase())


# startswith and endswith (The startswith() method returns True if the string starts with the specified value, otherwise it returns False. The endswith() function, on the other hand, returns True if the string endswith the specified value, else it returns False.)
sentence = 'Binary Search is a classic recursive algorithm'
print(sentence.startswith("Binary"))
print(sentence.startswith("Search",7,20))


# split (The split() method returns a list of words in a string where default separator is any whitespace.)
fruits = 'apples, mangoes, bananas, grapes'
print(fruits.split())
print(fruits.split(",",maxsplit = 2))


# capitalize (The capitalize() method capitalizes only the first character of the given string.)
print("san francisco".capitalize())


# upper (The upper() method only capitalizes the first letter of the string.)
print("san francisco".upper())


# title (The title() method capitalizes all the first letters of the string.)
print("san francisco".title())


# ljust and rjust (The ljust() method returns a left-justified version of the given string using a specified character, whitespace being default. The rjust() methods aligns the string to the right.)
text = 'Binary Search'
print(text.rjust(25),"is a classic recursive algorithm")

text = 'Binary Search'
print(text.ljust(25),"is a classic recursive algorithm")


# strip (The strip() method returns a copy of the string with the leading and trailing characters removed. Default character to be removed is whitespace.)
string = '#.......Section 3.2.1 Issue #32......'
print(string.strip('.#!'))
print(string.rstrip('.#!')) # rstrip(): strips characters from the right of a string. 
print(string.lstrip('.#!')) # lstrip(): strips characters from the left of a string.


# zfill (The zfill() method adds zeros(0) at the beginning of the string. The length of the returned string depends on the width provided.)
print('7'.zfill(3))
print('-21'.zfill(5))
print('Python'.zfill(10))
print('Python'.zfill(3))