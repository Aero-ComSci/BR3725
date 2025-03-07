def multiply_binary(num1, num2):
  product = 0
  while num2 > 0:
    if num2 & 1:
      product += num1
    num1 <<= 1   
    num2 >>= 1    
  return product

