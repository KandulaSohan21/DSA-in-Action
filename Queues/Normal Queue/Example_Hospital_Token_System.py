"""
Problem Statement: Hospital Token Management System

A hospital issues token numbers to patients as they arrive.

The doctor always consults the patient who received the
earliest token first.

Implement a Queue to manage patient consultations.

Output:

1. Display the queue after patients register.
2. Simulate consulting two patients.
3. Display the remaining queue.
   """

from collections import deque

patients = deque()

# Registering patients

patients.append("Rahul")
patients.append("Priya")
patients.append("Sohan")
patients.append("Sneha")
patients.append("Akhil")

print("PATIENT QUEUE AFTER REGISTRATION\n")

for patient in patients:
print(patient)

print("\nDoctor starts consultation...\n")

served = patients.popleft()
print(f"Consulted: {served}")

served = patients.popleft()
print(f"Consulted: {served}")

print("\nREMAINING PATIENT QUEUE\n")

for patient in patients:
print(patient)

print(f"\nNext Patient: {patients[0]}")
