# Bubble Sort

## Definition

Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.

The process continues until the entire collection is sorted.

The algorithm gets its name because larger elements gradually "bubble up" to the end of the list after each pass.

---

## How It Works

1. Compare the first two elements.
2. Swap them if they are in the wrong order.
3. Move to the next pair of adjacent elements.
4. Repeat until the end of the list.
5. Start another pass from the beginning.
6. Continue until no swaps are needed.

---

## Example

Unsorted Array:

[50, 20, 40, 10]

Pass 1:

50 ↔ 20 → [20, 50, 40, 10]

50 ↔ 40 → [20, 40, 50, 10]

50 ↔ 10 → [20, 40, 10, 50]

Pass 2:

40 ↔ 10 → [20, 10, 40, 50]

Pass 3:

20 ↔ 10 → [10, 20, 40, 50]

Sorted ✓

---

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n)       |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

### Explanation

* Best Case: The array is already sorted.
* Average Case: Multiple swaps are required.
* Worst Case: The array is sorted in reverse order.

---

## Space Complexity

O(1)

Bubble Sort sorts the collection in-place and requires no additional memory.

---

## Advantages

* Easy to understand and implement.
* No extra memory required.
* Useful for educational purposes.

---

## Disadvantages

* Inefficient for large datasets.
* Performs many unnecessary comparisons.
* Much slower than advanced sorting algorithms such as Merge Sort and Quick Sort.

---

## When to Use Bubble Sort

* Small datasets.
* Learning sorting concepts.
* Situations where simplicity is more important than performance.
