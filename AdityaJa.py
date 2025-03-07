import math

num1 = int(input("write a number "))
binary = int(input("write the number in binary "))
num2 = int(input("what do you want to multiply it by that is even "))
shifts = int(math.log(num2,2))
result = (num1<<num2)
print(result)
print(shifts)
