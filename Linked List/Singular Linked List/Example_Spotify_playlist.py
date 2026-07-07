"""
Problem Statement: Spotify Playlist Navigation

A Spotify playlist stores songs in a sequence.

Each song is connected to the next song using a Singly Linked List.

When a song finishes playing, Spotify automatically moves to
the next linked song.

A new song is added to the end of the playlist.

Implement a Singly Linked List to represent the playlist.

Output:

1. Display the playlist before adding a new song.
2. Add a new song.
3. Display the playlist after adding the new song.
   """

class SongNode:

```
def __init__(self, title):
    self.title = title
    self.next = None
```

class Playlist:

```
def __init__(self):
    self.head = None

def add_song(self, title):

    new_song = SongNode(title)

    if self.head is None:
        self.head = new_song
        return

    current = self.head

    while current.next is not None:
        current = current.next

    current.next = new_song

def display(self):

    current = self.head

    while current is not None:
        print(current.title)
        current = current.next
```

playlist = Playlist()

playlist.add_song("Billie Jean")
playlist.add_song("Beat It")
playlist.add_song("Who Is It")
playlist.add_song("Thriller")

print("PLAYLIST BEFORE ADDING A NEW SONG\n")
playlist.display()

playlist.add_song("Smooth Criminal")

print("\nPLAYLIST AFTER ADDING A NEW SONG\n")
playlist.display()
