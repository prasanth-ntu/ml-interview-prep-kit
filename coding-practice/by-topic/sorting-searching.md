# Sorting & Searching

## Sorting Algorithms

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable |
|-----------|-------------|------------|--------------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

---

## Binary Search Patterns

### 1. Standard Binary Search
Find exact element

### 2. Lower/Upper Bound
Find first/last occurrence or insertion point

### 3. Search on Answer
Binary search on result space, not input

---

## Problems by Pattern

### Binary Search
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Binary Search | Easy | | |
| Search Insert Position | Easy | | |
| Find First and Last Position | Medium | | |
| Search in Rotated Sorted Array | Medium | | |

### Search on Answer
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Koko Eating Bananas | Medium | | |
| Capacity to Ship Packages | Medium | | |
| Split Array Largest Sum | Hard | | |

---

## Common Techniques

```python
# Standard binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Lower bound (first >= target)
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Upper bound (first > target)
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

# Search on answer
def search_on_answer(lo, hi):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_feasible(mid):
            hi = mid  # or lo = mid + 1, depending on problem
        else:
            lo = mid + 1  # or hi = mid - 1
    return lo
```

---

## Tips
- `left + (right - left) // 2` prevents overflow
- Pay attention to `<=` vs `<` and `+1` vs not
- For "search on answer", define `is_feasible()` clearly
