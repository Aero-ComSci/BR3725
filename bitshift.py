a = 13
b = 46
def dingy(a, b, ans=0):
    if b == 0:  
        return ans
    if b & 1:  
        ans += a
    return dingy(a << 1, b >> 1, ans) 
ans = dingy(a, b)
print(f"{a} x {b} = {ans}")

## a <<= 1 (left shift): This doubles the value of a at each step, making it handle the next "place value" in binary multiplication
## b >>= 1 (right shift): This halves b and moves to the next bit (binary digit) to check if you should add the current value of a
## generated code from ai
