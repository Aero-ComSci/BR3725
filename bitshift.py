#I could multiply two positive numbers using addition and bit-shifting by using a method based on the binary representation of numbers. 
#Essentially, the algorithm iterates through each bit of the multiplier, shifts the multiplicand, and adds the results when the corresponding bit is set.


def multiplying_two_numbers(a, b):
    result = 0
    shiftcount = 0
    while b > 0:
        if b & 1:  
            result += a << shift_count 
        a <<= 1  # Shift a left by 1 (multiply by 2)
        b >>= 1  # Shift b right by 1 (move to next bit)
        shift_count += 1
    return result

