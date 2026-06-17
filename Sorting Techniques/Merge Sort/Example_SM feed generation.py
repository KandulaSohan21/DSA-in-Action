"""
Problem Statement: Social Media Feed Generation

A social media platform receives posts from multiple users.

To generate a user's home feed, the platform must combine
posts from different users and display them in chronological
order (latest posts first).

Since thousands of posts are created every minute, the
platform uses Merge Sort to efficiently organize posts based
on their timestamps.

Implement Merge Sort to sort social media posts from newest
to oldest.

Output:

1. Display posts before sorting.
2. Display posts after sorting.
   """

posts = [
["Rahul posted a travel photo in Instagram", "10:15"],
["Priya shared a project update in Linkedin", "09:45"],
["Sohan uploaded a LinkedIn post", "11:30"],
["Akhil posted a coding challenge in Instagram", "08:20"],
["Sneha shared a workout reel  in Instagram", "10:50"]
]

def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2

  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)

def merge(left, right):
  merged = []

  i = j = 0

  while i < len(left) and j < len(right):

      if left[i][1] > right[j][1]:
          merged.append(left[i])
          i += 1
      else:
          merged.append(right[j])
          j += 1

  merged.extend(left[i:])
  merged.extend(right[j:])

  return merged

print("SOCIAL MEDIA FEED BEFORE SORTING\n")

for post in posts:
  print(f"{post[1]}  |  {post[0]}")

sorted_posts = merge_sort(posts)

print("\nSOCIAL MEDIA FEED AFTER SORTING (LATEST FIRST)\n")

for post in sorted_posts:
  print(f"{post[1]}  |  {post[0]}")
