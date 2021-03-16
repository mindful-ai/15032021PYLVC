# get 10 numbers from the user
# separate the evens and odds

# Inputs

N = []
print("Enter 10 numbers: ")
for i in range(10):
    n = int(input(" --> "))
    N.append(n)

# Process

evens = []
odds = []
for n in N:
    if(n % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)

# Output

print("-" * 50)
print("EVENS : ", evens)
print("ODDS  : ", odds)
