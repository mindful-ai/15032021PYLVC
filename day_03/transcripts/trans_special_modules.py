Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -------------------------- datetime
>>> 
>>> from datetime import datetime
>>> t = datetime.now()
>>> t
datetime.datetime(2021, 3, 17, 17, 5, 41, 26848)
>>> t.year
2021
>>> t.month
3
>>> t.day
17
>>> d.hour
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d.hour
NameError: name 'd' is not defined
>>> t.hour
17
>>> t.minute
5
>>> t.second
41
>>> 
>>> 
>>> "Wednesday, 17 March 2021, 5:07 PM"
'Wednesday, 17 March 2021, 5:07 PM'
>>> f = "%A, %d %B %Y, %I:%M %p"
>>> t
datetime.datetime(2021, 3, 17, 17, 5, 41, 26848)
>>> t.strftime(f)
'Wednesday, 17 March 2021, 05:05 PM'
>>> type(t)
<class 'datetime.datetime'>
>>> 
>>> datetime.now().strftime(f)
'Wednesday, 17 March 2021, 05:10 PM'
>>> t
datetime.datetime(2021, 3, 17, 17, 5, 41, 26848)
>>> t1 = datetime.now()
>>> 
>>> t1 - t
datetime.timedelta(seconds=324, microseconds=847266)
>>> 
>>> # --------------------------------- Collections
>>> 
>>> t = "mary had a little lamb"
>>> words = t.split()
>>> D = {}
>>> for word in words:
	if word in D:
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
>>> D
{'mary': 1, 'had': 1, 'a': 1, 'little': 1, 'lamb': 1}
>>> 
>>> from collections import Counter
>>> words
['mary', 'had', 'a', 'little', 'lamb']
>>> z = Counter(words)
>>> z
Counter({'mary': 1, 'had': 1, 'a': 1, 'little': 1, 'lamb': 1})
>>> 
>>> 
>>> # ----------------------------------- itertools
>>> 
>>> from itertools import permutations, combinations
>>> 
>>> s = "abcd"
>>> list(permutations(s))
[('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ('a', 'c', 'b', 'd'), ('a', 'c', 'd', 'b'), ('a', 'd', 'b', 'c'), ('a', 'd', 'c', 'b'), ('b', 'a', 'c', 'd'), ('b', 'a', 'd', 'c'), ('b', 'c', 'a', 'd'), ('b', 'c', 'd', 'a'), ('b', 'd', 'a', 'c'), ('b', 'd', 'c', 'a'), ('c', 'a', 'b', 'd'), ('c', 'a', 'd', 'b'), ('c', 'b', 'a', 'd'), ('c', 'b', 'd', 'a'), ('c', 'd', 'a', 'b'), ('c', 'd', 'b', 'a'), ('d', 'a', 'b', 'c'), ('d', 'a', 'c', 'b'), ('d', 'b', 'a', 'c'), ('d', 'b', 'c', 'a'), ('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')]
>>> list(combinations(s, 3))
[('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
>>> list(combinations(s, 4))
[('a', 'b', 'c', 'd')]
>>> 
>>> # ------------------------------------ functools
>>> 
>>> from functools import reduce
>>> L = [1,2,3,4]
>>> reduce(lambda x, y: x + y, L)
10
>>> map(lambda x, y: x + y, L)
<map object at 0x000001AC91A7CDA0>
>>> list(map(lambda x, y: x + y, L))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list(map(lambda x, y: x + y, L))
TypeError: <lambda>() missing 1 required positional argument: 'y'
>>> 
>>> 
>>> sum(L)
10
>>> 
>>> # -------------------------------------- operators
>>> 
>>> from operator import itemgetter
>>> itemgetter(1)("apples")
'p'
>>> itemgetter(1)(["apples", "mangoes", "grapes"])
'mangoes'
>>> f = itemgetter(1)
>>> type(f)
<class 'operator.itemgetter'>
>>> 
>>> f("can")
'a'
>>> f(["apples", "mangoes", "grapes"])
'mangoes'
>>> f([ (1, "red"), (2, "blue") ])
(2, 'blue')
>>> 
>>> 
>>> L = ["cat", "ant", "donkey", "zebra", "giraffe"]
>>> L.sort()
>>> L
['ant', 'cat', 'donkey', 'giraffe', 'zebra']
>>> L.sort(key=itemgetter(-1))
>>> L
['zebra', 'giraffe', 'ant', 'cat', 'donkey']
>>> 
>>> 
>>> L = [(3, "sunil"), (1, "anil"), (2, "raj")]
>>> L.sort()
>>> L
[(1, 'anil'), (2, 'raj'), (3, 'sunil')]
>>> L.sort(key=itemgetter(1))
>>> L
[(1, 'anil'), (2, 'raj'), (3, 'sunil')]
>>> L = [(2, "sunil"), (1, "anil"), (3, "raj")]
>>> L.sort()
>>> L
[(1, 'anil'), (2, 'sunil'), (3, 'raj')]
>>> L.sort(key=itemgetter(1))
>>> L
[(1, 'anil'), (3, 'raj'), (2, 'sunil')]
>>> 
