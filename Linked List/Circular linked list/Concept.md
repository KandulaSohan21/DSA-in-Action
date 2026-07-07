# Circular Linked List

## Definition

A Circular Linked List is a variation of a Linked List in which the last node points back to the first node (Head) instead of pointing to NULL.

This creates a continuous loop, allowing traversal to continue indefinitely without reaching an end.

Circular Linked Lists are useful in applications where data needs to be processed repeatedly in a cyclic manner.

---

## Structure of a Circular Linked List

Unlike a Singly Linked List:

Head

A → B → C → D

↑             ↓

└─────────────┘

The last node points back to the Head.

---

## How It Works

1. The first node is called the Head.
2. Every node points to the next node.
3. The last node points back to the Head.
4. Traversal continues in a loop until a stopping condition is met.

---

## Basic Operations

### Insert

Add a new node while maintaining the circular connection.

### Delete

Remove a node and reconnect the remaining nodes.

### Traverse

Visit nodes until returning to the Head.

### Search

Search by traversing around the circle.

---

## Time Complexity

| Operation           | Complexity               |
| ------------------- | ------------------------ |
| Access              | O(n)                     |
| Search              | O(n)                     |
| Insert at Beginning | O(1) (with Tail pointer) |
| Insert at End       | O(1) (with Tail pointer) |
| Delete              | O(n)                     |

---

## Space Complexity

O(n)

where **n** is the number of nodes.

---

## Advantages

* Continuous traversal.
* Efficient cyclic processing.
* No NULL pointer at the end.
* Ideal for round-robin systems.

---

## Disadvantages

* Traversal must stop explicitly to avoid infinite loops.
* More complex than a Singly Linked List.

---

## When to Use Circular Linked Lists

* Music playlist repeat mode.
* Multiplayer turn-based games.
* CPU Round Robin Scheduling.
* Circular task scheduling.
* Traffic signal control systems.
