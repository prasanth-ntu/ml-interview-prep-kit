# Coding Practice - Progress Tracker

## Current Focus
<!-- Update based on upcoming interviews -->
- **Target**: Update with your target companies and platforms
- **Focus Areas**: Arrays, Math/Statistics, Dynamic Programming

---

## Progress Summary

| Topic | Easy | Medium | Hard | Total |
|-------|------|--------|------|-------|
| Arrays/Strings | 4/15 | 0/20 | 0/5 | 4/40 |
| Linked Lists | 0/5 | 0/10 | 0/3 | 0/18 |
| Trees/Graphs | 0/10 | 0/15 | 0/5 | 0/30 |
| Dynamic Programming | 0/5 | 0/15 | 0/10 | 0/30 |
| Math/Statistics | 0/10 | 0/10 | 0/5 | 0/25 |
| **Total** | 4/45 | 0/70 | 0/28 | 4/143 |

---

## Study Plan Template

### Week 1: {Focus Area}
- [ ] Topic review: [Arrays Pattern](by-topic/arrays-strings.md)
- [ ] Easy: Problem 1, Problem 2
- [ ] Medium: Problem 1

### Week 2: {Focus Area}
...

---

## Quick Navigation

### By Platform
- [LeetCode](by-platform/leetcode/)
- [HackerRank](by-platform/hackerrank/)

### By Topic
- [Arrays & Strings](by-topic/arrays-strings.md)
- [Linked Lists](by-topic/linked-lists.md)
- [Trees & Graphs](by-topic/trees-graphs.md)
- [Dynamic Programming](by-topic/dynamic-programming.md)
- [Sorting & Searching](by-topic/sorting-searching.md)
- [Math & Statistics](by-topic/math-statistics.md)

### Templates
- [Problem Template](templates/problem-template.py)
- [Notes Template](templates/notes-template.md)

---

## Complexity Quick Reference

### Common Time Complexities by Pattern

| Pattern | Time Complexity | Example |
|---------|----------------|---------|
| Single loop | O(n) | Linear search |
| Nested loops (both over n) | O(n²) | Brute force pairs |
| Loop + binary search inside | O(n log n) | Search in sorted array per element |
| Sorting then iterating | O(n log n) | Sort + two pointers |
| Hash map lookup in loop | O(n) | Two Sum optimal |
| Binary search | O(log n) | Sorted array search |
| Recursion with memoization | Varies | DP problems |

### Common Space Complexities

| What You Use | Space Complexity |
|--------------|-----------------|
| Fixed variables only | O(1) |
| Hash map / dictionary | O(n) |
| 2D matrix | O(n²) or O(n×m) |
| Recursion (call stack) | O(depth) |

### Data Structure Operations (Average Case)

| Data Structure | Access | Search | Insert | Delete |
|----------------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Hash Map (dict) | O(1) | O(1) | O(1) | O(1) |
| Hash Set (set) | - | O(1) | O(1) | O(1) |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| List (array) | O(1) | O(n) | O(n)* | O(n) |

*O(1) amortized for append at end

### List vs Set/Dict for Membership (`in` operator)

| Data Structure | `in` Complexity | Why |
|----------------|-----------------|-----|
| List | O(n) | Linear scan required |
| Set | O(1) | Hash table lookup |
| Dict | O(1) | Hash table lookup |

**Common pitfall**: Using a list when you need frequent membership checks leads to O(n²) algorithms. Switch to set/dict for O(n).

### Constants in Big-O

**Rule**: O(any constant) = O(1)

| Expression | Simplifies To | Why |
|------------|---------------|-----|
| O(26) | O(1) | 26 lowercase letters — bounded, doesn't grow with n |
| O(100) | O(1) | Fixed constant |
| O(2n) | O(n) | Drop the constant multiplier |
| O(n + 26) | O(n) | Drop lower-order terms |

**Interview tip**: Always clarify input constraints! If limited to lowercase English letters, space for a frequency map is O(1). If Unicode is allowed, it becomes O(k) where k = unique characters (could approach n).

**Nuance on "large constants"**: Technically, Unicode has a finite charset (~150K characters), so O(150,000) = O(1) by definition. But in interviews, it's better to say:
> "Space is O(1) for lowercase English. For Unicode, it's technically O(1) since the charset is finite, but practically I'd describe it as O(min(n, k)) where k is the charset size — acknowledging the significant memory difference."

This shows you understand both the theory and practical implications.

---

## Resources
- [Blind 75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)
- [NeetCode 150](https://neetcode.io/practice)
- [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)
