def multiply(a,b):
    #Add the code and an explanation on how to 
    #multiply a number by 2 using bitshift
    result=0
    while b>0:
        if (b&1) !=0:
            result = result+a

        a=a<<1
        b = b>>1
    return result

multiply(3,5)