def multiply(A,B):
    result = 0
    while A:
        if A&1: result = result + B # Add shifted B if last bit of A is 1
        A >>= 1 # next bit of A
        B <<= 1 # shift B to next bit position
    return result
