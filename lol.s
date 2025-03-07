; Store 5 in x0
mov x0, #0x5
; shift left by 1 (which is multiply by 2^1, i.e. multiply by 2)
lsl x1, x0, #0x1
; add x0 (which is 5) back to x1 to complete a multiplication of 3
add x1, x1, x0
; profit???? value is now in x1
