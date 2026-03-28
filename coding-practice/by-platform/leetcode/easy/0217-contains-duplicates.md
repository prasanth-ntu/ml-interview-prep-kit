# 217. Contains Duplicate

## Description

- **Difficulty:** Easy
- **Topics:** Array, Hash Table
- **URL**: https://leetcode.com/problems/contains-duplicate/


Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Examples

### Example 1:

**Input:** `nums = [1,2,3,1]`

**Output:** `true`

**Explanation:** 

The element 1 occurs at the indices 0 and 3.

### Example 2:

**Input:** `nums = [1,2,3,4]`

**Output:** `false`

**Explanation:** 

All elements are distinct.

### Example 3:

**Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`

**Output:** `true`

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Key Learnings

### Why Brute Force (List) Fails
Using a list for membership checking (`if x in my_list`) is O(n) per lookup because Python must scan the entire list. With n elements and n lookups, this gives **O(n²)** total time — too slow for 10⁵ elements.

### Why Set Works
Sets use **hash tables** internally, giving O(1) average lookup time. The `in` operator on a set computes a hash and jumps directly to the correct bucket, instead of scanning.

| Operation | List | Set |
|-----------|------|-----|
| `in` check | O(n) | O(1) |
| `.append()` / `.add()` | O(1) | O(1) |

### Python Gotcha
`{}` creates an empty **dict**, not a set! Use `set()` for an empty set.

```python
my_dict = {}      # dict
my_set = set()    # set
my_set = {1, 2}   # set with values - this works
```

## Solutions

| Approach | Time | Space | Result |
|----------|------|-------|--------|
| Brute force (list) | O(n²) | O(n) | TLE (70/77) |
| Hash set | O(n) | O(n) | ✅ Accepted |
| One-liner `len(nums) != len(set(nums))` | O(n) | O(n) | ✅ Accepted |