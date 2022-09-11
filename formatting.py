"""String Formatting"""

name = "Dee"
age = 20
sentence = "I'm " + name + " and I'm " + str(age) + " years old."
print(sentence)

sentence = f"I'm {name} and I'm {age} years old."
print(sentence)

# Number Formatting
value = 20.12345
print(f"Value = {value:.2f}")

# Scientic Notation
mass = 3451.1524
print(f"Mass = {mass:.1e}")

# Hexadecimal
memory = 1876543210
print(f"Memory = {memory:X}")

# Binary
number = 25
print(f"Binary = {number:b}")
