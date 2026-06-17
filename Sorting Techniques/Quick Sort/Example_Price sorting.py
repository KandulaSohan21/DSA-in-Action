
"""
Problem Statement: E-Commerce Product Price Sorting

An e-commerce platform contains thousands of products.

A customer wants to view products sorted from the lowest
price to the highest price.

To provide fast results, the platform uses Quick Sort.

Implement Quick Sort to arrange products based on price.

Output:
Display products sorted by price in ascending order.
"""

products = [
["Wireless Mouse", 799],
["Laptop", 65000],
["Keyboard", 1499],
["Monitor", 12000],
["Headphones", 2499]
]
print("Original Product List:\n",products)

def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr) // 2]

  left = [item for item in arr if item[1] < pivot[1]]
  middle = [item for item in arr if item[1] == pivot[1]]
  right = [item for item in arr if item[1] > pivot[1]]

  return quick_sort(left) + middle + quick_sort(right)


sorted_products = quick_sort(products)

print("Products Sorted by Price:\n")

for product in sorted_products:
    print(f"{product[0]} - ₹{product[1]}")
