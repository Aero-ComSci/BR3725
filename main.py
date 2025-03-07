@@ -0,0 +1,8 @@
def multiply(a, b):
    result = 0 #Add the code and an explanation on how to 
    while b > 0:
        if b is odd:
            result = result + a  #multiply a number by 2 using bitshift
            b = b >> 1  
        a = a << 1
    return result
