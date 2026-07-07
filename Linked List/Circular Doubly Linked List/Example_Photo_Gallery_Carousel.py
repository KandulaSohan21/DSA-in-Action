"""
Problem Statement: Photo Gallery Carousel

A photo gallery application displays images in a carousel.

Users can:

* Swipe right to view the next image.
* Swipe left to view the previous image.

After the last image, the gallery returns to the first image.
Likewise, moving backward from the first image displays the last image.

Implement a Circular Doubly Linked List to simulate this
photo gallery carousel.

Output:

1. Display forward navigation.
2. Display backward navigation.
   """

class Photo:

```
def __init__(self, name):
    self.name = name
    self.prev = None
    self.next = None
```

class PhotoGallery:

```
def __init__(self):
    self.head = None
    self.tail = None

def add_photo(self, name):

    new_photo = Photo(name)

    if self.head is None:
        self.head = new_photo
        self.tail = new_photo
        self.head.next = self.head
        self.head.prev = self.head
        return

    new_photo.prev = self.tail
    new_photo.next = self.head

    self.tail.next = new_photo
    self.head.prev = new_photo

    self.tail = new_photo

def show_forward(self, steps):

    print("FORWARD NAVIGATION\n")

    current = self.head

    for _ in range(steps):
        print(current.name)
        current = current.next

def show_backward(self, steps):

    print("\nBACKWARD NAVIGATION\n")

    current = self.head.prev

    for _ in range(steps):
        print(current.name)
        current = current.prev
```

gallery = PhotoGallery()

gallery.add_photo("Beach")
gallery.add_photo("Mountains")
gallery.add_photo("City")
gallery.add_photo("Forest")

gallery.show_forward(6)

gallery.show_backward(6)
