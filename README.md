# Art-of-Computer-Programming
Adding my attempts to the exercise solutions in form of documentation and code
##1.1
### Exercise 1
**Rearrange a, b, c, d to b, c, d, a**  
e <-- b (a, b, c, d, b)  
b <-- c (a, c, c, d, b)  
c <-- d (a, c, d, d, b)  
d <-- a (a, c, d, a, b)
a <-- e (b, c, d, a)