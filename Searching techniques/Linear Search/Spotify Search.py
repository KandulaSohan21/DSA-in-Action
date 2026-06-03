"""
Problem Statement: Spotify Song Search

You are using a music streaming platform like Spotify.

A playlist contains multiple songs in the order they were added.
The playlist is not sorted alphabetically.

A user wants to search for a song titled:

"Who Is It"

by Michael Jackson.

Since the playlist is unsorted, the system checks each song one by one until the target song is found.

Implement this search functionality using the Linear Search algorithm.

Input:

* A playlist containing song titles.
* A target song title.

Output:

* Display the position of the song in the playlist if found.
* Otherwise display "Song not found".
  """

playlist = [
"Billie Jean",
"Beat It",
"Thriller",
"Smooth Criminal",
"Black or White",
"Who Is It",
"Remember The Time",
"Bad"
]

target_song = "Who Is It"

for index in range(len(playlist)):
if playlist[index].lower() == target_song.lower():
print(f'"{target_song}" found at position {index + 1}')
break
else:
print("Song not found")
