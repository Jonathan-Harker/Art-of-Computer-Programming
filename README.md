# Art-of-Computer-Programming
As I enjoy getting lost in the world of algorithms I have made a project out of working through the excellent work "The Art of Computer Programming" by Donald Knuth.  

Here are my attempts to the exercise solutions in form of documentation and code.  

There is not enough context to attempt all answers. For example questions about diagrams in the book.  

I will not be adding the authors answers as this is to demonstrate my understanding of the questions posed.
## 1.1 Euclids Algorithm
<details>
  <summary>Exercise 1: Rearrange Items</summary>
  
  **Rearrange a, b, c, d to b, c, d, a**  
  e <-- b (a, b, c, d, b)  
  b <-- c (a, c, c, d, b)  
  c <-- d (a, c, d, d, b)  
  d <-- a (a, c, d, a, b)
  a <-- e (b, c, d, a)
</details>  

<details>
  <summary>Exercise 2: Prove m is always greater than n</summary>
  
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
</details>

<details>
<summary>Exercise 3: Avoid trivial replacements</summary>

  **Avoid Trivial Replacements**  

  **Attempted Solution**  
  Algorithm F - this looks like recursion
  * If m % n = 0 return n (Iteration 1)
  * If n % (m % n) = 0 return m % n (Iteration 2)
  * If (m % n) % (n % (m % n)) = 0 return n % (m % n) (Iteration 3)
  * If (n % (m % n)) % ((m % n) % (n % (m % n))) = 0 return (m % n) % (n % (m % n)) (Iteration 4)  

  The whole expression becomes the second arg  
  The second part of the expression, after the first modulus sign, becomes the first arg  

  So I seem to have overcomplicated this one...
  I have created a [recursive solution]("/exercises/chapter_1/one/euclids_algorithm") based on this
</details>


<details>
<summary>Exercise 4: Find the highest common divisor of 6099 and 2166</summary>

  **Find the highest common divisor of 6099 and 2166**  
  m=6099, n=2166
  * E1: r=1767
  * E2: False
  * E3: m=2166, n=1767
  * E1: r=399
  * E2: False
  * E3: m=1767, n=399
  * E1: r=171
  * E2: False
  * E3: m=399, n=171
  * E1: r=57
  * E2: False
  * E3: m=171, n=57
  * E2: True  

**Solution: 57**
</details>

<details>
<summary>Exercise 6: What is the average number of times step E1 is performed when n=5?</summary>

m=1 -> 1  
m=2 -> 2  
m=3 -> 3  
m=4 -> 2  
m=5 -> 1  
m=6 -> 2  
m=7 -> 3  
m=8 -> 4  
m=9 -> 3  
m=10 -> 1  
m=11 -> 2  
m=12 -> 3  
m=13 -> 4  
m=14 -> 3  
m=15 -> 1  
m=16 -> 2  
m=17 -> 3  
m=18 -> 4  
m=19 -> 3  
m=20 -> 1  

Average = 48 / 20 = 2.4
Check solution using the [recursive function]("/exercises/chapter_1/one/exercise_six").  
Setting m to 1,000,000 can be run in a reasonable time with the answer of 2.599996.  
This is very close to 2.6  

**Solution: 2.6**
</details>
