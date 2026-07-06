# Circular Queue

## Definition

A Circular Queue is a linear data structure that follows the **First In, First Out (FIFO)** principle, but with one important improvement.

Unlike a normal queue, the last position is connected back to the first position, forming a circle.

This allows the queue to reuse empty spaces created after dequeue operations, making memory utilization more efficient.

---

## Why Do We Need a Circular Queue?

Consider a queue with a fixed size of 5.

Queue:

Front

A → B → C → D → E

Rear

After removing A and B:

Empty → Empty → C → D → E

Even though there are two empty spaces at the beginning, a normal queue may not be able to use them if the rear has reached the end.

A Circular Queue solves this problem by allowing the rear pointer to wrap around to the beginning of the queue.

---

## Basic Operations

### Enqueue

Adds a new element at the rear.

If the rear reaches the last position, it wraps around to the first available position.

---

### Dequeue

Removes the element from the front.

---

### Front (Peek)

Returns the front element without removing it.

---

### Is Empty

Checks whether the queue contains any elements.

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Peek      | O(1)       |
| Is Empty  | O(1)       |

---

## Space Complexity

O(n)

where **n** is the capacity of the queue.

---

## Advantages

* Efficient memory utilization.
* No shifting of elements.
* Suitable for fixed-size buffers.
* Constant-time insertion and deletion.

---

## Disadvantages

* Fixed capacity.
* Slightly more complex implementation than a standard queue.

---

## When to Use Circular Queue

* CPU Round Robin Scheduling
* Circular Buffers
* Call Center Systems
* Streaming Applications
* Printer Spooling
* Traffic Signal Management
