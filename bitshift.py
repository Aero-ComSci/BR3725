def multiply(a, b):
    result = 0
    while b > 0: #While loop runs while there are bits, b is the multiplier
        if b & 1: #Checks for least significant bit
            result += a #Adds value for multiplication
        a <<= 1 #Multiplies a by 2, sihfts all bits by 1 to the left
        b >>= 1 #Divides b by 2, shifts all bits by 1 to the right
    return result
    #Loop ends when b becomes 0
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(multiply(a, b))
