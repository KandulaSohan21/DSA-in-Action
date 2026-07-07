# Linked List

## Definition

A Linked List is a linear data structure in which elements, called **nodes**, are connected using links (or pointers).

Unlike an array, the elements of a linked list are **not stored in contiguous memory locations**. Each node stores:

* Data
* A reference (pointer) to the next node

This allows efficient insertion and deletion of elements without shifting other elements in memory.

---

## Structure of a Node

Each node contains:

* Data
* Next Pointer

Example:

[Song A | • ] → [Song B | • ] → [Song C | NULL]

---

## How It Works

1. The first node is called the **Head**.
2. Each node points to the next node.
3. The last node points to **NULL**, indicating the end of the list.

---

## Types of Linked Lists

### 1. Singly Linked List

Each node contains data and a pointer to the next node.

Example:

A → B → C → NULL

* Traversal is only in one direction.
* Simple and memory-efficient.

---

### 2. Doubly Linked List

Each node contains data, a pointer to the next node, and a pointer to the previous node.

Example:

NULL ← A ⇄ B ⇄ C → NULL

* Traversal is possible in both directions.
* Requires extra memory for the previous pointer.

---

### 3. Circular Linked List

The last node points back to the first node instead of NULL.

Example:

A → B → C → A (loops back)

* No NULL pointer.
* Useful for applications requiring a continuous loop.

---

### 4. Circular Doubly Linked List

Each node has both next and previous pointers, and the last node connects back to the first.

Example:

A ⇄ B ⇄ C ⇄ A

* Combines features of both circular and doubly linked lists.
* Allows traversal in both directions in a loop.

---

## Basic Operations

### Insertion

Add a new node at the beginning, end, or middle of the list.

### Deletion

Remove a node without shifting the remaining nodes.

### Traversal

Visit each node one by one.

### Search

Find a specific node by traversing the list.

---

## Time Complexity

| Operation           | Complexity |
| ------------------- | ---------- |
| Access              | O(n)       |
| Search              | O(n)       |
| Insert at Beginning | O(1)       |
| Insert at End       | O(n)       |
| Delete at Beginning | O(1)       |
| Delete by Value     | O(n)       |

---

## Space Complexity

O(n)

where **n** is the number of nodes.

---

## Advantages

* Dynamic size.
* Efficient insertion and deletion.
* No contiguous memory required.
* Easy to expand.

---

## Disadvantages

* Sequential access only.
* Extra memory required for pointers.
* Slower searching compared to arrays.

---

## When to Use Linked Lists

* Music playlists.
* Browser navigation.
* Undo/Redo systems.
* Image viewers.
* Dynamic memory allocation.
