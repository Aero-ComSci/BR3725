# BR3725

c. Then, design a function (in pseudocode or a language of your choice) that takes two positive integers as input and multiplies them using only bit-shifting and addition operations. You cannot use the standard multiplication operator (*). For example, to multiply 5 (101 in binary) by 3 (011 in binary), you'd use shifts and additions. Show your work on how your function would calculate this example."
Why this question is effective:
* Conceptual Understanding: It forces students to demonstrate their understanding of the relationship between bit manipulation and arithmetic operations.
* Problem-Solving: It requires them to develop an algorithm and translate it into code (or pseudocode).
* Binary Representation: It reinforces their knowledge of binary number representation.
* Efficiency: It encourages them to think about efficient ways to perform multiplication.
* Practical Application: Bit shifting is a fundamental technique used in low-level programming and hardware design.
* Decomposition: the question naturally decomposes into two parts. First, explaining the theory, and second, applying that theory to a practical problem.

Every binary number is a power of 2. 
  </br>
find the first value on the very right of the binary number, first take the number of shifts+1. if the first number is 1 take the number of shifts+1 and take it to the power of two, then store that value, then bit shift to the right once and add 1 to the number of shifts+1. if 0 bit shift to the right once and add 1 to the number of shifts+1. After getting all the numbers, add all values stored. 
