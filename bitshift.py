function multiply(a, b):
    result = 0
    while b > 0:
        if (b AND 1) != 0:
            result = result + a
        a = a << 1
        b = b >> 1 
    return result
