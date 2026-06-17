# Quick Sort

## Definition

Quick Sort is a highly efficient sorting algorithm based on the Divide and Conquer technique.

It works by selecting a pivot element and partitioning the remaining elements into two groups:

* Elements smaller than the pivot.
* Elements greater than the pivot.

The same process is then applied recursively to both groups until the entire collection is sorted.

Quick Sort is one of the most widely used sorting algorithms because of its excellent average-case performance.

---

## How It Works

1. Select a pivot element.
2. Partition the array into:

   * Left side (elements smaller than pivot)
   * Right side (elements greater than pivot)
3. Recursively apply Quick Sort to both partitions.
4. Combine the results.

---

## Example

Unsorted Array:

[45, 12, 78, 23, 56]

Pivot = 56

Left:

[45, 12, 23]

Pivot:

[56]

Right:

[78]

Sort Left:

[12, 23, 45]

Final Result:

[12, 23, 45, 56, 78]

---

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n²)      |

### Explanation

* Best Case: Pivot divides the array evenly.
* Average Case: Balanced partitions most of the time.
* Worst Case: Pivot is always the smallest or largest element.

---

## Space Complexity

O(log n)

Due to recursive function calls.

---

## Advantages

* Very fast for large datasets.
* Efficient average-case performance.
* Widely used in real-world applications.

---

## Disadvantages

* Worst-case performance can degrade to O(n²).
* Recursive implementation may consume stack space.

---

## Why Quick Sort?

For large datasets containing thousands or millions of records, Quick Sort is significantly faster than Bubble Sort and Selection Sort.
