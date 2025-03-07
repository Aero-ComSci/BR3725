# BR3725

Explain how left-shifting a binary number by 'n' positions is equivalent to multiplying that number by 2^n. Then, design a function (in pseudocode or a language of your choice) that takes two positive integers as input and multiplies them using only bit-shifting and addition operations. You cannot use the standard multiplication operator (*). For example, to multiply 5 (101 in binary) by 3 (011 in binary), you'd use shifts and additions. Show your work on how your function would calculate this example."
Why this question is effective:
* Conceptual Understanding: It forces students to demonstrate their understanding of the relationship between bit manipulation and arithmetic operations.
* Problem-Solving: It requires them to develop an algorithm and translate it into code (or pseudocode).
* Binary Representation: It reinforces their knowledge of binary number representation.
* Efficiency: It encourages them to think about efficient ways to perform multiplication.
* Practical Application: Bit shifting is a fundamental technique used in low-level programming and hardware design.
* Decomposition: the question naturally decomposes into two parts. First, explaining the theory, and second, applying that theory to a practical problem.

**Explanation**

When you left shift a binary number by n positions, you take each bit and, by shifting it by n, you change the decimal value of that bit by 2^n.  The last n bits of the number all become 0, so the first 1 bit in the binary number is at least having a value of 2^n.  The larger the original binary number, the further the shifted value would go, and thus, by 2^n.
