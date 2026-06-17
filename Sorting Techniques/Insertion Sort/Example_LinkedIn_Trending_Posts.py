"""
Problem Statement: LinkedIn Trending Posts

LinkedIn ranks posts based on engagement scores
(likes, comments, shares).

As new posts gain engagement, they need to be placed
in the correct position among already ranked posts.

Implement Insertion Sort to arrange posts from
highest engagement score to lowest engagement score.

Output:

1. Display posts before sorting.
2. Display posts after sorting.
   """

posts = [
["AI Project Showcase", 450],
["Data Science Roadmap", 1200],
["Internship Experience", 800],
["Machine Learning Tips", 600],
["Career Guidance", 950]
]

print("LINKEDIN POSTS BEFORE SORTING\n")

for post in posts:
  print(f"{post[0]} - {post[1]} engagements")

for i in range(1, len(posts)):

  current_post = posts[i]
  current_score = posts[i][1]

  j = i - 1

  while j >= 0 and posts[j][1] < current_score:
      posts[j + 1] = posts[j]
      j -= 1

  posts[j + 1] = current_post

print("\nLINKEDIN POSTS AFTER SORTING (TRENDING ORDER)\n")

for post in posts:
  print(f"{post[0]} - {post[1]} engagements")
