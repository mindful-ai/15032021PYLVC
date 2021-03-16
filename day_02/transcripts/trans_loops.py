Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for c in "python":
	print(c)

	
p
y
t
h
o
n
>>> for c in "python":
	print(c, end=' ')

	
p y t h o n 
>>> for c in "python":
	print(c, end='\t')

	
p	y	t	h	o	n	
>>> 
>>> for item in ["red", "green", "blue"]:
	print(item.upper())

	
RED
GREEN
BLUE
>>> for item in ("red", "green", "blue"):
	print(item.upper())

	
RED
GREEN
BLUE
>>> for item in {"red", "green", "blue"}:
	print(item.upper())

	
GREEN
RED
BLUE
>>> D = {"name", "Anil", "age":35}
SyntaxError: invalid syntax
>>> D = {"name": "Anil", "age":35}
>>> for item in D:
	print(item)

	
name
age
>>> for item in D.keys():
	print(item)

	
name
age
>>> for item in D.values():
	print(item)

	
Anil
35
>>> for item in D.items():
	print(item)

	
('name', 'Anil')
('age', 35)
>>> 
>>> D
{'name': 'Anil', 'age': 35}
>>> D1 = {}
>>> for k, v in D.items():
	D1[v] = k

	
>>> D1
{'Anil': 'name', 35: 'age'}
>>> 
>>> N = [1, 2, 3, 4, 5]
>>> for n in N:
	print(n)

	
1
2
3
4
5
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 30))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(20, 40, 2))
[20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
>>> list(range(20, 0, -1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
>>> for i in range(10):
	print(i, " python")

	
0  python
1  python
2  python
3  python
4  python
5  python
6  python
7  python
8  python
9  python
>>> 
>>> # -------------------------------- Loop controls
>>> 
>>> for i in range(10):
	print(i, " python")
	if(i == 5):
		break

	
0  python
1  python
2  python
3  python
4  python
5  python
>>> for i in range(10):
	print(i, " python")
	if(i == 5):
		continue

	
0  python
1  python
2  python
3  python
4  python
5  python
6  python
7  python
8  python
9  python
>>> for i in range(10):
	if(i == 5):
		continue
	print(i, "python")

	
0 python
1 python
2 python
3 python
4 python
6 python
7 python
8 python
9 python
>>> 
>>> # ---------------------- while loop
>>> 
>>> n = 1
>>> while n <= 10:
	print(n)
	n += 1

	
1
2
3
4
5
6
7
8
9
10
>>> 
