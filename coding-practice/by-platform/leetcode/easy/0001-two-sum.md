# 1. Two Sum

- **Difficulty:** Easy
- **Topics:** #array, #hash-table
- **URL:** https://leetcode.com/problems/two-sum/


## Problem

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

<br>

**Constraints:**

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists**.
 

**Follow-up**: Can you come up with an algorithm that is less than O(n^2) time complexity?

---

### Hint 1
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions just for completeness. It is from these brute force solutions that you can come up with optimizations.

### Hint 2
So, if we fix one of the numbers, say `x`, we have to scan the entire array to find the next number y which is `value - x` where value is the input parameter. Can we change our array somehow so that this search becomes faster?

### Hint 3
The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?


## My Solutions

| # | Approach | Time | Space | Code |
|---|----------|------|-------|------|
| 1 | Brute Force (nested loops) | O(n²) | O(1) | [View](0001-two-sum.py) |
| 2 | Hash Map (check-before-add) | O(n) | O(n) | [View](0001-two-sum.py) |

---

## Key Insights

### Why Hash Map is O(n)
- Single pass through array
- Dictionary lookup/insert is O(1) average

### Why "Check Before Add" Pattern
If we build the dictionary first, we face issues:
1. Duplicate values overwrite indices (`nums=[3,3]` → `d={3:1}`)
2. Same element might match itself (`nums=[3,2,4]`, `target=6` → would return `[0,0]`)

By checking *before* adding, we only look at elements that came before — preventing self-matching while handling duplicates correctly.

