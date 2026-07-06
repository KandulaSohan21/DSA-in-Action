"""
Problem Statement: Call Center Round Robin Assignment

A customer support center has four support agents.

Incoming customer calls are assigned to the agents one after another.

After the last agent receives a call, the next incoming call is
assigned back to the first agent, following a circular order.

Implement a Circular Queue to simulate this round-robin assignment.

Output:

1. Display the available agents.
2. Simulate assigning customer calls.
3. Show how the assignment wraps around to the first agent.
   """

from collections import deque

agents = deque([
"Agent Rahul",
"Agent Priya",
"Agent Sohan",
"Agent Sneha"
])

print("AVAILABLE SUPPORT AGENTS\n")

for agent in agents:
print(agent)

print("\nCUSTOMER CALL ASSIGNMENTS\n")

for call in range(1, 9):

```
current_agent = agents.popleft()

print(f"Customer Call {call} → {current_agent}")

agents.append(current_agent)
```

print("\nAGENTS AFTER ROUND ROBIN\n")

for agent in agents:
print(agent)
