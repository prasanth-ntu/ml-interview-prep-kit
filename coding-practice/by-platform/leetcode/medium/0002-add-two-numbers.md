# 2. Add Two Numbers

- **Difficulty:** Medium
- **Topics:** #linked-list, #math, #recursion
- **URL:** https://leetcode.com/problems/add-two-numbers/


## Problem

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Visual Example:**

```
Input lists:
  l1: [2] -> [4] -> [3]        (represents 342)
  l2: [5] -> [6] -> [4]        (represents 465)

Output:
      [7] -> [0] -> [8]        (represents 807)

Explanation: 342 + 465 = 807
```

**Example 1:**

![Add Two Numbers Example 1](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998
```

<br>

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

---

### Hint 1
The digits are already in reverse order, which is actually convenient! Think about how you add numbers by hand — you start from the rightmost digit (ones place) and move left. The reverse storage means you can process nodes left-to-right while naturally handling ones → tens → hundreds.

### Hint 2
What happens when the sum of two digits exceeds 9? You need to track a **carry** value. For example: `7 + 5 = 12` means the current digit is `2` and carry is `1`.

### Hint 3
The two linked lists might have different lengths (e.g., 5-digit + 2-digit numbers). Handle this by treating missing nodes as `0`. Also remember: even after both lists are exhausted, a remaining carry creates one more digit (e.g., `999 + 1 = 1000`).

