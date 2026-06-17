"""
Problem Statement: Airport Boarding Queue

An airline has assigned boarding priorities to passengers.

Due to confusion near the boarding gate, some passengers
are standing in the wrong order.

The airport staff wants to arrange passengers from
highest priority to lowest priority before boarding begins.

Implement Gnome Sort to organize the boarding queue.

Output:

1. Display the queue before sorting.
2. Display the queue after sorting.
   """

passengers = [
["Rahul", 3],
["Sneha", 5],
["Akhil", 2],
["Priya", 4],
["Sohan", 1]
]

print("BOARDING QUEUE BEFORE SORTING\n")

for passenger in passengers:
  print(f"{passenger[0]} - Priority {passenger[1]}")

index = 0
n = len(passengers)

while index < n:

  if index == 0:
      index += 1

  elif passengers[index][1] <= passengers[index - 1][1]:
      index += 1

  else:
      passengers[index], passengers[index - 1] = (
          passengers[index - 1],
          passengers[index]
      )
      index -= 1

print("\nBOARDING QUEUE AFTER SORTING\n")

for passenger in passengers:
  print(f"{passenger[0]} - Priority {passenger[1]}")
