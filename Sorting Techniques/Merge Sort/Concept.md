# Merge Sort

## Definition

Merge Sort is an efficient sorting algorithm based on the Divide and Conquer approach.

It divides a large dataset into smaller parts, sorts each part independently, and then merges them together to produce a fully sorted collection.

Merge Sort is known for its consistent performance and is widely used in applications that process large amounts of data.

---

## How It Works

1. Divide the collection into two halves.
2. Recursively divide each half until only one element remains.
3. Merge the smaller sorted collections together.
4. Continue merging until the entire collection is sorted.

---

## Example

Unsorted Array:

[38, 27, 43, 3, 9, 82, 10]

Step 1:

Divide:

[38, 27, 43]

[3, 9, 82, 10]

Step 2:

Further Divide:

[38]

[27, 43]

[3, 9]

[82, 10]

Step 3:

Merge Sorted Parts:

[27, 38, 43]

[3, 9, 10, 82]

Step 4:

Final Merge:

[3, 9, 10, 27, 38, 43, 82]

Sorted ✓

---

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n log n) |

### Explanation

Merge Sort always divides the dataset into halves and performs merging operations consistently.

---

## Space Complexity

O(n)

Additional memory is required for the merging process.

---

## Advantages

* Consistent O(n log n) performance.
* Stable sorting algorithm.
* Efficient for large datasets.
* Works well with linked lists and external sorting systems.

---

## Disadvantages

* Requires additional memory.
* More complex than Bubble Sort or Selection Sort.

---

## When to Use Merge Sort

* Large datasets.
* Stable sorting requirements.
* Data coming from multiple sources.
* External file sorting systems.
