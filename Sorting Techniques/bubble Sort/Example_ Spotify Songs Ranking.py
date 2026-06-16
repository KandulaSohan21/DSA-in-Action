"""
Problem Statement: Spotify Top Songs Ranking

Spotify wants to display the most popular songs based on
their play counts.

The songs are currently stored in an unsorted order.

To create a ranking list, the songs must be sorted from
highest plays to lowest plays.

Implement Bubble Sort to rank the songs.

Output:
Display the songs sorted by play count in descending order.
"""

songs = [
["Billie Jean", 850000],
["Who Is It", 320000],
["Thriller", 1200000],
["Beat It", 950000],
["Bad", 500000]
]

n = len(songs)

for i in range(n):
  for j in range(0, n - i - 1):
    if songs[j][1] < songs[j + 1][1]:
        songs[j], songs[j + 1] = songs[j + 1], songs[j]

print("Spotify Top Songs Ranking:\n")

for rank, song in enumerate(songs, start=1):
  print(f"{rank}. {song[0]} - {song[1]:,} plays")
