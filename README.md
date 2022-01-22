# Art-of-Computer-Programming
As I enjoy getting lost in the world of algorithms I have made a project out of working through the excellent work "The Art of Computer Programming" by Donald Knuth.

Here are my attempts some exercise solutions in form of documentation and code.

Some algorithms that I have implemented so far are 
* [Euclids Algorithm 1.1](/exercises/chapter_1/one/euclids_algorithm.py) - the highest common divisor of 2 numbers
* [Log Calculator 1.2.2](/exercises/chapter_1/two/log_calculator.py) - An approximation that uses log table constants
* [Return numbers with only ones in any base recursively 1.2.3](/exercises/chapter_1/two/only_ones.py)
* [Calculate Modulus 1.2.4](/exercises/chapter_1/two/calculate_modulus.py)
* [Get the bionomial coefficient 1.2.6](/exercises/chapter_1/two/binomial_coefficients.py)
* [Get h - the harmonic number 1.2.7](exercises/chapter_1/two/harmonic_numbers.py)
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

## 1.2.3 Sums and Product
<details>
<summary>What is the equivalent of each side of <sub>i=1</sub><sup>3</sup>𝚺 <sub>j=1</sub><sup>i</sup>𝚺a<sub>ij</sub> = <sub>j=1</sub><sup>3</sup>𝚺 <sub>i=j</sub><sup>3</sup>𝚺a<sub>ij</sub></summary>

We are dealing with a loop within a loop. However, the inner loop is either reduced or incremented by an iteration each time the outer loop iterates.  

**LHS** - <sub>i=1</sub><sup>3</sup>𝚺 <sub>j=1</sub><sup>i</sup>𝚺a<sub>ij</sub>
* i=1 j=1 11 (next j gets reset, i gets incremented)
* i=2 j=1 21
* i=2 j=2 22 (next j gets reset, i gets incremented)
* i=3 j=1 31
* i=3 j=2 32
* i=3 j=3 33 (now both loops end)  

**LHS** = a<sub>11</sub> + (a<sub>21</sub> + a<sub>22</sub>) + (a<sub>31</sub> + a<sub>32</sub> + a<sub>33</sub>)

**RHS** - <sub>j=1</sub><sup>3</sup>𝚺 <sub>i=j</sub><sup>3</sup>𝚺a<sub>ij</sub>
* i=1 j=1 11
* i=2 j=1 21
* i=3 j=1 31 (j gets incremented, i gets reset to j)
* i=2 j=2 22
* i=3 j=2 32 (j gets incremented, i gets reset to j)
* i=3 j-3 33 (now both loops end)  

**RHS** = (a<sub>11</sub> + a<sub>21</sub> + a<sub>31</sub>) + (a<sub>22</sub> + a<sub>32</sub>) + a<sub>33</sub>  

**RHS == LHS**
</details>

<details>
<summary>Write the sequence 9*1+3=11, 9*12+3=111, 9*123+4=1111, 9*1234+5=11111 in sigma notation</summary>

If we were solving this in programming then we could use string parsing. However, a mathematical solution is more elegant.  

I have taken the authors solutions here and applied them to the case of n=4.

General formulae for base 10 is 9 <sub>k=0</sub><sup>n</sup>𝚺(n-k)10<sup>k</sup> + (n+1)  
Note that the multiplication by 9 and the addition of 5 is done on the result of the sum.  

Where n=4:  
9 <sub>k=0</sub><sup>4</sup>𝚺(4-k)10<sup>k</sup> + 5  

Summation loop as follows:
* k<sub>0</sub> = (4-0)10<sup>0</sup> = 4*1 = 4
* k<sub>1</sub> = (4-1)10<sup>1</sup> = 3*10 = 30
* k<sub>2</sub> = (4-2)10<sup>2</sup> = 2*100 = 200
* k<sub>3</sub> = (4-3)10<sup>3</sup> = 1*1000 = 1000
* k<sub>4</sub> = (4-4)10<sup>3</sup> = 0*10000 = 0

Sum total: 1000 + 200 + 30 + 4 = 1234  
Multiply by 9: 1234 * 9 = 11106  
Add 5: 11106 + 5 = 11111

