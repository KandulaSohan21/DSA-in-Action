"""
Problem Statement: Job Portal Candidate Ranking

A job portal receives applications from multiple candidates.

Each candidate has an assessment score.

The recruiter wants to rank candidates from highest score
to lowest score before scheduling interviews.

Implement Heap Sort to create the ranking list.

Output:

1. Display candidates before sorting.
2. Display candidates after sorting.
   """

def heapify(arr, n, i):

```
largest = i
left = 2 * i + 1
right = 2 * i + 2

if left < n and arr[left][1] > arr[largest][1]:
    largest = left

if right < n and arr[right][1] > arr[largest][1]:
    largest = right

if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)
```

def heap_sort(arr):

```
n = len(arr)

for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
```

candidates = [
["Sohan", 92],
["Rahul", 85],
["Priya", 97],
["Akhil", 88],
["Sneha", 95]
]

print("CANDIDATES BEFORE SORTING\n")

for candidate in candidates:
print(f"{candidate[0]} - {candidate[1]}")

heap_sort(candidates)

print("\nCANDIDATES AFTER SORTING (HIGHEST SCORE FIRST)\n")

for candidate in reversed(candidates):
print(f"{candidate[0]} - {candidate[1]}")
