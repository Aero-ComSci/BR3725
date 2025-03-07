def multiply(x, y):
  #bitwise left shift = multiplying number by 2 for each position it's shifted  
  result = 0
    while y > 0:
        if y & 1:
            result += x
        x <<= 1
        y >>= 1
    return result

multiply(3, 5)
