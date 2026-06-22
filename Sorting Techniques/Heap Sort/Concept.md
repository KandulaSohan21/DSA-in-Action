# Heap Sort

## Definition

Heap Sort is a comparison-based sorting algorithm that uses a Binary Heap data structure to sort elements efficiently.

A Heap is a special complete binary tree that satisfies the Heap Property.

For a Max Heap:

* Parent node ≥ Child nodes

For a Min Heap:

* Parent node ≤ Child nodes

Heap Sort works by:

1. Building a Max Heap.
2. Extracting the largest element.
3. Placing it in its correct position.
4. Repeating until all elements are sorted.

---

## How It Works

Given:

[40, 10, 30, 50, 20]

Step 1:

Build Max Heap

```
    50
   /  \
 40    30
/  \
```

10   20

Step 2:

Move 50 to the end.

Step 3:

Heapify remaining elements.

Step 4:

Repeat until sorted.

Final Result:

[10, 20, 30, 40, 50]

---

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n log n) |

---

## Space Complexity

O(1)

Heap Sort performs sorting in-place.

---

## Advantages

* Guaranteed O(n log n).
* No additional memory required.
* Efficient for large datasets.
* Useful for priority-based systems.

---

## Disadvantages

* Not stable.
* Slightly slower than Quick Sort in practice.

---

## When to Use Heap Sort

* Large datasets.
* Priority-based processing.
* Ranking systems.
* Scheduling applications.
