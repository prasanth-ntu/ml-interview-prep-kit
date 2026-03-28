# Math & Statistics

## Key Topics for DS/ML Interviews

### Probability
- Bayes' theorem
- Conditional probability
- Expected value
- Variance, standard deviation

### Statistics
- Mean, median, mode
- Percentiles, quartiles
- Hypothesis testing (p-value, significance)
- A/B testing

### Linear Algebra
- Matrix operations
- Eigenvalues, eigenvectors
- Dot product, cosine similarity

---

## Common Coding Patterns

### 1. Math Properties
- GCD/LCM
- Prime numbers
- Modular arithmetic

### 2. Bit Manipulation
- AND, OR, XOR
- Bit shifting
- Count set bits

### 3. Combinatorics
- Permutations, combinations
- Pascal's triangle

---

## Problems

### Math
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Fizz Buzz | Easy | | |
| Power of Two | Easy | | |
| Count Primes | Medium | | |
| Pow(x, n) | Medium | | |

### Bit Manipulation
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Single Number | Easy | | |
| Number of 1 Bits | Easy | | |
| Reverse Bits | Easy | | |

### Probability/Statistics
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Random Pick with Weight | Medium | | |
| Shuffle an Array | Medium | | |

---

## Common Techniques

```python
# GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# LCM
def lcm(a, b):
    return a * b // gcd(a, b)

# Check if power of 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Count set bits
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
# Or: bin(n).count('1')

# Fast exponentiation
def power(x, n):
    if n < 0:
        x, n = 1/x, -n
    result = 1
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result

# Sieve of Eratosthenes
def count_primes(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return sum(is_prime)
```

---

## Interview Questions (Conceptual)

### Probability
- What's the probability of getting at least one 6 in 4 dice rolls?
- Explain Bayes' theorem with an example
- How would you simulate a fair coin with a biased one?

### Statistics
- Difference between Type I and Type II errors?
- When would you use median over mean?
- How do you calculate sample size for A/B test?
