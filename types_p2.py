"""Type Hinting Part 2"""


def add_numbers(x: float, y: float) -> float:
    """Receives two numbers and returns the sum"""
    return x + y


add_numbers()


# Student Class Definition
class Student:
    id: int
    name: str
    gpa: float

    def __init__(self, id: int, name: str, gpa: float):
        self.id = id
        self.name = name
        self.gpa = gpa


# Initializing Student Instances
john = Student(1, "John", 3.4)
mary = Student(2, "Mary", 3.6)

john.gpa

# List of Student Objects
students: list[Student] = []
students.append(john)
students.append(mary)
