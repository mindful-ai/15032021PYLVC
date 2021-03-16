# Get "some" numbers from the user and separate the primes


import myprime
print("extractprimes.py -> __name__ = ", __name__)

# Inputs

N = []
while True:

    n = input(" --> ")
    if(n == "q"):
        break
    elif(n.isdigit()):
        N.append(int(n))

print(N)

# process

primes = []
for n in N:
    if(myprime.checkprime(n)):
        primes.append(n)

# Output

print("-" * 50)
print("PRIMES : ", primes)
