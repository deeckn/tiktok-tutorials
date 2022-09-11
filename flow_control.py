"""
Flow Control:
If-else Statements
"""

# Basics
bool_exp = 5 > 2  # -> True

if bool_exp:
    print("5 is more than 2")
else:
    print("5 is less than 2")

# Mutiple Cases
score = 64

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
elif score >= 50:
    print("Grade E")
else:
    print("Fail!!!")


# Short-hand Version
weather = "Raining"
item = "Umbrella" if weather == "Raining" else "Nothing"
print(item)

# Equivalent Alternative
if weather == "Raining":
    item = "Umbrella"
else:
    item = "Nothing"

print(item)
