# Arrays & Strings

## Key Patterns

### 1. Two Pointers
- **When**: Sorted array, finding pairs, palindrome check
- **How**: Start from both ends or same direction
- **Complexity**: Usually O(n) time, O(1) space

### 2. Sliding Window
- **When**: Contiguous subarray/substring problems
- **Types**: Fixed size, variable size
- **Complexity**: Usually O(n) time

### 3. Prefix Sum
- **When**: Range sum queries, subarray sums
- **How**: Precompute cumulative sums

### 4. Hash Map
- **When**: Need O(1) lookup, counting, finding pairs
- **Trade-off**: O(n) extra space

### 5. Sorting + Binary Search
- **When**: Finding elements, range queries on sorted data

---

## Problems by Pattern

### Hash Map
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Two Sum | Easy | [Solution](../by-platform/leetcode/easy/0001-two-sum.py) | 🔄 |

### Two Pointers
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Two Sum II | Easy | [Solution](../by-platform/leetcode/easy/) | |
| 3Sum | Medium | | |
| Container With Most Water | Medium | | |

### Sliding Window
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Max Consecutive Ones | Easy | | |
| Longest Substring Without Repeating | Medium | | |
| Minimum Window Substring | Hard | | |

### Prefix Sum
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Running Sum | Easy | | |
| Subarray Sum Equals K | Medium | | |

---

## Common Techniques

```python
# Two pointers (opposite ends)
left, right = 0, len(arr) - 1
while left < right:
    # process
    left += 1
    right -= 1

# Sliding window (variable size)
left = 0
for right in range(len(arr)):
    # expand window
    while condition_violated:
        # shrink window
        left += 1
    # update result

# Prefix sum
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]
# sum(arr[i:j]) = prefix[j] - prefix[i]
```

---

## Edge Cases to Remember
- Empty array
- Single element
- All same elements
- Negative numbers
- Integer overflow
