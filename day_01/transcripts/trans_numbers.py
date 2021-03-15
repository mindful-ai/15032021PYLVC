Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # NUMBERS
>>> 
>>> a = 4
>>> type(a)
<class 'int'>
>>> b = 1.4
>>> type(b)
<class 'float'>
>>> 
>>> # ----------------------- OPERATORS
>>> 
>>> # ------- Arithmetic Operators
>>> 
>>> a + b
5.4
>>> c =  a + b
>>> print(c)
5.4
>>> c
5.4
>>> a - b
2.6
>>> a * b
5.6
>>> a / b
2.857142857142857
>>> 
>>> 
>>> 5 // 2
2
>>> 5 % 2
1
>>> 5 / 2
2.5
>>> 
>>> 5 ** 2
25
>>> 5 ** 3
125
>>> # ------ RElational Operators
>>> 
>>> a > b # Is a greater than b?
True
>>> a < b
False
>>> a == b
False
>>> a != b
True
>>> a >= b
True
>>> a <= b
False
>>> 
>>> # ----------- Logical operatos
>>> 
>>> a > b and a < 10
True
>>> a > b and a > 10
False
>>> a > b or a > 10
True
>>> a > b and not a > 10
True
>>> 
>>> # ------------------------------ Built in functions
>>> 
>>> a = 100
>>> hex(a)
'0x64'
>>> bin(a)
'0b1100100'
>>> oct(a)
'0o144'
>>> 
>>> b = '100'
>>> type(b)
<class 'str'>
>>> type(a)
<class 'int'>
>>> b + 100
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    b + 100
TypeError: can only concatenate str (not "int") to str
>>> int(a) + b
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int(a) + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> int(b) + a
200
>>> 
>>> c = 'f789'
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'f789'
>>> int(c, 16)
63369
>>> d = 'ksadj987987'
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'ksadj987987'
>>> 
>>> 
>>> a = 5
>>> b = 2
>>> a - b
3
>>> b - a
-3
>>> abs(a - b)
3
>>> abs(b - a)
3
>>> pow(a, 5)
3125
>>> a ** 5
3125
>>> # ------------------- Built in modules
>>> 
>>> gcd(10, 20)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    gcd(10, 20)
NameError: name 'gcd' is not defined
>>> import math
>>> gcd(10, 20)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    gcd(10, 20)
NameError: name 'gcd' is not defined
>>> math.gcd(10, 20)
10
>>> math.log(5)
1.6094379124341003
>>> math.e
2.718281828459045
>>> math.pi
3.141592653589793
>>> 2.7 ** 1.6
4.89984139789623
>>> 
>>> 
>>> ang = 90
>>> math.sin(ang)
0.8939966636005579
>>> math.sin(ang * math.pi/180)
1.0
>>> import random
>>> random.randint(1, 100)
40
>>> random.randint(1, 100)
5
>>> random.randint(1, 100)
41
>>> random.randint(1, 100)
23
>>> random.randint(1, 100)
75
>>> random.randint(1, 100)
53
>>> random.randint(1, 100)
50
>>> math.sin(math.radians(90))
1.0
>>> 
>>> 
>>> # --------------- inputs from the keyboard
>>> 
>>> input()
12
'12'
>>> a = input()
23
>>> a
'23'
>>> type(a)
<class 'str'>
>>> a * 5
'2323232323'
>>> int(a) * 5
115
>>> a = input("Enter a number: ")
Enter a number: 455
>>> a
'455'
>>> a = int(input("Enter a number : "))
Enter a number : 455
>>> a
455
>>> type(a)
<class 'int'>
>>> a + 10
465
>>> 
