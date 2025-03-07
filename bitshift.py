# In binary, each digit represents a power of 2. Left-shifting a number by n positions appends n zeros to its binary representation. For example, 5 (binary 101) shifted left by 1 becomes 1010 (10 in decimal), equivalent to 5 × 2¹ = 10

def multiply(n):
    def multiply(a, b):
    result = 0
    while b > 0:
        if b & 1:  # Check if least significant bit = 1
            result += a
        a = a << 1  # Multiply a by 2
        b = b >> 1  # Divide b by 2 
    return result
    return n

