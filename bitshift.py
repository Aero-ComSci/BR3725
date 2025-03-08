def multiply(a, b):
    result = 0 
    
    while b > 0:  
        if b & 1:  #This section checks if the least significant bit is 1, and if it is, it is used for the final production.
            result += a  The value of a is added to b if the least significant bit is 1
        
        a <<= 1  #A left shift on b is applied here, which is equivelant to multiplying by 2
        b >>= 1  #A right shift on b is applied here, which is equivelant to dividing b by 2

    return result #after all the bits of b have been processed, result is produced as the final amount
