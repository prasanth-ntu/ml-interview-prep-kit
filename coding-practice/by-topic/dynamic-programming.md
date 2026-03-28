# Dynamic Programming

## Key Patterns

### 1. 1D DP
- **When**: Single sequence, linear decisions
- **Examples**: Climbing stairs, house robber, coin change

### 2. 2D DP
- **When**: Two sequences, grid problems
- **Examples**: LCS, edit distance, unique paths

### 3. Knapsack
- **0/1 Knapsack**: Take or skip each item
- **Unbounded**: Can take item multiple times

### 4. Interval DP
- **When**: Optimal way to split/merge intervals
- **Examples**: Matrix chain multiplication, burst balloons

---

## Framework

1. **Define state**: What information do we need?
2. **Define recurrence**: How do states relate?
3. **Base cases**: Starting values
4. **Order of computation**: Bottom-up or top-down
5. **Extract answer**: Where is the final result?

---

## Problems by Pattern

### 1D DP
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Climbing Stairs | Easy | | |
| House Robber | Medium | | |
| Coin Change | Medium | | |
| Longest Increasing Subsequence | Medium | | |

### 2D DP
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Unique Paths | Medium | | |
| Longest Common Subsequence | Medium | | |
| Edit Distance | Medium | | |

### Knapsack
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Partition Equal Subset Sum | Medium | | |
| Target Sum | Medium | | |

---

## Common Techniques

```python
# 1D DP (bottom-up)
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = recurrence(dp[i-1], dp[i-2], ...)

# 1D DP (top-down with memoization)
@lru_cache(maxsize=None)
def dp(i):
    if base_case:
        return value
    return recurrence(dp(i-1), dp(i-2), ...)

# 2D DP
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = recurrence(dp[i-1][j], dp[i][j-1], ...)

# Space optimization (2D -> 1D)
prev = [0] * (m + 1)
curr = [0] * (m + 1)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        curr[j] = recurrence(prev[j], curr[j-1], ...)
    prev, curr = curr, prev
```

---

## Tips
- Start with brute force recursion
- Identify overlapping subproblems
- Add memoization (top-down)
- Convert to tabulation (bottom-up) if needed
- Optimize space if possible
