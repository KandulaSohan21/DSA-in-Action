"""
Problem Statement: Browser History Navigation

A web browser keeps track of the pages visited by a user.

Each newly visited page is added to the top of the history stack.

When the user clicks the Back button, the browser removes
the most recently visited page and returns to the previous page.

Implement this functionality using a Stack.

Output:

1. Display browser history after visiting pages.
2. Simulate pressing the Back button twice.
   """

history = []

# Visiting web pages

history.append("Home Page")
history.append("YouTube")
history.append("GitHub")
history.append("LinkedIn")
history.append("ChatGPT")

print("BROWSER HISTORY\n")

for page in reversed(history):
print(page)

print("\nUser presses Back...\n")

current_page = history.pop()
print(f"Closed: {current_page}")

print("\nUser presses Back again...\n")

current_page = history.pop()
print(f"Closed: {current_page}")

print("\nCURRENT BROWSER HISTORY\n")

for page in reversed(history):
print(page)

print(f"\nCurrent Page: {history[-1]}")
