# 🐍 Python Data Structures

## 📖 Overview

This repository contains my learning and practice of Python's core data structures. I learned not only the syntax but also **when to use each data structure**, their advantages, limitations, and built mini projects to apply them in real-world scenarios.

## 📚 Topics Covered

- Lists
- Tuples
- Sets
- Dictionaries

---

# 📌 1. List

## What is a List?

A **List** is an ordered, mutable collection that can store multiple values of different data types.

```python
students = ["Usman", "Ali", "Ahmed"]
```

### Features

- ✅ Ordered
- ✅ Mutable (can be modified)
- ✅ Allows duplicate values
- ✅ Supports indexing and slicing

### Common Methods

- `append()`
- `insert()`
- `remove()`
- `pop()`
- `clear()`
- `sort()`
- `reverse()`
- `len()`

### Use Cases

- Shopping Cart
- Student Names
- Todo List
- Chat Messages
- Product List

### Avoid Using List When

- Only unique values are required.
- Data should never change.
- Fast membership checking is the highest priority.

---

# 📌 2. Tuple

## What is a Tuple?

A **Tuple** is an ordered, immutable collection.

```python
coordinates = (31.5204, 74.3587)
```

### Features

- ✅ Ordered
- ❌ Immutable
- ✅ Allows duplicates
- ✅ Supports indexing

### Use Cases

- GPS Coordinates
- RGB Colors
- Days of the Week
- Months of the Year
- Fixed Configuration Data

### Avoid Using Tuple When

- Data needs frequent modification.
- Adding or removing elements is required.

---

# 📌 3. Set

## What is a Set?

A **Set** is an unordered collection of unique values.

```python
roll_numbers = {101, 102, 103}
```

### Features

- ❌ Unordered
- ✅ Mutable
- ❌ Does not allow duplicates
- ❌ No indexing

### Common Methods

- `add()`
- `remove()`
- `discard()`
- `pop()`
- `union()`
- `intersection()`
- `difference()`

### Use Cases

- Student Roll Numbers
- CNIC Numbers
- Flight Numbers
- Email IDs
- Tags
- Unique Categories

### Avoid Using Set When

- Element order matters.
- Index-based access is needed.

---

# 📌 4. Dictionary

## What is a Dictionary?

A **Dictionary** stores information using **Key : Value** pairs.

```python
student = {
    "name": "Usman",
    "age": 21,
    "cgpa": 3.20
}
```

### Features

- ✅ Mutable
- ✅ Keys are unique
- ✅ Fast key-based access
- ✅ Stores structured data

### Common Methods

- `get()`
- `keys()`
- `values()`
- `items()`
- `pop()`
- `update()`
- `del`

### Use Cases

- Student Records
- User Profiles
- Product Information
- Employee Records
- API Responses (JSON)

### Avoid Using Dictionary When

- Only sequential data is needed.
- Key-value mapping is unnecessary.

---

# 📊 Comparison Table

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| Ordered | ✅ | ✅ | ❌ | ✅ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Allows Duplicates | ✅ | ✅ | ❌ | Keys ❌ / Values ✅ |
| Supports Indexing | ✅ | ✅ | ❌ | Access by Key |
| Key-Value Mapping | ❌ | ❌ | ❌ | ✅ |

---

# 🎯 Which One Should I Use?

| Situation | Recommended Data Structure |
|-----------|----------------------------|
| Shopping Cart | List |
| Student Names | List |
| GPS Coordinates | Tuple |
| RGB Color | Tuple |
| Student Roll Numbers | Set |
| CNIC Numbers | Set |
| Email IDs | Set |
| Student Record | Dictionary |
| User Profile | Dictionary |
| Product Details | Dictionary |

---

# 🚀 Mini Projects Completed

## 📁 Student Management System (List)

Features:

- Add Student
- Display Students
- Search Student
- Remove Student
- Sort Students
- Reverse List
- Count Students

---

## 📁 Student Record Management System (Dictionary)

Features:

- Add Student
- Display All Students
- Search Student
- Update Student CGPA
- Delete Student
- Count Students
- Refactored using Functions

---

# 💡 Key Takeaways

- Learned the difference between mutable and immutable data structures.
- Understood when to use Lists, Tuples, Sets, and Dictionaries.
- Practiced indexing, slicing, looping, searching, updating, and deleting data.
- Built two CRUD-based mini projects.
- Refactored code using functions to improve modularity and readability.

---

# 📝 Summary

- **List** → Use when data changes and order matters.
- **Tuple** → Use when data should remain constant.
- **Set** → Use when only unique values are required.
- **Dictionary** → Use when data should be accessed using meaningful keys.

---
