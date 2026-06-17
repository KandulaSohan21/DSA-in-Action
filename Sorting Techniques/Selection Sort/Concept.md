# Selection Sort

## Definition

Selection Sort is a simple sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion of a collection and places it in its correct position.

Unlike Bubble Sort, which swaps adjacent elements multiple times, Selection Sort performs fewer swaps by directly selecting the required element.

---

## How It Works

1. Find the smallest element in the unsorted portion.
2. Swap it with the first unsorted position.
3. Move the boundary of the sorted portion one step forward.
4. Repeat until the entire collection is sorted.

---

## Example

Unsorted Array:

[64, 25, 12, 22, 11]

Pass 1:

Smallest = 11

[11, 25, 12, 22, 64]

Pass 2:

Smallest = 12

[11, 12, 25, 22, 64]

Pass 3:

Smallest = 22

[11, 12, 22, 25, 64]

Sorted ✓

---

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n²)      |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

### Explanation

Selection Sort always scans the remaining unsorted portion to find the minimum element, regardless of the initial order.

---

## Space Complexity

O(1)

Selection Sort is an in-place sorting algorithm and requires no extra memory.

---

## Advantages

* Easy to understand and implement.
* Performs fewer swaps than Bubble Sort.
* Works well for small datasets.

---

## Disadvantages

* Inefficient for large datasets.
* Time complexity remains O(n²) in all cases.
* Slower than Quick Sort, Merge Sort, and Heap Sort.

---

## When to Use Selection Sort

* Small datasets.
* Educational purposes.
* Situations where minimizing swaps is important.
