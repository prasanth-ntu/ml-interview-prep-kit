# 242. Valid Anagram

## Description

- **Difficulty:** Easy
- **Topics:** Hash Table, String, Sorting
- **URL**: https://leetcode.com/problems/valid-anagram/description/

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.


**Example 1:**

Input: `s = "anagram", t = "nagaram"`

Output: `true`

**Example 2:**

Input: `s = "rat", t = "car"`

Output: `false`



**Constraints:**

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.


**Follow up**: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

## Approaches

### Approach 1: Hash Map (Two Dictionaries)
Count character frequencies in both strings using separate dictionaries, then compare.

| Complexity | Value |
|------------|-------|
| Time | O(m + n) |
| Space | O(k) where k = unique chars (max 26 for lowercase English) |

### Approach 2: Hash Map (Single Dictionary with Increment/Decrement)
Use one dictionary: increment for first string, decrement for second. If all values are 0, it's an anagram.

| Complexity | Value |
|------------|-------|
| Time | O(m + n) |
| Space | O(k) where k = unique chars |

**Optimization:** Early exit if `len(s) != len(t)`.

### Approach 3: Counter (Pythonic)
Use `collections.Counter` for cleaner code.

```python
from collections import Counter
return Counter(s) == Counter(t)
```

| Complexity | Value |
|------------|-------|
| Time | O(m + n) |
| Space | O(k) where k = unique chars |

### Approach 4: Sorting
Sort both strings and compare. Simpler but less efficient.

```python
return sorted(s) == sorted(t)
```

| Complexity | Value |
|------------|-------|
| Time | O(m log m + n log n) |
| Space | O(m + n) — always, since `sorted()` creates new lists |

---

## Comparison Summary

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash Map (two dicts) | O(m + n) | O(k) | More verbose |
| Hash Map (single dict) | O(m + n) | O(k) | Space-efficient, early exit possible |
| Counter | O(m + n) | O(k) | Most Pythonic, clean one-liner |
| Sorting | O(m log m + n log n) | O(m + n) | Simplest to understand, but slower |

**Key insight:** Counter's space is bounded by character set size (26 for lowercase English, ~150K for Unicode), while sorting *always* allocates proportional to string length.

---

## Unicode Follow-up

All hash-based approaches (1-3) naturally handle Unicode without modification. The space complexity becomes O(k) where k is the number of unique Unicode characters in the input (upper bound ~150K characters in Unicode).

The sorting approach also handles Unicode correctly, as Python's `sorted()` works with any comparable elements.