"""Logical Operators"""

# AND OR NOT

running = True
hungry = False
thirsty = True

print(f"Running && Hungry: {running and hungry}")
print(f"Running && Thirsty: {running and thirsty}")
print(f"Hungry || Thirsty: {hungry or thirsty}")
print(f"Not Thirsty: {not thirsty}")
print(f"Not Hungry: {not hungry}")

# With Comparison Operators
good_eye = True
age = 27

can_drive = good_eye and age >= 18
print(f"Can Drive: {can_drive}")
