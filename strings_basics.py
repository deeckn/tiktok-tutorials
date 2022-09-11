"""Python Strings: Index and Substrings"""

# Get character with index
animal = "Elephant"
index = 3
letter = animal[index]
print(letter)

# Get substring
starting_index = 5
ending_index = 7
ant = animal[starting_index: ending_index+1]
print(ant)

# Start : Stop + 1 : Step
alphabets = "abcdefghijklmnopqrstuvwxyz"
half = alphabets[0::2]
print(half)

# Negative Index
food = "hamburger"
letter = food[-1]
print(letter)

# Reverse Word
food = food[::-1]
print(food)

# Upper and lower
fruit = "apple"
fruit = fruit.upper()
print(fruit)

fruit = fruit.lower()
print(fruit)
