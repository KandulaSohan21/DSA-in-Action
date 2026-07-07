# Singly Linked List

## Definition

A Singly Linked List is a linear data structure where each node contains:

* Data
* A pointer (reference) to the next node

Unlike arrays, nodes are not stored in contiguous memory locations. Instead, each node points to the next node, forming a chain.

Traversal is possible only in the forward direction.

---

## Structure of a Node

Each node contains two parts:

* Data
* Next Pointer

Example:

Head

[Billie Jean | • ] → [Beat It | • ] → [Who Is It | • ] → [Thriller | NULL]

---

## How It Works

1. The first node is called the Head.
2. Each node stores the address of the next node.
3. The last node points to NULL.
4. New nodes can be inserted without shifting existing nodes.

---

## Basic Operations

### Insert

Add a new node at the beginning, end, or after a specific node.

### Delete

Remove a node from the linked list.

### Traverse

Visit each node one by one from Head to NULL.

### Search

Find a node by comparing its data.

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

* Dynamic memory allocation.
* Efficient insertion and deletion.
* No shifting of elements.
* Memory is allocated only when needed.

---

## Disadvantages

* Sequential access only.
* Cannot traverse backwards.
* Extra memory is required for pointers.

---

## When to Use a Singly Linked List

* Music playlists.
* Browser history.
* Task management.
* Image slideshows.
* Dynamic memory allocation.
