def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

# -----------------------------------------------

print("myprime.py -> __name__ = ", __name__)
if __name__ == "__main__":
    
    # Input
    x = int(input("Enter a number: "))

    # Output
    if(checkprime(x) == True):
        print("The entered number is prime")
    else:
        print("The number is not prime")
