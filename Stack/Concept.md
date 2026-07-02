# Stack

## Definition

A Stack is a linear data structure that follows the **Last In, First Out (LIFO)** principle.

This means the last element added to the stack is the first one to be removed.

Think of a stack of books. You place a new book on top, and when you need a book, you remove the topmost one first.

---

## Basic Operations

### Push

Adds a new element to the top of the stack.

Example:

Push "Home"

Push "About"

Push "Contact"

Stack:

Top

Contact

About

Home

---

### Pop

Removes the top element from the stack.

After Pop:

Top

About

Home

---

### Peek

Returns the top element without removing it.

---

### Is Empty

Checks whether the stack contains any elements.

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |
| Is Empty  | O(1)       |

---

## Space Complexity

O(n)

where n is the number of elements stored.

---

## Advantages

* Fast insertion and deletion.
* Simple implementation.
* Useful for managing nested operations.

---

## Disadvantages

* Only the top element is directly accessible.
* Searching is inefficient.

---

## When to Use Stack

* Undo/Redo operations.
* Browser navigation.
* Function call management.
* Expression evaluation.
* Backtracking algorithms.
