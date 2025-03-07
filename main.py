function multiply(a, b): ##This code is written in pseudocode USED HELP FROM INTERNET
    result = 0 ## This will hold the final result
    
    while b > 0:
        if b is odd:    ##Check if the least significant bit of b is 1
            result = result + a  ## Add a to result

        a = a << 1    ## Left-shift a by 1 (a = a * 2)
        b = b >> 1   ## Right-shift b by 1 (b = b // 2)

    return result   ## Return the final result

##Explaining the code:  The operation << multiplies a number by 2. Shifting a number n by 1 bit left is equivalent to multiplying it by 2^1. The operation >> divides the number by 2 and for example, shifting the number n by 1 bit right, it is equivalent to dividing by 2^1. To determine if the current value of b is odd, we need to check if its least significant bit (the rightmost bit) is 1. This can be done using the bitwise and operation b & 1. The result being set to 0 will hold the final result. 
