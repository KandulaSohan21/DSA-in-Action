"""
Problem Statement: Investment Growth Prediction

A financial analyst wants to estimate the growth of an
investment over several months.

For demonstration purposes, assume the projected growth
for each month follows the Fibonacci pattern, where each
month's value depends on the previous two months.

To avoid recalculating the same values repeatedly,
implement the Fibonacci Sequence using Dynamic Programming
(Tabulation).

Output:

1. Display the projected growth for each month.
2. Display the total growth at the requested month.
   """

months = 10

fib = [0] * (months + 1)

fib[0] = 0
fib[1] = 1

for i in range(2, months + 1):
fib[i] = fib[i - 1] + fib[i - 2]

print("INVESTMENT GROWTH PROJECTION\n")

for month in range(months + 1):
print(f"Month {month}: {fib[month]}")

print(f"\nEstimated Growth at Month {months}: {fib[months]}")
