# BR3725

Left-shifting a binary number by 'n' positions is equivalent to multiplying that number by 2^n. Let a number n = ab (where ab is the binary representation of n) then if we shift ab 1 position we now have ab0 which gives us 2*b + 2*a + 0*1, which is 2*ab. Using this as the base case we can generalize n = abcde.... and each position shift results in 2 * n, and with each shift we then always multiply by 2 for each shift which gives us 2^n when we left-shift a binary number n positions. 


Then, design a function (in pseudocode or a language of your choice) that takes two positive integers as input and multiplies them using only bit-shifting and addition operations. You cannot use the standard multiplication operator (*). For example, to multiply 5 (101 in binary) by 3 (011 in binary), you'd use shifts and additions. Show your work on how your function would calculate this example."

To multiple 3 by 5 we simply do two things. First we convert 3 to binary. Left-shift 3, 1 position add 1 and then shift 1 position and add 1. This gives us 1111 which is the result of 3*5, or in base 10, 15.  
