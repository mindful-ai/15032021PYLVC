# Data Types

Numbers - numerical values
Operators - arithmetic, relational, logical,
built-in functions - int(), float(), bin(), oct(), hex(), abs(),
modules - math, random

Strings - collection of characters - "", '', '''  '''
Operators - + * len in del
built-in functions -
case - upper(), lower(), capitalize()
querying - isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith()
searching - count(), find()
modifications - replace(), split(), join(), strip(), lstrip(), rstrip(), rjust(), ljust()
iteration -> for loop
format()

Lists = ordered collection of objects - []
Operators + * len in del
accessability [start:end:skip] [0] [3:6] [1:10:2]
replace L[5] = Value/object
built-in functions
adding values append(), extend(), insert()
removing elements pop(), remove()
searching index(), count()
re-arranging sort(), reverse(), sorted(), reversed()
copying -> deepcopy()
iteration -> for loop
other misc -> max(), min(), sum(), any(), all()

Tuples = ordered collection of objects - () -> immutable list
Operators + * len in del
accessability [start:end:skip] [0] [3:6] [1:10:2]
searching index(), count()
re-arranging sorted(), reversed()
copying -> deepcopy()
iteration -> for loop

Lists/Tuple    x,y,*z = ('red', 'green', 'yellow', 'blue')

Sets = unordered collection - {} -> immutable -> mathematical set theory
Operators | & ^
built-ins -> add(), update(), remove(), intersection(), union()
iteration -> for loop

Dictionaries = unordered collection -> { key:Value }
d[key] = value -> to add a new key value pair
d.setdefault()
d.remove(), d.pop()
d.update()
d.keys(), d.values(), d.items()
iteration -> for loop

Interconversion functions: int, float, str, chr, ord, list, tuple, set, dict

# -------------------------------- BRANCHING

if <condition>:
    <statements>
elif <condition>:
    <statements>
..
..
else:
    <statements>


# ------------------------------- LOOPING

for <var> in <iterable>:
    <statements>
else:
    <statement>

while <condition>:
    <statement>
else:
    <statement>

break statement
continue statement

# ------------------------------ FUNCTIONS/MODULES

def <fucntionname>(<arg1>, <arg2> ....):
    <logic>
    return <expr>

# ----------------------------------------------

modules.py -> module/package/library
    <collection of functions>
    def function()
        return <expr>

if __name__ == '__main__':

    <test code>

# ---------------------------------------

import module
module.function()

# ----------------------------------------------

Lambda function: fobj = lambda x,y : x + y
Special functions: map(), filter(), zip()

Special modules:
datetime -> now(), strftime(), t1 + t2, <format strings>
functools -> reduce()
itertools -> permutation(), combination()
collections -> Counter()
operator -> itemgetter()



# ----------------------------------------------

comprehensions -> [<expr> <loop> <condition>]

exception handling ->
try:
    <statements>
except:
    <statements>
else:
    <statements>
finally:
    <statements>

# ------------------------------------ REGEX

Regular Expressions -> re module -> match(), search(), findall(), finditer()
group(), groups(), groupdict(), span(), start(), end(), sub(), subn()
Metacharacters -> . [abc] [^abc] \ | \d \w \s \D \W \S * + ? {m,n} $ ^ \b \B

www.regex101.com



# -----------------------------------------------------

os -> mkdir(), chdir(), getcwd() .....
os.path -> join(), splitext(), basename() ...
shutil -> move(), copy()
subprocess -> call(), check_output()

csv -> Writer, Reader, DictReader
json -> load(), dump()

# --------------------------------------------------------------------- OOP 


OOP - class, object, inheritance, polymorphism, multiple inheritance,

__repr__, __str__, __len__, __iter__, __next__, operator overloading

class class1(object):

    # data items

    # methods

classmodule.py

    class class1(object):

        # data items

        # methods

    class class2(object):

        # data items

        # methods
# -----------------------------------------------------

import classmodule
o1 = classmodule.class1()
o2 = classmodule.class2()

# ------------------------------------------------- MISC OOP

decorators
custom exceptions
logging
csv
json






# --------------------------------------------------------------

Pickle and Shelve -> Data Persistance
Testing -> unittest.Test
ORM -> mysql.conenctor connect(), cursor(), execute(), executemany(), fetchall()
Socket -> Server: socket(), bind(), listen(), accept(), send(), receive(), decode(), encode()
          Client: connect()
Flask framework
Introduction to REST API -> requests

# -----------------------------------------------------------


