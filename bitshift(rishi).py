def multiply(a,b):
    answer=0
    while b>0:
        if b&1: 
            answer+=a
        a<<=1
        b>>=1
    return answer 

a=int(input('enter first number'))
b=int(input('enter 2nd number'))
print(multiply(a,b))

#the program multiples 2 nums by shifting the first number(a) and adding it based on the bits of the second number(b). it shifts 
#(a) to the left multiplying by 2 and shifts b to the right dividing it by 2. it adds a to the result when a bit in b is 1
