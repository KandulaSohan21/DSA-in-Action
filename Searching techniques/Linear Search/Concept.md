# Linear Search

## Definition

Linear Search is the simplest searching algorithm. It checks each element in a collection one by one until the target element is found or the entire collection has been searched.

It does not require the data to be sorted.

## How It Works

1. Start from the first element.
2. Compare it with the target value.
3. If it matches, return the position.
4. Otherwise, move to the next element.
5. Repeat until the target is found or the collection ends.

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(1)       |
| Average Case | O(n)       |
| Worst Case   | O(n)       |

### Explanation

* Best Case: The target is found at the first position.
* Average Case: The target is somewhere in the middle.
* Worst Case: The target is at the last position or does not exist.

## Space Complexity

O(1)

Linear Search uses a constant amount of extra memory regardless of the input size.

## Advantages

* Easy to implement.
* Works on sorted and unsorted data.
* No additional memory required.

## Disadvantages

* Inefficient for large datasets.
* Slower than Binary Search for sorted collections.

## Example

Array:

[12, 45, 78, 23, 90]

Target:

23

Comparisons:

12 → 45 → 78 → 23 ✓

Result: Found at index 3.
