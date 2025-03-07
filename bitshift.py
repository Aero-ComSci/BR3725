def multiply(n):
    #Add the code and an explanation on how to 
    #multiply a number by 2 using bitshift
    ## Get the number
    ## convert it to a binary
    ## By shifting the 0s and ones you can multiply numbers. For example 4 100 --> 1000 8. Notice how the number got multiplied by two
#1) create a list and number
#2) divide a number by two to turn it into binary
#3) append to list 
#4) add a zero to the end of the list to mulitply by 2
    
    
    n = 7  
    list = []
    res = ""
while n > 0:
    res = str(n % 2) + res
    n //= 2
    list.append(res)

print(list)
list.append(0)

     
    return n

