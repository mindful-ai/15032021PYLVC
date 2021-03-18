Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> 
>>> m = re.search(r"\d+\.\d+", "The value is 24.1632")
>>> m
<re.Match object; span=(13, 20), match='24.1632'>
>>> s = "The value is 24.1632"
>>> s[13:20]
'24.1632'
>>> 
>>> 
>>> m = re.search(r"(\d+)\.(\d+)", "The value is 24.1632")
>>> m
<re.Match object; span=(13, 20), match='24.1632'>
>>> m.group()
'24.1632'
>>> m.span()
(13, 20)
>>> m.groups()
('24', '1632')
>>> m.groups()[0]
'24'
>>> m.groups()[1]
'1632'
>>> m = re.search(r"(:?<decimal>\d+)\.(:?<floating>\d+)", "The value is 24.1632")
>>> m.group()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    m.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> m
>>> m = re.search(r"(?P<decimal>\d+)\.(?P<floating>\d+)", "The value is 24.1632")
>>> m
<re.Match object; span=(13, 20), match='24.1632'>
>>> m.group()
'24.1632'
>>> m.group(1)
'24'
>>> m.group(2)
'1632'
>>> m.groups()
('24', '1632')
>>> m.groupdict()
{'decimal': '24', 'floating': '1632'}
>>> 
