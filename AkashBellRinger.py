# Left-shifting a binary number by 'n' positions multiplies the number by 2^n, as each shift increases the value of each bit by a power of 2.

function multiply(a, b):
    result=0
    while b>0:
      if (b & 1) == 1
        result = result + a #Adds a to the result if the current bit of b is 1
      a = a << 1 # Left shift a by 1 (which multiplies a by 2 due to the power of 2 increasing by 1)
      b = b >> 1 # Right shift b by 1 (which divides b by 2 due to the power of 2 decreasing by 1)
