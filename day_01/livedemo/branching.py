# PRogram to subtract two numbers and print the sign of the resultant

# INput
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Process

res = a - b

# OUtput

print("--------------------------------")

print("DIFFERENCE: ", abs(a - b))

if(res < 0):
    print("The difference is negative")
elif (res > 0):
    print("The difference is positive")
    if(5 < res < 25): # res > 5 and res < 25
        print("Result between 5 and 25")
else:
    print("The difference is zero")

print("Thank you!")

    
    

