Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add2(x, y):

	return x + y

>>> type(add2)
<class 'function'>
>>> 
>>> 
>>> f = lambda x,y:x+y
>>> type(f)
<class 'function'>
>>> f(10, 20)
30
>>> f("abc", "def")
'abcdef'
>>> # -------------------------------- map()
>>> 
>>> T = [10, 40, 90, 100]
>>> F = []
>>> for t in T:
	F.append(t * 1.8 + 32)

	
>>> F
[50.0, 104.0, 194.0, 212.0]
>>> F1 = map(lambda t : t * 1.8 + 32, T)
>>> F1
<map object at 0x00000292F92B5358>
>>> list(F1)
[50.0, 104.0, 194.0, 212.0]
>>> 
>>> 
>>> def conv2farh(t):
	return t * 1.8 + 32

>>> F2 = map(conv2farh, T)
>>> list(F2)
[50.0, 104.0, 194.0, 212.0]
>>> 
>>> # ----------------------------------- filter()
>>> 
>>> import random
>>> R = []
>>> for i in range(100):
	R.append(random.randint(1, 100))

	
>>> R
[48, 39, 22, 83, 84, 88, 100, 3, 29, 23, 70, 38, 90, 7, 8, 100, 74, 13, 42, 13, 15, 63, 90, 1, 19, 33, 44, 47, 18, 76, 9, 21, 2, 95, 11, 87, 56, 22, 36, 93, 11, 36, 1, 31, 19, 33, 73, 61, 100, 54, 90, 6, 91, 84, 36, 82, 15, 3, 31, 6, 41, 95, 8, 76, 50, 60, 47, 98, 61, 62, 46, 64, 69, 73, 58, 52, 20, 43, 91, 83, 56, 78, 87, 53, 29, 20, 18, 74, 5, 36, 89, 74, 87, 56, 32, 44, 50, 35, 38, 62]
>>> 
>>> D9 = filter(lambda n : n % 9 == 0, R)
>>> D9
<filter object at 0x00000292F92B5518>
>>> list(D9)
[90, 63, 90, 18, 9, 36, 36, 54, 90, 36, 18, 36]
>>> 
>>> # ----------------------------------- zip()
>>> 
>>> T1 = ("Anil", "Sunil", "Raj")
>>> T2 = ("Chennai", "Pune", "bangalore")
>>> zip(T1, T2)
<zip object at 0x00000292F935A908>
>>> list(zip(T1, T2))
[('Anil', 'Chennai'), ('Sunil', 'Pune'), ('Raj', 'bangalore')]
>>> dict(zip(T1, T2))
{'Anil': 'Chennai', 'Sunil': 'Pune', 'Raj': 'bangalore'}
>>> {'Anil': 'Chennai', 'Sunil': 'Pune', 'Raj': 'bangalore'}
{'Anil': 'Chennai', 'Sunil': 'Pune', 'Raj': 'bangalore'}
>>> 
>>> 
>>> 
>>> D = {'Anil': 'Chennai', 'Sunil': 'Pune', 'Raj': 'bangalore'}
>>> zip(*D)
<zip object at 0x00000292F932D308>
>>> list(zip(*D))
[('A', 'S', 'R'), ('n', 'u', 'a'), ('i', 'n', 'j')]
>>> D
{'Anil': 'Chennai', 'Sunil': 'Pune', 'Raj': 'bangalore'}
>>> list(zip(*D.items()))
[('Anil', 'Sunil', 'Raj'), ('Chennai', 'Pune', 'bangalore')]
>>> 
