def multiply(num, n):
    '''
    Left shifting is equavilant to 2^n because as you shift
    you start to multiply by 2 each number you shift.
    For example: 16 8 4 2 1 <- in this sequence the numbers
    are increasing by a multiplication factor of 2.
    '''
    shift = 2 ** n
    count = 0
    bin = []
    while(True):
      shift = shift / 2
      if shift < num:
        count += shift
        bin.append("1")
      else:
        bin.append("0")
      if count == num:
        break
    print(bin)
multiply(int(input("Type a number: ")), int(input("How many places do you want to shift it: ")))
