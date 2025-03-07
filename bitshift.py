def multiply(a,b):
    #Add the code and an explanation on how to 
    #multiply a number by 2 using bitshift
    #doubling just like binary pattern is the only way to shift forward or back, and it is important to add what is left over especally when there is a product of an odd number
    # this requires addition and an aproximation
    result=0
    while b>0:
        if (b&1) !=0:
            result = result+a

        a=a<<1
        b = b>>1
    return result

multiply(3,5)