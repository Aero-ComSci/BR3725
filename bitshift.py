def multiply(a, b):
  result = 0
  if b>0:
    while True:
      if b & 1:
        result += a
        
      a << 1
      b >> 1
      
    return result
    
print(multiply(3, 5))
