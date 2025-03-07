def multiply(n):
    # First this appends 0 to the end of the binary sequence(bitshifting) to the number converted to binary using bin
    # then it uses the int(n,2) function to convert back to the original number
    n=(int(bin(n)+"0",2))
    print(n)
    return n
multiply(5)  # change number for different multiplication
