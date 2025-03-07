num1 = 0b0101  #This is 5 in decimal
num2 = 0b1000   #This is 16 in decimal
x = 0 #I made this to be a counter variable
while num2 != 0:  #This should count what the multiple of 2 is, like that 16 is 2^4 
    num2 >> 1
    x+=1 #every halving it takes to get to 0 makes it increase by 1
print(num1 << x)
