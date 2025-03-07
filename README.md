# BR3725

Explain how left-shifting a binary number by 'n' positions is equivalent to multiplying that number by 2^n.

If you move 0001(1) by n=1 positions, then the binary code results is 00010(2) which is 1 times 2^1 . If you move 11 by n=2 positions, then the binary code results 1100(12), which is 3 times 2^2. This is mathematically correct and adding multiple zeros to the right of the binary means you are adding the powers of two with the coefficients of the zero, which is essentially just scaling the original number differently

Then, design a function (in pseudocode or a language of your choice) that takes two positive integers as input and multiplies them using only bit-shifting and addition operations. You cannot use the standard multiplication operator (*). For example, to multiply 5 (101 in binary) by 3 (011 in binary), you'd use shifts and additions. Show your work on how your function would calculate this example."
Why this question is effective:
* Conceptual Understanding: It forces students to demonstrate their understanding of the relationship between bit manipulation and arithmetic operations.
* Problem-Solving: It requires them to develop an algorithm and translate it into code (or pseudocode).
* Binary Representation: It reinforces their knowledge of binary number representation.
* Efficiency: It encourages them to think about efficient ways to perform multiplication.
* Practical Application: Bit shifting is a fundamental technique used in low-level programming and hardware design.
* Decomposition: the question naturally decomposes into two parts. First, explaining the theory, and second, applying that theory to a practical problem.
