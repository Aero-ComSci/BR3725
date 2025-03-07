#Bell Ringer 3/7/25

#When you left-shift a binary number, multiply it by 2. Each shift to the left doubles the number. 
# To multiply two numbers using bit shifts, we look at the bits of the second number and add the 
# first number shifted by the right amount. For example, 
# to multiply 5 by 3, we shift 5 and add the results when the bits of 3 are 1.
#Attempt was not a success

def multiply(p, j):
    pranav = 0
    shift_count = 0
    while j > 0:
        if j & 1:  
            pranav += a << shift_count  
        p <<= 1   #Examples of double shifts
        j >>= 1  
        shift_count += 1
    return pranav
