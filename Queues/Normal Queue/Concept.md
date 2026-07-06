# Queue

## Definition

A Queue is a linear data structure that follows the **First In, First Out (FIFO)** principle.

This means the first element inserted into the queue is the first element to be removed.

Think of people waiting in a queue at a hospital or a ticket counter. The person who arrives first is served first, while new arrivals join the end of the queue.

---

## Basic Operations

### Enqueue

Adds a new element to the rear (end) of the queue.

Example:

Patient A → Patient B → Patient C

Patient D arrives

Queue:

Front

Patient A → Patient B → Patient C → Patient D

Rear

---

### Dequeue

Removes the element at the front of the queue.

After serving Patient A:

Front

Patient B → Patient C → Patient D

Rear

---

### Front (Peek)

Returns the first element without removing it.

---

### Is Empty

Checks whether the queue contains any elements.

---

## Time Complexity

| Operation    | Complexity |
| ------------ | ---------- |
| Enqueue      | O(1)       |
| Dequeue      | O(1)       |
| Front (Peek) | O(1)       |
| Is Empty     | O(1)       |

---

## Space Complexity

O(n)

where **n** is the number of elements stored in the queue.

---

## Advantages

* Fair processing order.
* Fast insertion and removal.
* Simple implementation.
* Ideal for scheduling tasks.

---

## Disadvantages

* Only the front element can be removed.
* Random access is not possible.

---

## When to Use Queue

* Hospital token systems.
* Ticket booking systems.
* Printer job scheduling.
* Customer service systems.
* CPU process scheduling.
* Breadth-First Search (BFS).
