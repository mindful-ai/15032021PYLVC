Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # SETS
>>> 
>>> s = "mississippi"
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'i', 's', 'm', 'p'}
>>> 
>>> 
>>> s1 = set("abcdefg")
>>> s1
{'b', 'a', 'f', 'g', 'e', 'd', 'c'}
>>> s2 = { 'd', 'e', 'f', 'g', 'h', 'i', 'j' }
>>> s1
{'b', 'a', 'f', 'g', 'e', 'd', 'c'}
>>> s23
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s23
NameError: name 's23' is not defined
>>> s2
{'f', 'i', 'g', 'j', 'e', 'd', 'h'}
>>> 
>>> 
>>> # -------------------------------------
>>> 
>>> s1 & s2
{'f', 'g', 'd', 'e'}
>>> s1 | s2
{'b', 'a', 'f', 'i', 'g', 'j', 'e', 'd', 'c', 'h'}
>>> s1 ^ s2
{'b', 'h', 'a', 'i', 'j', 'c'}
>>> 
>>> 
>>> # ---------------------------------------
>>> 
>>> s1.set('x')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s1.set('x')
AttributeError: 'set' object has no attribute 'set'
>>> s1.add('x')
>>> s1
{'b', 'x', 'a', 'f', 'g', 'e', 'd', 'c'}
>>> s1.add('a')
>>> s1
{'b', 'x', 'a', 'f', 'g', 'e', 'd', 'c'}
>>> 
>>> s3 = set("mnop")
>>> s3
{'p', 'n', 'o', 'm'}
>>> s1.update(s3)
>>> s1
{'n', 'p', 'b', 'x', 'a', 'f', 'm', 'g', 'o', 'e', 'd', 'c'}
>>> 
>>> # -----------------------------------
>>> 
>>> 'b' in s1
True
>>> 'k' in s1
False
>>> s1.remove('b')
>>> s1
{'n', 'p', 'x', 'a', 'f', 'm', 'g', 'o', 'e', 'd', 'c'}
>>> 
>>> del s3
>>> s3
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s3
NameError: name 's3' is not defined
>>> 
>>> # -----------------------------------
>>> 
>>> s1.intersection(s2)
{'f', 'g', 'd', 'e'}
>>> s1.union(s2)
{'n', 'p', 'x', 'a', 'f', 'm', 'g', 'i', 'j', 'o', 'e', 'd', 'c', 'h'}
>>> 
