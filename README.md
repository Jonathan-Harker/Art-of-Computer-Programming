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
* [A game you can't win - play on the command line if you do not believe me!](applications/counters_game.py) - Based on a practical application of Fibonacci numbers
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

## 1.3.1 MIX 
<details>
<summary>Some functions explained</summary>

Some of the more complex functions are explained here in detail
<details>
<summary>CHAR</summary>

* Contents of rA is turned into a 10 byte code. 
  * Take our example of register A storing the number 10000.
  * 0 has a character code of 30
  * 1 has a character code of 31
  * rA would store 0's
    * This would equal 30 30 30 30 30
  * rX would store the string representation of 10000
    * This would equal 31 30 30 30 30
</details>

<details>
<summary>MOVE</summary>

* MOVE -1,1(1)
* MOVE x,y(z)
* x is the source memory address. The contents are copied to the memory address held in rI1
  * This is hard set to rI1 and is not changed by any of the variables x, y, z
* y is the index register and therefore must be between 1 and 6. 
  * The contents of the Index register are added to the source memory address
  * In our example y=1 which means the contents or rI1 are added to the initial memory location of -1
  * As rI1 held the address of 2 the source memory address is modified to memory location 1.
  * Therefore, the contents of 1 (0/NOP) is copied to 2
  * rI1 is then incremented by 1
* z is the number of operations or copies that are carried out
</details>

<details>
<summary>NUM</summary>

* 1000010000 is assumed to be a number in string text. 
* We may see this in modern programming languages as "1000010000"
* Each Byte in MIX can contain 6 bits allowing a maximum of 64 values
  * This allows for 0 - 63 in binary 000000 to 111111
* Each word can store 6 bytes 
  * This allows for the +/- sign and 5 bytes
    * [+][0][0][0][0][63] would simply be 63
    * [+][0][0][0][1][0] would be 64 as we have used the next byte
    * [+][0][0][1][0][0] would be 64<sup>2</sup> or 3969
    * Therefore, each byte can allow a maximum of 64<sup>i</sup> values
    * [+][64<sup>4</sup>][64<sup>4</sup>][64<sup>3</sup>][64<sup>2</sup>][64<sup>1</sup>] represent the max values depending on position
* To turn manually "1000010000" into a numeric value that MIX can understand we have to find the log base 2 of this number
* log<sub>2</sub>1000010000 = ~29.897
  * 64 = 2<sup>6</sup> and so log<sub>64</sub>1000010000 = 29.897 / 6 = ~4.98
  * If this was over 5 we would not be able to store it
    * In this case MIX stores the remainder
  * We know now all bytes are required including the first one that represents 64<sup>4</sup>
  * 1000010000 / 64<sup>4</sup> = ~59.6
  * floor(59.6) = 59
  * **The first byte is 59**
* Calculating the second byte
  * We now need the remainder
  * 1000010000 - (59 * 64<sup>4</sup>) = 10154256
  * 10154256 / 64<sup>3</sup> = ~38.74
  * floor(38.74) = 38
  * **The second byte is 38**
* Calculating the third byte
  * 10154256 - (38 * 64<sup>3</sup>) = 192784
  * 192784 / 64<sup>2</sup> = ~47.07
  * **The third byte is 47**
* Calculating the fourth byte
  * 192784 - (47 * 64<sup>2</sup>) = 272
  * 272 / 64 = 4.25
  * **The fourth byte is 4**
* Calculating the fifth byte
  * 272 - (4 * 64) = 16
  * **The fifth byte is 16**
* Register A is left with 59 38 47 4 16 after the conversion
</details>
</details>

<details>

<summary>What is the result of the "number one" program</summary>

| INSTRUCTION  | Description                                                                          | Register A      | Register X      | Register I1 | Other                 | Results Explanation                                                                                                                        | Instruction # | Execution Time |
|--------------|--------------------------------------------------------------------------------------|-----------------|-----------------|-------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------|----------------|
| ORIG 1       | Store the instructions from set location onwards                                     |                 |                 |             |                       | All instructions start from memory location 1                                                                                              |               |                |
| STZ 1        | Store the Value of 0 at location 1                                                   | +00000          | +00000          | +00         | Mem1: +00000          |                                                                                                                                            | 33            | 2              |
| ENNX 1       | Enter Negative Number Value at X                                                     |                 | -00001          |             |                       | -1 gets stored in rX                                                                                                                       | 55            | 1              |
| STX 1(0:1)   | Store the rhs digits and +/- sign X at Memory location 1 lhs                         |                 |                 |             | Mem1: -100000         |                                                                                                                                            | 31            | 2              |
| SLAX 1       | Shift Left Including A & X                                                           |                 | -00010          |             |                       | No change to A as all zeros, Register X gets shifted                                                                                       | 06            | 2              |
| ENNA 1       | Enter Negative Value into A                                                          | -00001          |                 |             |                       | Register A is loaded with -00001                                                                                                           | 48            | 1              |
| INCX 1       | Increases Register X by the Value of 1                                               |                 | -0 0 0 0 63     |             |                       | Register X is increased by 1 causing -10(-64 in base 10) to be increased by 1. The value of -63 is now stored.                             | 55            | 1              | 
| ENT1 1       | Enter Value into the register                                                        |                 |                 | +01         |                       | Register I1 is set to +01                                                                                                                  | 49            | 1              |
| SRC 1        | Shift Right Circularly by given amount                                               | -63 0 0 0 0     | -1 0 0 0 0      |             |                       | Reg A is set to -10000 and Reg X is set to +10000                                                                                          | 06            | 2              |
| ADD 1        | Add The Memory location of 1 to Register A                                           | -0 0 0 0 0      |                 |             | Overflow is set to on | -63 - 1 would require 7 bits to store as the number would now be -1 0 0 0 0 0 0. This causes an overflow with remainder 0.                 | 01            | 2              |
| DEC1 -1      | Decrease Register X by the value of -1                                               |                 |                 | +02         |                       | A decrease of minus 1 is an increase of 1 so rI1 is set to +02                                                                             | 49            | 1              |
| STZ 1        | Store the Value of 0 at location 1                                                   |                 |                 |             | Mem1: +00000          | Mem 1 gets set to zero                                                                                                                     | 33            | 2              |
| CMPA 1       | Register A is compared to the memory                                                 |                 |                 |             | Comparison: EQUAL     | Register A contains +00000 and Memory 1 contains 00000                                                                                     | 56            | 2              |
| MOVE -1,1(1) | Copy data from specified memory location to location set in rI1 - then increment rI1 |                 |                 | +03         | Mem2: +00000          | This copies the data from memory address 1 to mem address 2. 3 is stored in rI1 and -1 is the parameter so the target memory address is 2. | 07            | 3              |
| NUM 1        | Convert the contents of Register A and X to Numeric values to be stored in A         | -00 00 02 28 16 |                 |             |                       | +00000 10000 is converted to a number. 10,000 -> encoded num.                                                                              | 05            | 10             |
| CHAR 1       | Convert the contents of Register A to a 10 byte code, thus using Registers A & X     | -30 30 30 30 30 | -31 30 30 30 30 |             |                       | Contents of Register A is turned into a 10 byte decimal number that fills both rA and rX                                                   | 05            | 10             |

End state:
* Register A: -30 30 30 30 30
* Register X: -31 30 30 30 30
* Register I1: +03
* Mem1: +00000
* Mem2: +00000
* Comparison: EQUAL
* Overflow is set to ON

If the starting cell is 0 then there will be some discrepancies:
* The sign on rI1 will be - not +
* The overflow toggle will be set to off
* The comparison indicator will be set to EQUAL not LESS
  * This is because the ADD 1 instruction will add zero as the contents of memory 1 will be zero.
<details>
<summary>Only the program</summary>

* ORIG 1
* STZ 1         
* ENNX 1       
* STX 1(0:1)   
* SLAX 1       
* ENNA 1       
* INCX 1        
* ENT1 1       
* SRC 1        
* ADD 1        
* DEC1 -1      
* STZ 1        
* CMPA 1       
* MOVE -1,1(1) 
* NUM 1        
* CHAR 1  
* HLT 1
</details>
</details>


<details>
<summary>Store I4 into J</summary>

As long as the number is greater than 0 and less than 3001.  
Example n=2041
* Setup
  * INC4 2041 
  * JMP 3000 
  * ORIG 3000 
* Copy r4 into rJ
  * LDX 3003 
  * STX -1,4 
  * JMP -1,4 
  * JMP 3004 
* End
  * HLT

Explanation of the program

| Instruction | Changes                | Description                                                                                 | Current Cell |
|-------------|------------------------|---------------------------------------------------------------------------------------------|--------------|
| INC4 2041   | r4 <-- +31 57          | The numerical representation of 2041 is stored in r4                                        | 0            |
| JMP 3000    | rJ <-- +0 2            | Jump to cell 3000, Register J stores the next location if it had not been interrupted, 2    | 1            |
| ORIG 3000   |                        | All instructions from here are set to memory 3000 onwards                                   | N/A          |
| LDX 3003    | rX <-- +46 60 0 0 39   | Register X stores the instruction to JMP to 3004 from cell 3003                             | 3000         |
| STX -1,4    | 2040 <-- +46 60 0 0 39 | Cell 2040 (-1 + the contents of r4) now store the instruction to Jump to cell 3004          | 3001         |
| JMP -1,4    | rJ <-- +46 59          | Jump to cell 2040, Register J stores the next location if it had not been interrupted, 3003 | 3002         |
| JMP 3004    | rJ <-- +31 57          | Jump to cell 3004, Register J stored the next location if it had not been interrupted, 2041 | 2040         |
| HLT         |                        | End of routine                                                                              | 3004         |

</details>

<details>
<summary>Compute x<sup>13</sup></summary>

Result is held in register A  
x is held in mem 2000  
For example x = 4

Setup
* INCA 4
* STA 2000
* SUB 2000

ALGO
* ADD 2000
* INC1 50
* MOVE 10(1)
* DEC1 41
* MOVE 8(22) *5 to the power of (2 plux x/2) where x is in ()
* MUL 2000
* SLAX 5

END
* HLT
</details>