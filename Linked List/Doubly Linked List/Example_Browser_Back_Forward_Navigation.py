"""
Problem Statement: Browser Back and Forward Navigation

A web browser stores the pages visited by a user.

Each webpage maintains references to both the previous page
and the next page.

This allows users to navigate using the Back and Forward
buttons without searching the history again.

Implement a Doubly Linked List to simulate browser navigation.

Output:

1. Display pages in forward order.
2. Display pages in backward order.
   """

class WebPage:

```
def __init__(self, page):

    self.page = page
    self.prev = None
    self.next = None
```

class BrowserHistory:

```
def __init__(self):

    self.head = None
    self.tail = None

def visit(self, page):

    new_page = WebPage(page)

    if self.head is None:
        self.head = new_page
        self.tail = new_page
        return

    self.tail.next = new_page
    new_page.prev = self.tail
    self.tail = new_page

def show_forward(self):

    current = self.head

    while current:
        print(current.page)
        current = current.next

def show_backward(self):

    current = self.tail

    while current:
        print(current.page)
        current = current.prev
```

browser = BrowserHistory()

browser.visit("Google")
browser.visit("GitHub")
browser.visit("LinkedIn")
browser.visit("ChatGPT")

print("FORWARD NAVIGATION\n")
browser.show_forward()

print("\nBACKWARD NAVIGATION\n")
browser.show_backward()
