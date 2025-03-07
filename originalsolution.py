a = 3
b = 5 

res = [int(i) for i in list('{0:0b}'.format(a))]

c = b % 2

if c == 1: 
    d = b - 1
    for i in range(( int(d/2) )): 
        res.append('0')
        
    numA = int(''.join(map(str, res)), 2)
    
    print(numA + a)

else: 
    for i in range(( int(b/2) )): 
        res.append('0')
        
    numA = int(''.join(map(str, res)), 2)
    
    print(numA + a)
    
    
    
    


