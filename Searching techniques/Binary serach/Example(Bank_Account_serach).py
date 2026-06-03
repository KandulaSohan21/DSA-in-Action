"""
Problem Statement: Bank Account Search

A bank stores customer account numbers in sorted order
within its database.

A customer visits the bank and requests details for
Account Number: 1007.

Since the database contains thousands or even millions
of account records, searching each account one by one
would be inefficient.

To speed up the search process, the bank uses the
Binary Search algorithm to quickly locate the account.

Implement a Binary Search program that finds whether
the requested account number exists in the bank's records.

Input:

* A sorted list of account numbers.
* A target account number.

Output:

* Display the position of the account if found.
* Otherwise display "Account not found".
  """

account_numbers = [
1001,
1002,
1003,
1004,
1005,
1006,
1007,
1008,
1009,
1010
]

target_account = 1007

left = 0
right = len(account_numbers) - 1

while left <= right:

```
mid = (left + right) // 2

if account_numbers[mid] == target_account:
    print(f"Account {target_account} found at index {mid}")
    break

elif account_numbers[mid] < target_account:
    left = mid + 1

else:
    right = mid - 1
```

else:
print("Account not found")
