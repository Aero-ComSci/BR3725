def multiply(p, z): # p is the current number and z is the essentially the number being analyzed 
    # the result originally starts at 0 before any of the numbers are shifted
    final_number = 0
    # while loop is used to continue multiplication process until all bits have been acknowledged
    while z > 0:
        # checks the program to determine least significant bit of z
        if z & 1: 
            final_number += p 
        p <<= 1 # shifts p to left and multiply by 2
        z >>= 1 # shifts z to the right and divide by 2
    return final_number

# simple inputs to test the program
p = int(input("Enter the first number: "))
z = int(input("Enter the second number: "))
print(multiply(p, z))
