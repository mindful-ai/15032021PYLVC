Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILE IO
>>> 
>>> # open(), close()
>>> # read(), readline(), readlines()
>>> # write(), writelines()
>>> # tell(), seek()
>>> 
>>> path = "C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\data.txt"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = "c:\new\text\read\a.dat"
>>> print(path)
c:
ew	extead.dat
>>> path = r"c:\new\text\read\a.dat"
>>> print(path)
c:\new\text\read\a.dat
>>> path = r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\data.txt"
>>> f = open(path, "r")
>>> # Mode
>>> # r -> read, w -> writing, a -> appending, b -> binary
>>> 
>>> f.read()
'On a dark desert highway, cool wind in my hair\nWarm smell of colitas, rising up through the air\nUp ahead in the distance, I saw a shimmering light\nMy head grew heavy and my sight grew dim\nI had to stop for the night\nThere she stood in the doorway;\nI heard the mission bell\nAnd I was thinking to myself,\n"This could be Heaven or this could be Hell"\nThen she lit up a candle and she showed me the way\nThere were voices down the corridor,\nI thought I heard them say...\nWelcome to the Hotel California\nSuch a lovely place (Such a lovely place)\nSuch a lovely face\nPlenty of room at the Hotel California\nAny time of year (Any time of year)\nYou can find it here\nHer mind is Tiffany-twisted, she got the Mercedes bends\nShe got a lot of pretty, pretty boys she calls friends\nHow they dance in the courtyard, sweet summer sweat.\nSome dance to remember, some dance to forget\nSo I called up the Captain,\n"Please bring me my wine"\nHe said, "We haven\'t had that spirit here since nineteen sixty nine"\nAnd still those voices are calling from far away,\nWake you up in the middle of the night\nJust to hear them say...\nWelcome to the Hotel California\nSuch a lovely place (Such a lovely place)\nSuch a lovely face\nThey livin\' it up at the Hotel California\nWhat a nice surprise (what a nice surprise)\nBring your alibis\nMirrors on the ceiling,\nThe pink champagne on ice\nAnd she said "We are all just prisoners here, of our own device"\nAnd in the master\'s chambers,\nThey gathered for the feast\nThey stab it with their steely knives,\nBut they just can\'t kill the beast\nLast thing I remember, I was\nRunning for the door\nI had to find the passage back\nTo the place I was before\n"Relax, " said the night man,\n"We are programmed to receive.\nYou can check-out any time you like,\nBut you can never leave! "'
>>> c = f.read()
>>> c
''
>>> f.tell()
1824
>>> f.seek(0)
0
>>> c = f.read()
>>> type(c)
<class 'str'>
>>> print(c)
On a dark desert highway, cool wind in my hair
Warm smell of colitas, rising up through the air
Up ahead in the distance, I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night
There she stood in the doorway;
I heard the mission bell
And I was thinking to myself,
"This could be Heaven or this could be Hell"
Then she lit up a candle and she showed me the way
There were voices down the corridor,
I thought I heard them say...
Welcome to the Hotel California
Such a lovely place (Such a lovely place)
Such a lovely face
Plenty of room at the Hotel California
Any time of year (Any time of year)
You can find it here
Her mind is Tiffany-twisted, she got the Mercedes bends
She got a lot of pretty, pretty boys she calls friends
How they dance in the courtyard, sweet summer sweat.
Some dance to remember, some dance to forget
So I called up the Captain,
"Please bring me my wine"
He said, "We haven't had that spirit here since nineteen sixty nine"
And still those voices are calling from far away,
Wake you up in the middle of the night
Just to hear them say...
Welcome to the Hotel California
Such a lovely place (Such a lovely place)
Such a lovely face
They livin' it up at the Hotel California
What a nice surprise (what a nice surprise)
Bring your alibis
Mirrors on the ceiling,
The pink champagne on ice
And she said "We are all just prisoners here, of our own device"
And in the master's chambers,
They gathered for the feast
They stab it with their steely knives,
But they just can't kill the beast
Last thing I remember, I was
Running for the door
I had to find the passage back
To the place I was before
"Relax, " said the night man,
"We are programmed to receive.
You can check-out any time you like,
But you can never leave! "
>>> f.seek(0)
0
>>> f.read(100)
'On a dark desert highway, cool wind in my hair\nWarm smell of colitas, rising up through the air\nUp a'
>>> f.read(100)
'head in the distance, I saw a shimmering light\nMy head grew heavy and my sight grew dim\nI had to sto'
>>> f.readline()
'p for the night\n'
>>> f.readline()
'There she stood in the doorway;\n'
>>> f.readline()
'I heard the mission bell\n'
>>> f.readlines()
['And I was thinking to myself,\n', '"This could be Heaven or this could be Hell"\n', 'Then she lit up a candle and she showed me the way\n', 'There were voices down the corridor,\n', 'I thought I heard them say...\n', 'Welcome to the Hotel California\n', 'Such a lovely place (Such a lovely place)\n', 'Such a lovely face\n', 'Plenty of room at the Hotel California\n', 'Any time of year (Any time of year)\n', 'You can find it here\n', 'Her mind is Tiffany-twisted, she got the Mercedes bends\n', 'She got a lot of pretty, pretty boys she calls friends\n', 'How they dance in the courtyard, sweet summer sweat.\n', 'Some dance to remember, some dance to forget\n', 'So I called up the Captain,\n', '"Please bring me my wine"\n', 'He said, "We haven\'t had that spirit here since nineteen sixty nine"\n', 'And still those voices are calling from far away,\n', 'Wake you up in the middle of the night\n', 'Just to hear them say...\n', 'Welcome to the Hotel California\n', 'Such a lovely place (Such a lovely place)\n', 'Such a lovely face\n', "They livin' it up at the Hotel California\n", 'What a nice surprise (what a nice surprise)\n', 'Bring your alibis\n', 'Mirrors on the ceiling,\n', 'The pink champagne on ice\n', 'And she said "We are all just prisoners here, of our own device"\n', "And in the master's chambers,\n", 'They gathered for the feast\n', 'They stab it with their steely knives,\n', "But they just can't kill the beast\n", 'Last thing I remember, I was\n', 'Running for the door\n', 'I had to find the passage back\n', 'To the place I was before\n', '"Relax, " said the night man,\n', '"We are programmed to receive.\n', 'You can check-out any time you like,\n', 'But you can never leave! "']
>>> f.close()
>>> 
>>> 
>>> 
>>> print(c)
On a dark desert highway, cool wind in my hair
Warm smell of colitas, rising up through the air
Up ahead in the distance, I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night
There she stood in the doorway;
I heard the mission bell
And I was thinking to myself,
"This could be Heaven or this could be Hell"
Then she lit up a candle and she showed me the way
There were voices down the corridor,
I thought I heard them say...
Welcome to the Hotel California
Such a lovely place (Such a lovely place)
Such a lovely face
Plenty of room at the Hotel California
Any time of year (Any time of year)
You can find it here
Her mind is Tiffany-twisted, she got the Mercedes bends
She got a lot of pretty, pretty boys she calls friends
How they dance in the courtyard, sweet summer sweat.
Some dance to remember, some dance to forget
So I called up the Captain,
"Please bring me my wine"
He said, "We haven't had that spirit here since nineteen sixty nine"
And still those voices are calling from far away,
Wake you up in the middle of the night
Just to hear them say...
Welcome to the Hotel California
Such a lovely place (Such a lovely place)
Such a lovely face
They livin' it up at the Hotel California
What a nice surprise (what a nice surprise)
Bring your alibis
Mirrors on the ceiling,
The pink champagne on ice
And she said "We are all just prisoners here, of our own device"
And in the master's chambers,
They gathered for the feast
They stab it with their steely knives,
But they just can't kill the beast
Last thing I remember, I was
Running for the door
I had to find the passage back
To the place I was before
"Relax, " said the night man,
"We are programmed to receive.
You can check-out any time you like,
But you can never leave! "
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\data2.txt", "w")
>>> f.write("HOTEL CALIFORNIA\n\n")
18
>>> f.writeline(["Eagles\n","-----------------------------------------\n"])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    f.writeline(["Eagles\n","-----------------------------------------\n"])
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeline'
>>> f.writelines(["Eagles\n","-----------------------------------------\n"])
>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\data2.txt", "a")
>>> f.write(c)
1776
>>> f.close()
>>> 
