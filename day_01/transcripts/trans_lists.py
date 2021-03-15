Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["red", "blue", "green", 1, 2, -4, 1.56, ['a', 'e', 'i']]
>>> L
['red', 'blue', 'green', 1, 2, -4, 1.56, ['a', 'e', 'i']]
>>> type(L)
<class 'list'>
>>> 
>>> # ------------------- accessing elements
>>> L[0]
'red'
>>> L[1]
'blue'
>>> L[-1]
['a', 'e', 'i']
>>> L[-1][1]
'e'
>>> L[:]
['red', 'blue', 'green', 1, 2, -4, 1.56, ['a', 'e', 'i']]
>>> :[::2]
SyntaxError: invalid syntax
>>> L[::2]
['red', 'green', 2, 1.56]
>>> L[::-1]
[['a', 'e', 'i'], 1.56, -4, 2, 1, 'green', 'blue', 'red']
>>> 
>>> # -------------------- mutability
>>> 
>>> L
['red', 'blue', 'green', 1, 2, -4, 1.56, ['a', 'e', 'i']]
>>> L[2]
'green'
>>> L[2] = "yellow"
>>> L
['red', 'blue', 'yellow', 1, 2, -4, 1.56, ['a', 'e', 'i']]
>>> 
>>> L[2][2]
'l'
>>> L[2][2] = "k"
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    L[2][2] = "k"
TypeError: 'str' object does not support item assignment
>>> 
>>> # -------------------- replacing elements
>>> 
>>> L = ["red", "green", "blue"]
>>> L
['red', 'green', 'blue']
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> L1 = ["black", "white"]
>>> L[1]
'yellow'
>>> L[1] = L1
>>> L
['red', ['black', 'white'], 'blue']
>>> 
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1:2]
['green']
>>> L[1:2] = L1
>>> L
['red', 'black', 'white', 'blue']
>>> 
>>> # ----------------------- operators
>>> 
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> "red" in L
True
>>> type(L) is list
True
>>> len(L)
4
>>> del L[0]
>>> L
['black', 'white', 'blue']
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> # ----------------------- add elements to a list
>>> L = ["red", "green", "blue"]
>>> L1
['black', 'white']
>>> 
>>> L.append("yellow")
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.append("pink")
>>> L
['red', 'green', 'blue', 'yellow', 'pink']
>>> L.insert(2, "orange")
>>> L
['red', 'green', 'orange', 'blue', 'yellow', 'pink']
>>> L.extend(L1)
>>> L
['red', 'green', 'orange', 'blue', 'yellow', 'pink', 'black', 'white']
>>> 
>>> # --------------------- remove elements
>>> 
>>> L
['red', 'green', 'orange', 'blue', 'yellow', 'pink', 'black', 'white']
>>> L.pop()
'white'
>>> L
['red', 'green', 'orange', 'blue', 'yellow', 'pink', 'black']
>>> L.pop()
'black'
>>> L.pop(2)
'orange'
>>> 'yellow' in L
True
>>> L.remove('yellow')
>>> L
['red', 'green', 'blue', 'pink']
>>> 
>>> # --------------------------- search in a list
>>> 
>>> L
['red', 'green', 'blue', 'pink']
>>> 'red' in L
True
>>> L.index('red')
0
>>> L.index('blue')
2
>>> L.index('black')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    L.index('black')
ValueError: 'black' is not in list
>>> L.find('black')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    L.find('black')
AttributeError: 'list' object has no attribute 'find'
>>> 
>>> L.count("red")
1
>>> L.append("red")
>>> L.count("red")
2
>>> L
['red', 'green', 'blue', 'pink', 'red']
>>> 
>>> # --------------------------------- rearrange elements
>>> 
>>> # SORTING
>>> 
>>> L
['red', 'green', 'blue', 'pink', 'red']
>>> sorted(L)
['blue', 'green', 'pink', 'red', 'red']
>>> L
['red', 'green', 'blue', 'pink', 'red']
>>> L.sort()
>>> L
['blue', 'green', 'pink', 'red', 'red']
>>> 
>>> # REVERSING
>>> L
['blue', 'green', 'pink', 'red', 'red']
>>> reversed(L)
<list_reverseiterator object at 0x000001D661F0EDA0>
>>> list(reversed(L))
['red', 'red', 'pink', 'green', 'blue']
>>> L
['blue', 'green', 'pink', 'red', 'red']
>>> L.reverse()
>>> L
['red', 'red', 'pink', 'green', 'blue']
>>> 
>>> 
>>> # Special
>>> 
>>> L = ["red", "green", ["apples", "cats"]]
>>> L.sort()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    L.sort()
TypeError: '<' not supported between instances of 'list' and 'str'
>>> L.sort(key=itemgetter(0))
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    L.sort(key=itemgetter(0))
NameError: name 'itemgetter' is not defined
>>> from operator import itemgetter
>>> L.sort(key=itemgetter(0))
>>> L
[['apples', 'cats'], 'green', 'red']
>>> 
>>> # -------------------- iterating
>>> 
>>> L
[['apples', 'cats'], 'green', 'red']
>>> L = ['red', 'green', 'blue', 'pink', 'red']
>>> for item in L:
	print(item)

	
red
green
blue
pink
red
>>> for item in L:
	print(item.upper())

	
RED
GREEN
BLUE
PINK
RED
>>> for item in sorted(L):
	print(item.upper())

	
BLUE
GREEN
PINK
RED
RED
>>> 
