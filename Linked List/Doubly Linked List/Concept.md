# Doubly Linked List

## Definition

A Doubly Linked List is a linear data structure where each node contains:

* Data
* A pointer to the previous node
* A pointer to the next node

Unlike a Singly Linked List, a Doubly Linked List allows traversal in both forward and backward directions.

This makes it suitable for applications where users frequently move back and forth through data.

---

## Structure of a Node

Each node contains:

* Previous Pointer
* Data
* Next Pointer

Example:

NULL ← [Google] ⇄ [GitHub] ⇄ [LinkedIn] ⇄ [ChatGPT] → NULL

---

## How It Works

1. The first node is called the Head.
2. The last node is called the Tail.
3. Each node points to both its previous and next nodes.
4. Traversal is possible in both directions.

---

## Basic Operations

### Insert

Add a new node at the beginning, end, or between existing nodes.

### Delete

Remove a node while updating both previous and next pointers.

### Forward Traversal

Move from Head to Tail.

### Backward Traversal

Move from Tail to Head.

### Search

Find a node by traversing from either direction.

---

## Time Complexity

| Operation           | Complexity               |
| ------------------- | ------------------------ |
| Access              | O(n)                     |
| Search              | O(n)                     |
| Insert at Beginning | O(1)                     |
| Insert at End       | O(1) (with Tail pointer) |
| Delete a Known Node | O(1)                     |
| Delete by Value     | O(n)                     |

---

## Space Complexity

O(n)

Each node stores two pointers, so a Doubly Linked List requires more memory than a Singly Linked List.

---

## Advantages

* Forward and backward traversal.
* Faster deletion when the node is known.
* Efficient insertion at both ends.
* Ideal for navigation systems.

---

## Disadvantages

* Extra memory required for the previous pointer.
* More complex pointer management.

---

## When to Use a Doubly Linked List

* Browser navigation.
* Music players (Next/Previous).
* Image galleries.
* Undo and Redo systems.
* Text editors.
