# Input some text from the user
# List the vowels in the text and it count

# Input:
# apples
# OUtput:
# a --> 1
# e --> 1
# i --> 0
# o --> 0
# u --> 0

text = input("Enter some text: ")
for c in "aeiou":
    print(c, ' --> ', text.count(c))

    
'''
>>> text = "mary had a little lamb"
>>> { v:text.count(v) for v in 'aeiou' }
'''
