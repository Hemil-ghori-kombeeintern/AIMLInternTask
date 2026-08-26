# SQL_Basics_Complete_Notes

# SQL Basics — Complete Notes

## 1. What is SQL?

**SQL (Structured Query Language)** is a language used to communicate with relational databases.

SQL is used to:
- Read data
- Insert data
- Update data
- Delete data
- Filter and sort data
- Combine data from multiple tables
- Group and analyze data

Common relational databases:
- MySQL
- PostgreSQL
- SQLite
- SQL Server
- Oracle

---

## 2. Database and Table

A **database** is a collection of related data.

A **table** stores data in rows and columns.

### `students`

| id | name | age | city | course_id |
| --- | --- | --- | --- | --- |
| 1 | Hemil | 22 | Surat | 101 |
| 2 | Rahul | 23 | Mumbai | 102 |
| 3 | Priya | 21 | Surat | 101 |
| 4 | Neha | 24 | Delhi | 103 |

### `courses`

| course_id | course_name |
| --- | --- |
| 101 | MSc IT |
| 102 | BCA |
| 103 | BTech |

---

# 3. SELECT

`SELECT` retrieves data from a table.

### All columns

```sql
SELECT * FROM students;
```

### Specific columns

```sql
SELECT name, age
FROM students;
```

### DISTINCT

Removes duplicate values.

```sql
SELECT DISTINCT city
FROM students;
```

---

# 4. WHERE

`WHERE` filters rows based on a condition.

```sql
SELECT *
FROM students
WHERE city = 'Surat';
```

Comparison operators:

```
=   Equal
<>  Not equal
!=  Not equal
>   Greater than
<   Less than
>=  Greater than or equal
<=  Less than or equal
```

### AND

```sql
SELECT *
FROM students
WHERE city = 'Surat'
AND age >= 22;
```

### OR

```sql
SELECT *
FROM students
WHERE city = 'Surat'
OR city = 'Mumbai';
```

### NOT

```sql
SELECT *
FROM students
WHERE NOT city = 'Surat';
```

### IN

```sql
SELECT *
FROM students
WHERE city IN ('Surat', 'Mumbai');
```

### BETWEEN

```sql
SELECT *
FROM students
WHERE age BETWEEN 21 AND 23;
```

### LIKE

Used for pattern matching.

```sql
SELECT *
FROM students
WHERE name LIKE 'H%';
```

```
% → Zero or more characters
_ → Exactly one character
```

### NULL

Use `IS NULL` and `IS NOT NULL`.

```sql
SELECT *
FROM students
WHERE city IS NULL;
```

```sql
SELECT *
FROM students
WHERE city IS NOT NULL;
```

---

# 5. ORDER BY

`ORDER BY` sorts query results.

### Ascending

```sql
SELECT *
FROM students
ORDER BY age ASC;
```

### Descending

```sql
SELECT *
FROM students
ORDER BY age DESC;
```

### Multiple columns

```sql
SELECT *
FROM students
ORDER BY city ASC, age DESC;
```

---

# 6. LIMIT

`LIMIT` restricts the number of returned rows.

```sql
SELECT *
FROM students
LIMIT 3;
```

Example: top 3 oldest students:

```sql
SELECT *
FROM students
ORDER BY age DESC
LIMIT 3;
```

`OFFSET` skips rows and is commonly used for pagination:

```sql
SELECT *
FROM students
LIMIT 10 OFFSET 20;
```

---

# 7. INSERT

`INSERT` adds new records.

```sql
INSERT INTO students (id, name, age, city, course_id)
VALUES (5, 'Amit', 22, 'Pune', 102);
```

Multiple rows:

```sql
INSERT INTO students (id, name, age, city, course_id)
VALUES
    (6, 'Riya', 21, 'Surat', 101),
    (7, 'Karan', 23, 'Delhi', 103);
```

---

# 8. UPDATE

`UPDATE` modifies existing records.

```sql
UPDATE students
SET age = 23
WHERE id = 1;
```

Multiple columns:

