# Art-of-Computer-Programming
Adding my attempts to the exercise solutions in form of documentation and code. 
##1.1
Adding my attempts to the exercise solutions in form of documentation and code
## 1.1
### Exercise 1
**Rearrange a, b, c, d to b, c, d, a**  
e <-- b (a, b, c, d, b)  
b <-- c (a, c, c, d, b)  
c <-- d (a, c, d, d, b)  
d <-- a (a, c, d, a, b)
a <-- e (b, c, d, a)

### Exercise 2
**Prove m is always greater than n (except first iteration)**    

**Euclids Algorithm**  
E0: If m < n, exchange m <--> n  
E1: Divide m by n and let r be the remainder  
E2:  if r = 0 return n  
E3: Set m <- n, n <- r 

**Constraints**  
* n cannot be 1 as there would be no remainder  
* m and n cannot be equal as there would be no remainder  

**Attempted Solution**  
* r = m % n  
* We set m < n and n < r  
* This equals m < n and n < m % n  
* Whatever the value of n, m must be greater than m % n  
* m > m % n  

### Exercise 3
**Avoid Trivial Replacements**  

**Attempted Solution**  
Algorithm F - this looks like recursion
* If m % n = 0 return n (Iteration 1)
* If n % (m % n) = 0 return m % n (Iteration 2)
* If (m % n) % (n % (m % n)) = 0 return n % (m % n) (Iteration 3)
* If (n % (m % n)) % ((m % n) % (n % (m % n))) = 0 return (m % n) % (n % (m % n)) (Iteration 4)  

The whole expression becomes the second arg  
The second part of the expression, after the first modulus sign, becomes the first arg  

