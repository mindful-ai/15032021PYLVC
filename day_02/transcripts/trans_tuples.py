Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # TUPLE
>>> 
>>> T = ("red", "green", "blue")
>>> type(T)
<class 'tuple'>
>>> 
>>> # -------------- access elements
>>> T[0]
'red'
>>> T[-1]
'blue'
>>> T[::-1]
('blue', 'green', 'red')
>>> 
>>> # -------------- rearranging
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> sorted(T)
['blue', 'green', 'red']
>>> T
('red', 'green', 'blue')
>>> reversed(T)
<reversed object at 0x00000149A4035588>
>>> 
>>> # ------------------ adding removing
>>> # Not allowed in tuples
>>> # replacement is also not allowed
>>> 
>>> T[0]
'red'
>>> T[0] = "orange"
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    T[0] = "orange"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> # ------------- making changes
>>> 
>>> T
('red', 'green', 'blue')
>>> T = list(T)
>>> T
['red', 'green', 'blue']
>>> T[0] = "orange"
>>> T = tuple(T)
>>> T
('orange', 'green', 'blue')
>>> 
>>> # ---------------- list objects in a tuple
>>> 
>>> T = ('red', 'green', 'blue', ['white', 'black'])
>>> T[-1]
['white', 'black']
>>> T[-1] = ["brown", "yellow"]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    T[-1] = ["brown", "yellow"]
TypeError: 'tuple' object does not support item assignment
>>> T[-1].append("grey")
>>> T
('red', 'green', 'blue', ['white', 'black', 'grey'])
>>> T[-1][1]
'black'
>>> T[-1][1] = "yellow"
>>> T
('red', 'green', 'blue', ['white', 'yellow', 'grey'])
>>> ('red', 'green', 'blue', ['white', 'yellow', 'grey'])
('red', 'green', 'blue', ['white', 'yellow', 'grey'])
>>> 
>>> 
>>> # --------------------------- unpacking tuples / collections
>>> 
>>> T
('red', 'green', 'blue', ['white', 'yellow', 'grey'])
]
>>> T = ('red', 'green', 'blue')
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> 
>>> r,g = T
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    r,g = T
ValueError: too many values to unpack (expected 2)
>>> r, g, *others = T
>>> r
'red'
>>> g
'green'
>>> other
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    other
NameError: name 'other' is not defined
>>> others
['blue']
>>> T = ('red', 'green', 'blue', 'white', 'black')
>>> r, g, *o = T
>>> r
'red'
>>> g
'green'
>>> o
['blue', 'white', 'black']
>>> 
