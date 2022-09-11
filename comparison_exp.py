"""Comparison Expressions"""

# Value vs Value -> Boolean

# Equality
print(f"Equality (numbers): {35 == 35}")
print(f"Equality (Strings): {'Hello' == 'Hello'}")

# More than
print(f"More than: {40 > 40}")
print(f"More than or equal to: {40 >= 40}")

# Less than
print(f"Less than: {70 < 70}")
print(f"Less than or equal to: {70 <= 70}")

# In
print(f"In List: {5 in [1, 2, 3, 4, 5]}")
print(f"In List: {9 in [1, 2, 3, 4, 5]}")


class Item:
    pass


x = Item()
y = Item()

# Is
print(x is y)
