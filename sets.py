"""Python Collections: Sets"""

# Basics
evens = {2, 2, 4, 6, 8, 8}
print(f"Original Set: {evens}")

# Add element
evens.add(15)
print(f"Add 15: {evens}")

# Remove element
evens.remove(15)
print(f"Remove 15: {evens}")

# Union
odds = {1, 3, 5}
numbers = evens.union(odds)
print(f"Union: {numbers}")

# Intersection
intersect = numbers.intersection(odds)
print(f"Intersect: {intersect}")

# Difference
difference = numbers.difference(evens)
print(f"Difference: {difference}")