virtualenv myenv
myenv/Scripts/activate
deactivate

pip freeze > requirements.txt 
pip install -r requirements.txt
pip install modulename
pip uninstall modulename

myapp
    mypackage
        __init__.py   -> import all the functions from the .py module
        a.py
        b.py
    setup.py   -> import setuptools -> setup configuration

cd myapp -> pip install . -> mypackage will be installed globally

# -----------------------------------------------------------------

import pandas as pd
df = pd.read_csv("student.csv")

df.head()
df.tail()
df.columns

df['name']
df[['name', 'regid', 'avg']]
df['newcol'] = df['phy'] + df['chem'] + df['bio'] + df['math']


df.loc[0]
df.iloc[0]
df.iloc[[7,1,2,3]]

df.drop('newcol', axis=1, inplace=True)
df.drop([2,3,4])

df['newcol'] = df[['phy', 'chem', 'math', 'bio']].mean(axis=1)
df['avg'] = df[['phy', 'chem', 'math', 'bio']].mean(axis=1)

df['rank'] = df['avg'].rank()
df['rank'] = df['avg'].rank(method='dense', ascending=False)

import matplotlib.pyplot as plt
plt.bar(df['regid'], df['avg'], color='m')
plt.show()

with pd.ExcelWriter('report.xlsx') as writer:
    df.to_excel(writer)

-------------------------------------------------------

Test Suite:

def setUp(self):
        self.calc = Calculator()

    def test_last_answer_init(self):
        value = self.calc.last_answer
        self.assertEqual(value, 0.0, FAILURE)

    def test_add(self):
        value = self.calc.add(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 5.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_subtract(self):
        value = self.calc.subtract(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_subtract_negative(self):
        value = self.calc.subtract(NUMBER_2, NUMBER_1)
        self.assertEqual(value, -1.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_multiply(self):
        value = self.calc.multiply(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 6.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide(self):
        value = self.calc.divide(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.5, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, NUMBER_1, 0)

    def test_max_greater(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_max_less(self):
        value = self.calc.maximum(NUMBER_2, NUMBER_1)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_max_equal(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_1)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_min_greater(self):
        value = self.calc.minimum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_min_less(self):
        value = self.calc.minimum(NUMBER_2, NUMBER_1)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_min_equal(self):
        value = self.calc.minimum(NUMBER_2, NUMBER_2)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_force_value(self):
        self.calc._last_answer = 5
        value = self.calc._last_answer
        self.assertEqual(value, 5, FAILURE)

    def tearDown(self):
        pass
    
    
# -----------------------------------------------------------------------------------------

Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> L = [(x, x**2) for x in range(20) if x % 2 == 0]
>>> L
[(0, 0), (2, 4), (4, 16), (6, 36), (8, 64), (10, 100), (12, 144), (14, 196), (16, 256), (18, 324)]
>>> # {}, (), [] => <expr> <loop> <condition>
... 
>>> L = ["red", "green", "blue", "orange", "yellow"]
>>> D = { k:len(k) for k in L }
>>> D
{'red': 3, 'green': 5, 'blue': 4, 'orange': 6, 'yellow': 6}
>>> import random
>>> LR = [ random.randint(1, 100) for x in range(10) ]
>>> LR
[94, 84, 97, 80, 23, 68, 99, 10, 51, 25]
>>> 
>>> 
>>> 
>>> N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> L1 = ( x**2 for x in N if x % 3 == 0)
>>> L1
<generator object <genexpr> at 0x000001889A6269A8>
>>> list(L1)
[9, 36, 81]
>>> L2 = ( x**2 if x % 3 == 0 else x for x in N)
>>> L2
<generator object <genexpr> at 0x000001889A626930>
>>> list(L2)
[1, 2, 9, 4, 5, 36, 7, 8, 81, 10]
>>>
>>> L3 = [ x for x in random.randint(1, 100) if x % 5 == 0}
  File "<stdin>", line 1
    L3 = [ x for x in random.randint(1, 100) if x % 5 == 0}
                                                          ^
SyntaxError: invalid syntax
>>> L3 = [ x for x in random.randint(1, 100) if x % 5 == 0 ]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> R = [random.randint(1, 100) for x in range(10)]          
>>> R
[56, 74, 35, 84, 50, 75, 38, 55, 11, 14]
>>> R5 = [ x for x in [random.randint(1, 100) for i in range(30)] if x % 5 == 0]
>>> R5
[30, 50, 5, 20, 80, 80]
>>>
