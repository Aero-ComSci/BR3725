def multiply(a, b):
    n = 0
    while b > 0:
        if b & 1:
            n = n + a
        a = a << 1
        b = b >> 1
    return n

n = multiply(6, 9)
print(n)  