```sql
UPDATE students
SET age = 23,
    city = 'Ahmedabad'
WHERE id = 1;
```

**Important:** Always check the `WHERE` condition.

Without `WHERE`, every row can be updated:

```sql
UPDATE students
SET city = 'Surat';
```

---

# 9. DELETE

`DELETE` removes records.

```sql
DELETE FROM students
WHERE id = 5;
```

Without `WHERE`, all rows can be deleted:

```sql
DELETE FROM students;
```

---

# 10. CRUD

CRUD means:

| Operation | SQL |
| --- | --- |
| Create | `INSERT` |
| Read | `SELECT` |
| Update | `UPDATE` |
| Delete | `DELETE` |

Example:

```sql
INSERT INTO students (name, age)
VALUES ('Amit', 22);

SELECT * FROM students;

UPDATE students
SET age = 23
WHERE name = 'Amit';

DELETE FROM students
WHERE name = 'Amit';
```

---

# 11. Aggregate Functions

Aggregate functions calculate values from multiple rows.

```
COUNT() → Count rows
SUM()   → Total
AVG()   → Average
MIN()   → Minimum
MAX()   → Maximum
```

### COUNT

```sql
SELECT COUNT(*) AS total_students
FROM students;
```

### AVG

```sql
SELECT AVG(age) AS average_age
FROM students;
```

### SUM

```sql
SELECT SUM(amount) AS total_amount
FROM payments;
```

### MIN

```sql
SELECT MIN(age) AS youngest
FROM students;
```

### MAX

```sql
SELECT MAX(age) AS oldest
FROM students;
```

---

# 12. GROUP BY

`GROUP BY` groups rows having the same values.

Example:

```sql
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city;
```

Another example:

```sql
SELECT course_id, AVG(age) AS average_age
FROM students
GROUP BY course_id;
```

---

# 13. HAVING

`HAVING` filters grouped results.

```sql
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city
HAVING COUNT(*) > 1;
```

### WHERE vs HAVING

```
WHERE  → Filters rows before grouping
GROUP BY → Creates groups
HAVING → Filters groups after grouping
```

---

# 14. JOIN

A `JOIN` combines related data from multiple tables.

Example relationship:

```
students.course_id
        ↓
courses.course_id
```

---

## INNER JOIN

Returns only matching rows from both tables.

```sql
SELECT
    s.name,
    c.course_name
FROM students s
INNER JOIN courses c
    ON s.course_id = c.course_id;
```

`JOIN` by itself normally means `INNER JOIN`.

---

## LEFT JOIN

Returns all rows from the left table and matching rows from the right table.

```sql
SELECT
    s.name,
    c.course_name
FROM students s
LEFT JOIN courses c
    ON s.course_id = c.course_id;
```

Use it when you want **all students**, even if a course is missing.

---

## RIGHT JOIN

Returns all rows from the right table and matching rows from the left table.

```sql
SELECT
    s.name,
    c.course_name
FROM students s
RIGHT JOIN courses c
    ON s.course_id = c.course_id;
```

Often the same result can be written more naturally by reversing the tables and using `LEFT JOIN`.

---

## FULL OUTER JOIN

Returns all rows from both tables, matching where possible.

```sql
SELECT
    s.name,
    c.course_name
FROM students s
FULL OUTER JOIN courses c
    ON s.course_id = c.course_id;
```

> PostgreSQL supports `FULL OUTER JOIN`. MySQL does not directly support it.
> 

---

## CROSS JOIN

Returns every possible combination of rows.

```sql
SELECT
    s.name,
    c.course_name
FROM students s
CROSS JOIN courses c;
```

If there are 4 students and 3 courses:

```
4 × 3 = 12 rows
```

---

## SELF JOIN

A table joined with itself.

Example `employees`:

| id | name | manager_id |
| --- | --- | --- |
| 1 | Raj | NULL |
| 2 | Hemil | 1 |
| 3 | Priya | 1 |

```sql
SELECT
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.id;
```

---

# 15. JOIN Cheat Sheet

