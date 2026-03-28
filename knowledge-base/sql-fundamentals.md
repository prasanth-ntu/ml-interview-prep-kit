# SQL Fundamentals

> Quick reference for SQL interview patterns - window functions, aggregations, joins

---

## Window Functions Syntax

```sql
function_name() OVER (
    [PARTITION BY column1, column2, ...]  -- Optional: creates groups
    [ORDER BY column3 [ASC|DESC], ...]    -- Optional: ordering within partition
)
```

<!-- Note to self: This section needs to be tidied up later >
`ROW_NUMBER` and `PARTITION_BY`
- https://www.geeksforgeeks.org/sql-server/sql-server-row_number-function-with-partition-by/
- https://www.datacamp.com/tutorial/row-number-sql
- https://media.datacamp.com/legacy/image/upload/v1713890725/Marketing/Blog/SQL_Window_Functions_1_1.pdf - Cheatsheet
- https://www.datacamp.com/cheat-sheet/sql-window-functions-cheat-sheet
- My own SQL 101 notebook: https://www.datacamp.com/datalab/w/d2dad61a-bfb1-4ae0-ae21-39c206610849/edit
<!-->

## ROW_NUMBER vs RANK vs DENSE_RANK

```
Data: salaries = [100, 100, 90, 80]

ROW_NUMBER():  1, 2, 3, 4  ← Always unique, arbitrary tiebreaker
RANK():        1, 1, 3, 4  ← Ties get same rank, then SKIPS
DENSE_RANK():  1, 1, 2, 3  ← Ties get same rank, NO skip
```

| Function | Ties | Gaps | Use When |
|----------|------|------|----------|
| `ROW_NUMBER()` | Arbitrary | No | Need unique row IDs |
| `RANK()` | Same rank | Yes | Competition ranking (1st, 1st, 3rd) |
| `DENSE_RANK()` | Same rank | No | "2nd highest" type queries |

## PARTITION BY = "GROUP BY for Window Functions"

```sql
-- Rank employees BY DEPARTMENT
SELECT
    name, department, salary,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees;
```

| name | department | salary | dept_rank |
|------|------------|--------|-----------|
| Alice | Eng | 150k | 1 |
| Bob | Eng | 120k | 2 |
| Carol | Sales | 130k | 1 |  ← Resets per partition
| Dan | Sales | 110k | 2 |

## Common Window Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `ROW_NUMBER()` | Unique sequential number | Pagination, deduplication |
| `RANK()` / `DENSE_RANK()` | Ranking with ties | Top N, Nth highest |
| `LAG(col, n)` | Previous row's value | Compare to yesterday |
| `LEAD(col, n)` | Next row's value | Compare to tomorrow |
| `SUM() OVER()` | Running total | Cumulative sales |
| `AVG() OVER()` | Running average | Moving average |

## N-th Element Patterns

**Pattern 1: Nth Highest (Global)**
```sql
SELECT * FROM (
    SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM employees
) t WHERE rnk = N;
```

**Pattern 2: Nth Highest Per Group**
```sql
SELECT * FROM (
    SELECT *, DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rnk
    FROM employees
) t WHERE rnk = N;
```

**Pattern 3: Top N Per Group**
```sql
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rn
    FROM employees
) t WHERE rn <= N;
```

## Aggregation Refresher

```sql
-- Basic GROUP BY
SELECT department, COUNT(*), AVG(salary), MAX(salary)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;  -- Filter AFTER grouping
```

| Clause | Filters | When |
|--------|---------|------|
| `WHERE` | Individual rows | Before GROUP BY |
| `HAVING` | Grouped results | After GROUP BY |

## JOIN Types Quick Reference

```
LEFT JOIN:   All from left + matching from right (NULLs if no match)
RIGHT JOIN:  All from right + matching from left
INNER JOIN:  Only matching rows from both
FULL OUTER:  All from both (NULLs where no match)
```

## Execution Order (Mental Model)

```
1. FROM / JOIN    ← Tables combined
2. WHERE          ← Row filtering
3. GROUP BY       ← Aggregation groups
4. HAVING         ← Group filtering
5. SELECT         ← Columns chosen (window functions run here)
6. ORDER BY       ← Sorting
7. LIMIT/OFFSET   ← Final row limiting
```

> **Interview Tip**: Window functions execute in SELECT phase, so you can't filter on them in WHERE—use a subquery!

---

## Second Highest Salary Patterns

**One-liner**: Use `LIMIT` with `OFFSET` or `DENSE_RANK()` window function

### Pattern A: LIMIT + OFFSET (Simplest)
```sql
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

### Pattern B: Window Function (More Flexible)
```sql
SELECT salary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM employees
) ranked
WHERE rnk = 2;
```

| Approach | Handles Ties? | Handles NULL? | N-th Salary? |
|----------|---------------|---------------|--------------|
| LIMIT/OFFSET | ❌ (returns one) | Add `COALESCE` | Change OFFSET |
| DENSE_RANK | ✅ (all tied 2nd) | Add `COALESCE` | Change WHERE |

> **Interview Trap**: "What if there's no second highest?" → Return NULL with `COALESCE` or outer wrapper

### Edge Case Handler
```sql
SELECT COALESCE(
    (SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1),
    NULL
) AS second_highest;
```

---

*Last updated: 2026-01-27*
