Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m = re.match(r"\d+\.\d+", "24.1632")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    m = re.match(r"\d+\.\d+", "24.1632")
NameError: name 're' is not defined
>>> import re
>>> text = "This contains a 12.34556 floating point value"
>>> m = re.match(r"\d+\.\d+", "24.1632")
>>> type(m0
     )
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type(m0
NameError: name 'm0' is not defined
>>> m
<re.Match object; span=(0, 7), match='24.1632'>
>>> m.group()
'24.1632'
>>> m = re.match(r"\d+\.\d+", text)
>>> m.group()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    m.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> m
>>> m = re.search(r"\d+\.\d+", text)
>>> m
<re.Match object; span=(16, 24), match='12.34556'>
>>> m.group()
'12.34556'
>>> m.span()
(16, 24)
>>> text[16:24]
'12.34556'
>>> m = re.search(r"(\d+)\.(\d+)", text)
>>> m.group()
'12.34556'
>>> m.group(1)
'12'
>>> m.group(2)
'34556'
>>> m.groups()
('12', '34556')
>>> m.groupdict()
{}
>>> m = re.search(r"(?P<beforedot>\d+)\.(?P<afterdot>\d+)", text)
>>> m.group()
'12.34556'
>>> m.groups()
('12', '34556')
>>> m.groupdict()
{'beforedot': '12', 'afterdot': '34556'}
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
abc matched in 'abc'
a6c matched in '123 a6c'
abc matched in 'abc ab'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
abc matched in 'abc'
a6c matched in '123 a6c'
abc matched in 'abc ab'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
a5e matched in 'a5e'
a6f matched in 'a6f'
a5b matched in 'a5b'
a5x matched in 'a5xb'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
abc matched in 'abc'
a5e matched in 'a5e'
a6f matched in 'a6f'
a6c matched in '123 a6c'
a5b matched in 'a5b'
a5x matched in 'a5xb'
abc matched in 'abc ab'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
abc matched in 'abc'
a6c matched in '123 a6c'
a55 matched in 'a55b'
a55 matched in 'a555b'
a55 matched in 'a5555b'
a55 matched in 'a55555b'
a55 matched in 'a555555b'
abc matched in 'abc ab'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
abc matched in 'abc'
a6c matched in '123 a6c'
abc matched in 'abc ab'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
123 matched in '123 a6c'
55 matched in 'a55b'
555 matched in 'a555b'
5555 matched in 'a5555b'
55555 matched in 'a55555b'
555555 matched in 'a555555b'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
3+2 matched in '3+2=5'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
a6 matched in 'a6f'
a6 matched in '123 a6c'
de matched in 'def ghi'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
abc matched in 'abc'
abc matched in 'abc ab'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
123 a matched in '123 a6c'
def g matched in 'def ghi'
abc a matched in 'abc ab'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
a6 matched in 'a6f'
a6 matched in '123 a6c'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
a6 matched in 'a6f'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
abc matched in 'abc'
a6c matched in '123 a6c'
abc matched in 'abc ab'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_04/session_03/regex_ex/regex_ex.py 
abc matched in 'abc'
a6c matched in '123 a6c'
>>> 