```
INNER JOIN
→ Only matching rows

LEFT JOIN
→ All left rows + matching right rows

RIGHT JOIN
→ All right rows + matching left rows

FULL OUTER JOIN
→ All rows from both tables

CROSS JOIN
→ Every possible combination

SELF JOIN
→ Table joined with itself
```

---

# 16. Column and Table Aliases

Aliases give temporary names.

```sql
SELECT
    name AS student_name,
    age AS student_age
FROM students;
```

Table aliases make JOIN queries shorter:

```sql
SELECT s.name, c.course_name
FROM students AS s
JOIN courses AS c
    ON s.course_id = c.course_id;
```

---

# 17. CASE

`CASE` provides conditional logic.

```sql
SELECT
    name,
    age,
    CASE
        WHEN age >= 18 THEN 'Adult'
        ELSE 'Minor'
    END AS age_group
FROM students;
```

---

# 18. COALESCE

`COALESCE` returns the first non-NULL value.

```sql
SELECT
    name,
    COALESCE(city, 'Unknown') AS city
FROM students;
```

---

# 19. Common Query Combinations

### Filter + Sort

```sql
SELECT name, age
FROM students
WHERE age >= 22
ORDER BY age DESC;
```

### Filter + Limit

```sql
SELECT *
FROM students
WHERE city = 'Surat'
LIMIT 5;
```

### Group + Aggregate

```sql
SELECT city, COUNT(*) AS total
FROM students
GROUP BY city;
```

### Group + HAVING

```sql
SELECT city, COUNT(*) AS total
FROM students
GROUP BY city
HAVING COUNT(*) >= 2;
```

### JOIN + Filter

```sql
SELECT s.name, c.course_name
FROM students s
JOIN courses c
    ON s.course_id = c.course_id
WHERE c.course_name = 'MSc IT';
```

### JOIN + GROUP BY

```sql
SELECT
    c.course_name,
    COUNT(s.id) AS total_students
FROM courses c
LEFT JOIN students s
    ON c.course_id = s.course_id
GROUP BY c.course_id, c.course_name;
```

---

# 20. SQL Execution Order

A useful logical order is:

```
FROM
JOIN
WHERE
GROUP BY
HAVING
SELECT
DISTINCT
ORDER BY
LIMIT
```

A query is normally written as:

```sql
SELECT ...
FROM ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
LIMIT ...;
```

---

# 21. Sample Database

Create tables:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100),
    course_id INT
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);
```

Insert courses:

```sql
INSERT INTO courses (course_id, course_name)
VALUES
    (101, 'MSc IT'),
    (102, 'BCA'),
    (103, 'BTech');
```

Insert students:

```sql
INSERT INTO students (id, name, age, city, course_id)
VALUES
    (1, 'Hemil', 22, 'Surat', 101),
    (2, 'Rahul', 23, 'Mumbai', 102),
    (3, 'Priya', 21, 'Surat', 101),
    (4, 'Neha', 24, 'Delhi', 103),
    (5, 'Amit', 22, 'Pune', 102);
```

---

# 22. Quick Revision

```sql
-- Read
SELECT * FROM students;

-- Filter
SELECT * FROM students
WHERE age >= 22;

-- Sort
SELECT * FROM students
ORDER BY age DESC;

-- Limit
SELECT * FROM students
LIMIT 5;

-- Insert
INSERT INTO students (name, age)
VALUES ('Amit', 22);

-- Update
UPDATE students
SET age = 23
WHERE id = 1;

-- Delete
DELETE FROM students
WHERE id = 1;

-- Join
SELECT s.name, c.course_name
FROM students s
JOIN courses c
    ON s.course_id = c.course_id;

-- Group
SELECT city, COUNT(*)
FROM students
GROUP BY city;

-- Having
SELECT city, COUNT(*) AS total
FROM students
GROUP BY city
HAVING COUNT(*) > 1;

-- Aggregate
SELECT
    COUNT(*) AS total,
    AVG(age) AS average_age,
    MIN(age) AS youngest,
    MAX(age) AS oldest
FROM students;
```