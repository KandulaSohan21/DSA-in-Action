# Fibonacci Sequence

## Definition

The Fibonacci Sequence is a series of numbers in which each number is the sum of the two preceding numbers.

It is one of the most common introductory problems used to understand Dynamic Programming because it demonstrates how storing previously computed results can eliminate redundant calculations.

The sequence begins with:

0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Mathematically,

F(n) = F(n - 1) + F(n - 2)

where:

* F(0) = 0
* F(1) = 1

---

## Dynamic Programming Approach

Instead of calculating the same Fibonacci values repeatedly, Dynamic Programming stores previously computed values and reuses them.

This technique is called **Memoization** (Top-Down) or **Tabulation** (Bottom-Up).

---

## Example

To calculate F(6):

F(6) = F(5) + F(4)

F(5) = F(4) + F(3)

F(4) = F(3) + F(2)

Without Dynamic Programming, many values such as F(3) and F(4) are calculated multiple times.

With Dynamic Programming, each value is calculated only once and stored.

---

## Time Complexity

| Approach            | Time Complexity |
| ------------------- | --------------- |
| Recursive           | O(2ⁿ)           |
| Dynamic Programming | O(n)            |

---

## Space Complexity

| Approach    | Space Complexity |
| ----------- | ---------------- |
| Memoization | O(n)             |
| Tabulation  | O(n)             |

---

## Advantages

* Eliminates repeated calculations.
* Much faster than naive recursion.
* Introduces the concept of Dynamic Programming.

---

## Applications

* Population growth prediction
* Financial forecasting
* Algorithm optimization
* Resource planning
* Dynamic Programming fundamentals
