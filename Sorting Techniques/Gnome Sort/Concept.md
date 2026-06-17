# Gnome Sort

## Definition

Gnome Sort is a simple sorting algorithm that sorts elements by repeatedly comparing neighboring elements and swapping them if they are in the wrong order.

After a swap, the algorithm moves one step backward to verify that the previous elements are still correctly ordered.

Its behavior is similar to a garden gnome arranging flower pots one by one, which is how the algorithm got its name.

---

## How It Works

1. Start from the beginning of the collection.
2. Compare the current element with the previous element.
3. If they are in the correct order, move forward.
4. If they are in the wrong order, swap them.
5. Move one step backward after a swap.
6. Continue until the end of the collection is reached.

---

## Example

Unsorted Array:

[5, 3, 2, 4]

Step 1:

[3, 5, 2, 4]

Step 2:

[3, 2, 5, 4]

Step 3:

[2, 3, 5, 4]

Step 4:

[2, 3, 4, 5]

Sorted ✓

---

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n)       |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

---

## Space Complexity

O(1)

Gnome Sort performs sorting in-place without requiring additional memory.

---

## Advantages

* Very easy to understand.
* Simple implementation.
* No extra memory required.

---

## Disadvantages

* Inefficient for large datasets.
* Performs many swaps.
* Slower than Quick Sort and Merge Sort.

---

## When to Use Gnome Sort

* Educational purposes.
* Small datasets.
* Understanding comparison-based sorting algorithms.
