# Linked Lists

## Key Patterns

### 1. Two Pointers (Fast & Slow)
- **When**: Cycle detection, finding middle, nth from end
- **How**: Fast moves 2x, slow moves 1x

### 2. Dummy Node
- **When**: Operations that might change head
- **How**: Create dummy pointing to head, return dummy.next

### 3. Reversal
- **When**: Reverse entire list or portion
- **How**: Track prev, curr, next pointers

### 4. Merge
- **When**: Combining sorted lists
- **How**: Compare heads, build result

---

## Problems by Pattern

### Fast & Slow Pointers
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Linked List Cycle | Easy | | |
| Middle of Linked List | Easy | | |
| Remove Nth Node From End | Medium | | |

### Reversal
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Reverse Linked List | Easy | | |
| Reverse Linked List II | Medium | | |
| Reverse Nodes in k-Group | Hard | | |

### Merge
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Merge Two Sorted Lists | Easy | | |
| Merge k Sorted Lists | Hard | | |

---

## Common Techniques

```python
# Fast & Slow (cycle detection)
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # cycle exists

# Dummy node
dummy = ListNode(0)
dummy.next = head
# ... operations
return dummy.next

# Reverse linked list
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev
```

---

## Edge Cases
- Empty list (head is None)
- Single node
- Two nodes
- Cycle at different positions
