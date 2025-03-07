def multiply(n):
    result = 0
    while n > 0:
        if n & 1:
            result += n
        n <<= 1
        
    # Multiplies the given number by 2 using bit-shifting.
    # Left-shifting a binary number by one position (n << 1) moves all bits to the left which then adds a zero at the rightmost position
    #This makes it double

    
    return n
