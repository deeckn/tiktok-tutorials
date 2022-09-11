"""Python Collections: Lists"""

# Basics
numbers = [1, 5, 9, 13]
print(f"Original list: {numbers}")

# Add element (Create)
# [1, 5, 9, 13, 15]
numbers.append(15)
print(f"Added 15: {numbers}")

# Get element (Retreive)
nine = numbers[2]
print(f"Index at 2 is {nine}")

# Update value (Update)
# [100, 5, 9, 13, 15]
numbers[0] = 100
print(f"Update number: {numbers}")

# Remove element (Delete)
# [5, 9, 13, 15]
numbers.remove(100)
print(f"Removed 100: {numbers}")

# Extend
# [5, 9, 13, 15, 70, 80, 90]
new_numbers = [70, 80, 90]
numbers.extend(new_numbers)
print(f"Extended list: {numbers}")
