Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS
>>> 
>>> s = "python"
>>> type(s)
<class 'str'>
>>> 
>>> 
>>> # ------------------------ immutable nature of strings
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[0] = "P"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[0] = "P"
TypeError: 'str' object does not support item assignment
>>> s = "Python"
>>> s[0] = "p"
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[0] = "p"
TypeError: 'str' object does not support item assignment
>>> 
>>> # ------------------------- subscripting
>>> 
>>> s[0]
'P'
>>> s[1]
'y'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[2:4] #tho
'th'
>>> s[2:5]
'tho'
>>> s[0:3]
'Pyt'
>>> s[-5:-2]
'yth'
>>> s[4:5]
'o'
>>> s[4:6]
'on'
>>> s[4:7]
'on'
>>> s[4:10]
'on'
>>> 
>>> s[0:3]
'Pyt'
>>> s[:3]
'Pyt'
>>> s[3:]
'hon'
>>> s[-2:]
'on'
>>> s[:2]
'Py'
>>> 
>>> s[:]
'Python'
>>> 
>>> s[0:6]
'Python'
>>> s[0:6:2]
'Pto'
>>> s[1:6:2]
'yhn'
>>> s[0:6:3]
'Ph'
>>> s[::2]
'Pto'
>>> s[::-1]
'nohtyP'
>>> s[::-2]
'nhy'
>>> s[1:5]
'ytho'
>>> s[1:5:-1]
''
>>> s[1:5][::-1]
'ohty'
>>> 
>>> 
>>> # ---------------------------- operators
>>> 
>>> 'py' + 'th' + 'on'
'python'
>>> 'py' * 5
'pypypypypy'
>>> len(s)
6
>>> 'p' in s
False
>>> 'o' in s
True
>>> 'tho' in s
True
>>> s is str
False
>>> type(s) is str
True
>>> type(s) is int
False
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> # ---------------------- functions
>>> 
>>> # ------------ case of the strings
>>> 
>>> s = "python"
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> 
>>> # ------------ query the strings
>>> 
>>> '1234'.isdigit()
True
>>> int('1234')
1234
>>> '1234A'.isdigit()
False
>>> '1234A'.isalpha()
False
>>> 'ab'.isalpha()
True
>>> '1234A'.isalnum()
True
>>> 
>>> ' '.isspace()
True
>>> "#$%^".isalnum()
False
>>> 
>>> # ---------------- finding substrings
>>> 
>>> s
'python'
>>> 'tho' in s
True
>>> s.find('tho')
2
>>> s.count('o')
1
>>> a = 'mississippi'
>>> a.count(s)
0
>>> a.count('s')
4
>>> # ---------------- string manipulation
>>> 
>>> # Replacement
>>> 
>>> ip = '192-168-1-1'
>>> ip.replace('-', '.')
'192.168.1.1'
>>> ip
'192-168-1-1'
>>> newip = ip.replace('-', '.')
>>> newip
'192.168.1.1'
>>> ip = ip.replace('-', '.')
>>> ip
'192.168.1.1'
>>> 
>>> 
>>> # stripping
>>> 
>>> s = '  1578993 '
>>> s.lstrip()
'1578993 '
>>> s
'  1578993 '
>>> s.rstrip()
'  1578993'
>>> s.strip()
'1578993'
>>> 
>>> 
>>> # justification
>>> 
>>> s = "python"
>>> s.ljust(20)
'python              '
>>> s.rjust(20,'>')
'>>>>>>>>>>>>>>python'
>>> 
>>> 
>>> # querying -> start and end
>>> 
>>> site = "www.google.com"
>>> site.startswith("https")
False
>>> site.endswith("com")
True
>>> 
>>> # split and join
>>> 
>>> text = "mary had a little lamb"
>>> words = text.split()
>>> words
['mary', 'had', 'a', 'little', 'lamb']
>>> type(words)
<class 'list'>
>>> words[0]
'mary'
>>> words[1]
'had'
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 
>>> words
['mary', 'had', 'a', 'little', 'lamb']
>>> '-'.join(words)
'mary-had-a-little-lamb'
>>> 
>>> 
>>> # --------------------- iteration
>>> 
>>> for ch in s:
	print(ch)

	
p
y
t
h
o
n
>>> for ch in s:
	print(ch.replace(ch, '*'))

	
*
*
*
*
*
*
>>> for i in s:
	print(s.replace(ch, '*'))

	
pytho*
pytho*
pytho*
pytho*
pytho*
pytho*
>>> for i in s:
	print(s.replace(i, '*'))

	
*ython
p*thon
py*hon
pyt*on
pyth*n
pytho*
>>> 
>>> 
>>> # ------------------------------- example
>>> 
>>> for i in '12345':
	print("*" * int(i))

	
*
**
***
****
*****
>>> 
