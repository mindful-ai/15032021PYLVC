Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "Temperature in Bangalore is 27.4 degree today"
>>> import re
>>> m = re.search(r'\d+\.\d*', s)
>>> m
<re.Match object; span=(28, 32), match='27.4'>
>>> s[28:32]
'27.4'
>>> m
<re.Match object; span=(28, 32), match='27.4'>
>>> m.span()
(28, 32)
>>> m.start()
28
>>> m.end()
32
>>> m.group()
'27.4'
>>> m.groups()
()
>>> m = re.search(r'(\d+)\.(\d*)', s)
>>> m.group()
'27.4'
>>> m.groups()
('27', '4')
>>> m.group(1)
'27'
>>> m.group(2)
'4'
>>> m.groupdict()
{}
>>> m = re.search(r'(?P<decimal>\d+)\.(?P<fraction>\d*)', s)
>>> m.group()
'27.4'
>>> m.groups()
('27', '4')
>>> m.groupdict()
{'decimal': '27', 'fraction': '4'}
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
abc matched in 'abc'
a6c matched in '123 a6c'
abc matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
abc matched in 'abc'
a6c matched in '123 a6c'
abc matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
abc matched in 'abc'
a6c matched in '123 a6c anc'
abc matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
abc matched in 'abc'
abc matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a6c matched in '123 a6c anc'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a55 matched in 'a55b'
a55 matched in 'a555b'
a55 matched in 'a5555b'
a55 matched in 'a55555b'
a55 matched in 'a555555b'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a5e matched in 'a5e'
a6f matched in 'a6f'
a5b matched in 'a5b'
a5x matched in 'a5xb'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
abc matched in 'abc'
a5e matched in 'a5e'
a6f matched in 'a6f'
a6c matched in '123 a6c anc'
a5b matched in 'a5b'
a5x matched in 'a5xb'
abc matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a5e matched in 'a5e'
a6f matched in 'a6f'
a5b matched in 'a5b'
a55 matched in 'a55b'
a55 matched in 'a555b'
a55 matched in 'a5555b'
a55 matched in 'a55555b'
a55 matched in 'a555555b'
a5x matched in 'a5xb'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
bc matched in 'abc'
a6 matched in 'a6f'
a6 matched in '123 a6c anc'
bc matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
123 matched in '123 a6c anc'
55 matched in 'a55b'
555 matched in 'a555b'
5555 matched in 'a5555b'
55555 matched in 'a55555b'
555555 matched in 'a555555b'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
3+2 matched in '3+2=5'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a55 matched in 'a55b'
a55 matched in 'a555b'
a55 matched in 'a5555b'
a55 matched in 'a55555b'
a55 matched in 'a555555b'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a5e matched in 'a5e'
a6f matched in 'a6f'
a6c matched in '123 a6c anc'
a5b matched in 'a5b'
a5x matched in 'a5xb'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
ab  matched in 'ab '
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
123 a matched in '123 a6c anc'
def g matched in 'def ghi'
abc a matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a6 matched in 'a6f'
a6 matched in '123 a6c anc'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a6 matched in 'a6f'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
abc matched in 'abc'
a6c matched in '123 a6c anc'
abc matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
abc matched in 'abc'
anc matched in '123 a6c anc'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
ab matched in 'ab '
ab matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
ab matched in 'abc'
ab matched in 'abc ab'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a55 matched in 'a55b'
a555 matched in 'a555b'
a5555 matched in 'a5555b'
a55555 matched in 'a55555b'
a555555 matched in 'a555555b'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a555 matched in 'a555b'
a5555 matched in 'a5555b'
a55555 matched in 'a55555b'
a555555 matched in 'a555555b'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_05/regex_ex/regex_ex.py ==
a55 matched in 'a55b'
a555 matched in 'a555b'
a555 matched in 'a5555b'
a555 matched in 'a55555b'
a555 matched in 'a555555b'
>>> 
