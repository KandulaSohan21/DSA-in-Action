# Insertion Sort

## Definition

Insertion Sort is a sorting algorithm that builds a sorted collection one element at a time.

It works similarly to how people arrange playing cards in their hands. Each new card is inserted into its correct position among the already sorted cards.

The algorithm maintains two portions:

* Sorted portion
* Unsorted portion

During each iteration, an element from the unsorted portion is picked and inserted into its correct position within the sorted portion.

---

## How It Works

1. Assume the first element is already sorted.
2. Pick the next element.
3. Compare it with elements in the sorted portion.
4. Shift larger elements one position to the right.
5. Insert the current element in its correct position.
6. Repeat until all elements are sorted.

---

## Example

Unsorted Array:

[8, 3, 5, 4]

Pass 1:

[3, 8, 5, 4]

Pass 2:

[3, 5, 8, 4]

Pass 3:

[3, 4, 5, 8]

Sorted ✓

---

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n)       |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

### Explanation

Best Case:
Array is already sorted.

Worst Case:
Array is sorted in reverse order.

---

## Space Complexity

O(1)

Insertion Sort sorts the data in-place without requiring additional memory.

---

## Advantages

* Easy to implement.
* Efficient for small datasets.
* Performs well on nearly sorted data.
* Stable sorting algorithm.

---

## Disadvantages

* Inefficient for large datasets.
* Slower than Merge Sort and Quick Sort.

---

## When to Use Insertion Sort

* Small datasets.
* Nearly sorted collections.
* Real-time insertion of new records.
