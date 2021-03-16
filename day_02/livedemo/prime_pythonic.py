# Program to determine if a number is prime or not

# Input
n = int(input("Enter a number: "))

# process/output
for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
else:
    print("The entered number is prime")


# If the loop exits because of the break, statements under else will not happen
# On the contrary, if the loop exits naturally, statements under else will happen
# exactly once.
