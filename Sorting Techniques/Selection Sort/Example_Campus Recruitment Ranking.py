
"""
Problem Statement: Campus Recruitment Ranking

A company visits a university campus for placements.

Candidates have completed an aptitude test and received scores.

The recruitment team wants to create a merit list from
highest score to lowest score.

To do this, the system repeatedly selects the candidate
with the highest score from the remaining candidates and
places them in the next rank.

Implement this ranking process using Selection Sort.

Output:
Display candidates sorted by score in descending order.
"""

candidates = [
["Sohan", 92],
["Rahul", 85],
["Priya", 97],
["Akhil", 88],
["Sneha", 95]
]
print(f"Campus Recruitment Merit List(Before Sorting):\n {candidates}\n")
n = len(candidates)

for i in range(n):

  max_index = i

  for j in range(i + 1, n):

      if candidates[j][1] > candidates[max_index][1]:
          max_index = j

  candidates[i], candidates[max_index] = (
      candidates[max_index],
      candidates[i]
  )

print("Campus Recruitment Merit List(After Sorting):\n")

for rank, candidate in enumerate(candidates, start=1):
  print(f"Rank {rank}: {candidate[0]} - {candidate[1]} marks")
