def multiply(a,b): #function
    result = 0 #final result that will be printed later
    while b>0: #checks if b is greater than 0 which makes it positive
        if b%2==1: #checks to see if remainder of b if divided by 2 is 1, hence b is odd. Once b is 0, the multiplication has ended. 
            result += a #if previous condition met, adds a to result
        a <<= 1 #shifts left (it multiplies by 2 each iteration)
        b >>= 1 #shifts right (it divides b by 2 each iteration)
    print(result)