It works for base 2 also!
General formulae for any base is...  
(b-1)<sub>k=0</sub><sup>n</sup>𝚺(n-k)b<sup>k</sup> + (n+1)  
So for base 2 we get  
(1)<sub>k=0</sub><sup>n</sup>𝚺(n-k)2<sup>k</sup> + (n+1)  
The multiplier is not needed in this case  
<sub>k=0</sub><sup>n</sup>𝚺(n-k)2<sup>k</sup> + (n+1)

Take n = 4 in base 2  
<sub>k=0</sub><sup>n</sup>𝚺(2-k)2<sup>2</sup> + 5  
* k<sub>0</sub> = (4-0)2<sup>0</sup> = 4*1 = 4
* k<sub>1</sub> = (4-1)2<sup>1</sup> = 3*2 = 6
* k<sub>2</sub> = (4-2)2<sup>2</sup> = 2*4 = 8
* k<sub>3</sub> = (4-3)2<sup>3</sup> = 1*8 = 8
* k<sub>4</sub> = (4-4)2<sup>3</sup> = 0*16 = 0

Sum total: 4 + 6 + 8 + 8 = 26  
Multiplier is 1 so nothing to do here    
Add 5: 26 + 5 = 31  which is 32 - 1   
This gives us 100000 - 1 = 11111 in binary

However, this notation can be simplified  
(b-1)<sub>k=0</sub><sup>n</sup>𝚺(n-k)b<sup>k</sup> + (n+1) = <sub>k=0</sub><sup>n</sup>𝚺 b<sup>k</sup>  
Does the new notation work?  
Let us try n=4 in base 2.  
<sub>k=0</sub><sup>n</sup>𝚺 b<sup>k</sup> = 2<sup>0</sup> + 2<sup>1</sup> + 2<sup>2</sup> + 2<sup>3</sup> + 2<sup>4</sup> = 1 + 2 + 4 + 8 + 16 = 31  
Base 10 is also simple = 1 + 10 + 100 + 1000 + 10000 = 11111

So with this simpler notation we get the same result in both base 2 and base 10

A recursive version of this algorithm can be found [here](/exercises/chapter_1/two/only_ones.py) 
</details>

## 1.2.5 Factorials
<details>
<summary>Express 20! as a product of its prime factors</summary>

20! = <sub>k>0</sub>𝚺 floor(20 / p<sup>k</sup>) for each prime factor  
Primes up to 20 = 2, 3, 5, 7, 11, 13, 17, 19  
As the 11, 13, 17 and 19 result in 1 by this sequence then we don't need to do any futher calculations for these numbers.  
We simply need to multiply the result by 11 * 13 * 17 * 19
* 20! as 2: <sub>k>0</sub>𝚺 floor(20 / 2<sup>k</sup>)
  * floor(20/2<sup>1</sup>) + floor(20/2<sup>2</sup>) + floor(20/2<sup>3</sup>) + floor(20/2<sup>4</sup>)
  * 10 + 5 + 2 + 1
  * 2<sup>18</sup>
* 20! as 3: <sub>k>0</sub>𝚺 floor(20 / 3<sup>k</sup>)
  * floor(20/3<sup>1</sup>) + floor(20/3<sup>2</sup>)
  * 6 + 2
  * 3<sup>8</sup>
* 20! as 5: <sub>k>0</sub>𝚺 floor(20 / 5<sup>k</sup>)
  * floor(20/5<sup>1</sup>)
  * 4
  * 5<sup>4</sup>
* 20! as 7: <sub>k>0</sub>𝚺 floor(20 / 7<sup>k</sup>)
  * floor(20/7<sup>1</sup>)
  * 2
  * 7<sup>2</sup>  

#### 20! = 2<sup>18</sup> * 3<sup>8</sup> * 5<sup>4</sup> * 7<sup>2</sup> * 11 * 13 * 17 * 19
```python
import math

2**18 * 3**8 * 5**4 * 7**2 * 11 * 13 * 17 * 19 == math.factorial(20)
```
```shell
Out[3]: True
```
</details>

## 1.2.6 Binomial Coefficients
<details>
<summary>How many bridge hands are possible</summary>

