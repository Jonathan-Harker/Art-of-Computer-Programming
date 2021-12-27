# Art-of-Computer-Programming
As I enjoy getting lost in the world of algorithms I have made a project out of working through the excellent work "The Art of Computer Programming" by Donald Knuth.

Here are my attempts some exercise solutions in form of documentation and code.

Some interesting algorithms that I have implemented so far are 
* [Euclids Algorithm](/exercises/chapter_1/one/euclids_algorithm.py) - the highest common divisor of 2 numbers
* [Log Calculator](/exercises/chapter_1/two/log_calculator.py) - An approximation that uses log table constants
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

## 1.2.1 Proof by Induction
<details>
<summary>Prove that the Fibonacci numbers satisfy F(n) >= ϕ<sup>n-2</sup></summary>

Where:

* ϕ = (1 + √5) / 2  
* 1 + ϕ = ϕ<sup>2</sup>   

Test:
* F<sub>(1)</sub> = 1
* F<sub>(1)</sub> >= ϕ<sup>n-2</sup> = ϕ<sup>-1</sup>
* 1 >= ϕ<sup>-1</sup>
* 1 >= 1 / ϕ
* ϕ >= 1 (Multiply by ϕ)
* (1 + √5) / 2 >= 1 (Sub real value for ϕ)
* 1 + √5 >= 2
* √5 >= 1 (Test is True)

Assert:
* F<sub>(n)</sub> >= ϕ<sup>n-2</sup>
* So F<sub>(n+1)</sub> >= ϕ<sup>n-1</sup>
* And F<sub>(n-1)</sub> >= ϕ<sup>n-3</sup>

Prove:
* F<sub>(n+1)</sub> >= F<sub>(n-1)</sub> + F<sub>(n)</sub> (The next in the sequence adds the previous 2 numbers)
* F<sub>(n+1)</sub> >= ϕ<sup>n-3</sup> + ϕ<sup>n-2</sup> (Substitute for the phi)
* ϕ<sup>n-3</sup> + ϕ<sup>n-2</sup> = ϕ<sup>n-3</sup>(1 + ϕ)
* ϕ<sup>n-3</sup>(1 + ϕ) = ϕ<sup>n-3</sup>(ϕ<sup>2</sup>) (As 1 + ϕ = ϕ<sup>2</sup>)
* ϕ<sup>n-3</sup>(ϕ<sup>2</sup>) = ϕ<sup>n-1</sup>
* ϕ<sup>n-3</sup> + ϕ<sup>n-2</sup> = ϕ<sup>n-1</sup>
* F<sub>(n+1)</sub> >= ϕ<sup>n-1</sup>
* F<sub>(n)</sub> >= ϕ<sup>n-2</sup> - **Proof is Correct**

</details>

## 1.2.2 Powers and Logarithms
<details>
<summary>What is -3<sup>-3</sup></summary>

-3<sup>-3</sup> = -1/3<sup>3</sup> = **1/27**
</details>

<details>
<summary>What is 0.125<sup>-2/3</sup></summary>

* 0.125<sup>-2/3</sup> = (1/8)<sup>-2/3</sup>
* (1/8)<sup>-2/3</sup> = <sup>3</sup>√(1/8)<sup>2</sup>
* <sup>3</sup>√(1/8)<sup>2</sup> = 1 / (1/2)<sup>2</sup>
* 1 / (1/2)<sup>2</sup> = 1 / (1/4)
* 1 / (1/4) = **4**
</details>

<details>
<summary>Will a 14 digit integer fit in a computer word with a capacity of 47 bits?</summary>

Let us assume that the 14 digit integer is going be at its max value.  
This would make the integer have a value of 99,999,999,999,999 or 9.9 * 10<sup>13</sup>  
Lets call this integer *i*   
Mathematically this question is asking is 47 >= log<sub>2</sub>(i)?  
We could ask what is the max value that a 47 bit integer will hold?  
This is simple to answer as it is 2<sup>47</sup> which is 1.4 * 10<sup>14</sup>  
The max allowed value of 1.4 * 10<sup>14</sup> is much greater than 9.9 * 10<sup>13</sup>  
Therefore **Yes the 14 digit integer will fit into a 47 bit value**
</details>