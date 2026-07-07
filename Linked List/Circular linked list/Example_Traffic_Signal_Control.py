"""
Problem Statement: Traffic Signal Control System

A traffic signal operates continuously throughout the day.

The lights always change in the following order:

Red → Green → Yellow → Red ...

After the Yellow signal, the system automatically returns
to the Red signal and repeats the cycle.

Implement a Circular Linked List to simulate this
traffic signal control system.

Output:

1. Display the signal sequence.
2. Simulate two complete traffic signal cycles.
   """

class SignalNode:

```
def __init__(self, color):
    self.color = color
    self.next = None
```

class TrafficSignal:

```
def __init__(self):
    self.head = None
    self.tail = None

def add_signal(self, color):

    new_signal = SignalNode(color)

    if self.head is None:
        self.head = new_signal
        self.tail = new_signal
        self.tail.next = self.head
        return

    self.tail.next = new_signal
    self.tail = new_signal
    self.tail.next = self.head

def display_sequence(self):

    current = self.head

    while True:
        print(current.color)
        current = current.next

        if current == self.head:
            break

def simulate(self, cycles):

    current = self.head

    total_signals = cycles * 3

    print("\nTRAFFIC SIGNAL SIMULATION\n")

    for i in range(total_signals):
        print(f"Signal: {current.color}")
        current = current.next
```

traffic = TrafficSignal()

traffic.add_signal("Red")
traffic.add_signal("Green")
traffic.add_signal("Yellow")

print("TRAFFIC SIGNAL ORDER\n")

traffic.display_sequence()

traffic.simulate(2)
