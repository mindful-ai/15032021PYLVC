# Word jumble game

# -> plepas
# -> apples point++

import random

def jumble(w):
    t = list(w)
    random.shuffle(t)
    return ''.join(t)

# Show a banner
print("-" * 60)
print("\t\tWELCOME TO WORD JUMBLE GAME")
print("\tComputer shows you a jumbled word")
print("\tYou need to guess it. Maximum 10 points.")
print("-" * 60)

# Create a list

words = ["apples", "laptop", "mobile", "mirror", "pencil", "duster", "tiger", "coconut", "paper", "kitchen"]

# Randomize/shuffle the list

random.shuffle(words)

# Initialize the points

points = 0

# For ever word scanned in the list, do the following (loop)

for word in words:

    # Jumble the word

    jword = jumble(word)

    # Present to the user

    print("WORD -> ", jword)

    # Ask for user input

    uword = input(" Guess -> ")

    # Compare and update points

    if(uword == word):
        points += 1
        print("Correct Guess!")
    else:
        print("In-correct...")

# Present the results


print("-" * 60)
print("POINTS : ", points)
if(points >= 8):
    print("Excellent playing")
elif (3 < points < 8):
    print("Good!")
else:
    print("Better luck next time....")

print("Thank you!")