# Circular Doubly Linked List

## Definition

A Circular Doubly Linked List is a linear data structure in which each node contains:

* Data
* A pointer to the previous node
* A pointer to the next node

Unlike a regular Doubly Linked List, the first and last nodes are connected.

* The last node points to the first node.
* The first node points back to the last node.

This creates a continuous loop while still allowing traversal in both forward and backward directions.

---

## Structure of a Node

Each node contains:

* Previous Pointer
* Data
* Next Pointer

Example:

```
         ┌──────────────────────────────┐
         │                              │
         ▼                              │
```

NULL ← A ⇄ B ⇄ C ⇄ D
▲               │
└───────────────┘

The first and last nodes are connected.

---

## How It Works

1. Every node stores references to both the previous and next nodes.
2. The last node links back to the first node.
3. The first node links back to the last node.
4. Traversal can continue forever in either direction.

---

## Basic Operations

### Insert

Add a node while maintaining both circular and doubly linked connections.

### Delete

Remove a node and reconnect its neighboring nodes.

### Forward Traversal

Move to the next node indefinitely.

### Backward Traversal

Move to the previous node indefinitely.

### Search

Locate a node by traversing either direction.

---

## Time Complexity

| Operation | Complexity               |
| --------- | ------------------------ |
| Access    | O(n)                     |
| Search    | O(n)                     |
| Insert    | O(1) (with Tail pointer) |
| Delete    | O(1) (known node)        |

---

## Space Complexity

O(n)

Each node stores two pointers.

---

## Advantages

* Bidirectional traversal.
* Continuous looping.
* Efficient insertion and deletion.
* Ideal for cyclic navigation.

---

## Disadvantages

* More memory usage.
* More complex implementation.

---

## When to Use Circular Doubly Linked Lists

* Photo gallery carousels.
* Media players.
* Game character selection.
* Dashboard widgets.
* Continuous menu systems.
