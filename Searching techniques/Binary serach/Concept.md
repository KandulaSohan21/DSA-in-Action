# Binary Search

## Definition

Binary Search is an efficient searching algorithm used to find an element in a sorted collection.

Instead of checking every element one by one, Binary Search repeatedly divides the search space into two halves until the target element is found.

The data must be sorted before Binary Search can be applied.

## How It Works

1. Find the middle element of the collection.
2. Compare it with the target value.
3. If they match, return the position.
4. If the target is smaller, search the left half.
5. If the target is larger, search the right half.
6. Repeat until the element is found or the search space becomes empty.

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(1)       |
| Average Case | O(log n)   |
| Worst Case   | O(log n)   |

### Explanation

Every comparison reduces the search space by half.

Example:

1000 books

After 1 comparison → 500 books

After 2 comparisons → 250 books

After 3 comparisons → 125 books

And so on...

This makes Binary Search significantly faster than Linear Search for large datasets.

## Space Complexity

Iterative Approach: O(1)

Recursive Approach: O(log n)

## Advantages

* Extremely fast for large datasets.
* Efficient searching.
* Reduces search space by half every step.

## Disadvantages

* Data must be sorted.
* Not suitable for frequently changing datasets.

## Example

Sorted Array:

[10, 20, 30, 40, 50, 60, 70]

Target:

50

Middle = 40

50 > 40 → Search Right Half

Middle = 60

50 < 60 → Search Left Half

Middle = 50 ✓ Found