This is calculated using the formulae n! / (k! * (n-k)!)

We can take each factorial expression n, k and n-k and calculate it as a product of prime factors.  
Once that has been done each exponential expression can either be multiplied or divided out.   
The final result can be seen [here](/exercises/chapter_1/two/binomial_coefficients.py)
```python
{2: 4, 5: 2, 7: 2, 17: 1, 23: 1, 41: 1, 43: 1, 47: 1}
```
2<sup>4</sup> * 5<sup>2</sup> * 7<sup>2</sup> * 17 * 23 * 41 * 43 * 47  
Resulting in **635 013 559 600**
</details>

## 1.2.8 Fibonacci Numbers
<details>
<summary>Counters Game - best move when n=1000</summary>

Rules - for 2 players
* There is a pile containing n counters. 
* The first player removes any number of counters, leaving at least one.  
* Each player must take at least one counter.
* Each player can take a maximum of 2 times the counters that the previous player took.

Let us imagine that there are 11 counters to start with.  

We shall assume that neither player wants to face certain loss.  
Therefore, their options shall be restricted to < CEIL(n/3)  

A summary of such a game make look like this:  

RC = Remaining Counters

| Turn | Player A | Options | RC  | Player B | Options | RC  |
|------|----------|---------|-----|----------|---------|-----|
| 0    | -        |         |     | -        |         | 11  |
| 1    | 3        | 1 2 3   | 8   | 1        | 1 2     | 7   |
| 2    | 2        | 1 2     | 5   | 1        | -       | 4   |
| 3    | 1        | -       | 3   | 1        | -       | 2   |
| 4    | 2        | -       | 0   |          |         |     |

This worked out pretty well for Player A. Only in their first turn did player B have any choice!  

Player B could have selected 2 counters.   
However, that would have left player A able to take a single counter from the 6 remaining, still leaving 5 counters for player B - ensuring victory!  

What if there are 15 counters? How many counters should Player A take?  
What are the max counters? max = CEIL(n/3) - 1 = 4.  
* This makes sense because if Player A took 5 counters player B would simply take 10 thus winning the game.  
* If Player A took 4 counters this would leave 11, which as we can see from our previous table allows player B certain victory.  
* What if Player A tries to always leave a fibonacci number of counters for his opponent?  
* At no time must he leave his opponent in a position to leave a fibonacci number of counters for him.  
* Options for Player A will be restricted with these rules in mind  

| Turn | Player A | Options | RC  | Player B | Options | RC  |
|------|----------|---------|-----|----------|---------|-----|
| 0    | -        |         |     | -        |         | 15  |
| 1    | 2        | -       | 13  | 4        | 1 2 3 4 | 9   |
| 2    | 1        | -       | 8   | 1        | 1 2     | 7   |
| 3    | 2        | -       | 5   | 1        | -       | 4   |
| 4    | 1        | -       | 3   | 1        | -       | 2   |
| 5    | 2        | -       | 0   |          |         |     |

Player A wins again! We note on turn 2 Player B could have chosen 2 counters.  
Player A Would then have taken 1 counter on turn 3 leaving the game in the same state.  
What about turn 1? Player B could have chosen 1, 2 or 3 instead. 
* Player B chooses 3, RC=10, Player A chooses 2. No difference.
* Player B chooses 2, RC=11, Player A chooses 3. No difference.
* Player B chooses 1, RC=12
  * Player A much choose 1. 
  * Choosing 2 would allow his opponent to leave him with a fibonacci number of counters.
  * RC=11. Now Player B can choose 1 or 2.  
  * If Player B leaves 10 counters Player A will choose 2 and leave 8.  
  * If Player B leaves 9 counters Player A will choose 1 and leave 8.
  * Either way certain victory follows for Player A.

What if there are 1000 counters. What move should Player A make?  
* max = CEIL(n/3) - 1
* n/3 = 333.33333...
* CEIL(333.333) = 334
* max = 333  

The most counters' player A can take is 333.  
* Player A must leave at least 1000 - 333 counters = 667
* The first Fibonacci number after 667 is 987.
* Player A must take **13 counters** for his first move
</details>