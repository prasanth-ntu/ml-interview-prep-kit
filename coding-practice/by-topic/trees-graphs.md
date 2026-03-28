# Trees & Graphs

## Key Patterns

### Trees

#### 1. DFS (Depth-First Search)
- **Preorder**: Root -> Left -> Right (serialize, copy)
- **Inorder**: Left -> Root -> Right (BST sorted order)
- **Postorder**: Left -> Right -> Root (delete, calculate)

#### 2. BFS (Breadth-First Search)
- **When**: Level-order traversal, shortest path in unweighted
- **How**: Queue-based

#### 3. Recursion
- **When**: Most tree problems
- **Think**: What does each node need to return to parent?

### Graphs

#### 1. BFS
- **When**: Shortest path (unweighted), level exploration
- **How**: Queue + visited set

#### 2. DFS
- **When**: Path finding, cycle detection, topological sort
- **How**: Recursion or stack + visited set

#### 3. Union-Find
- **When**: Connected components, cycle detection in undirected

---

## Problems by Pattern

### Tree DFS
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Maximum Depth of Binary Tree | Easy | | |
| Validate BST | Medium | | |
| Lowest Common Ancestor | Medium | | |

### Tree BFS
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Level Order Traversal | Medium | | |
| Right Side View | Medium | | |

### Graph BFS/DFS
| Problem | Difficulty | Link | Status |
|---------|------------|------|--------|
| Number of Islands | Medium | | |
| Course Schedule | Medium | | |
| Clone Graph | Medium | | |

---

## Common Techniques

```python
# Tree DFS (recursive)
def dfs(node):
    if not node:
        return
    # preorder: process here
    dfs(node.left)
    # inorder: process here
    dfs(node.right)
    # postorder: process here

# Tree BFS (level order)
from collections import deque
queue = deque([root])
while queue:
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.popleft()
        # process node
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

# Graph BFS
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Graph DFS
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

---

## Edge Cases
- Empty tree/graph
- Single node
- Skewed tree (like linked list)
- Disconnected graph
- Self-loops, cycles
