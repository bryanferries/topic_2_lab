class Student:
    def __init__(self, name, student_id, GPA):  ##Regular style class initializing the variables
        self.name = name
        self.grades = GPA
        self.student_id = student_id

    def __str__(self):  ##Setting up the str method for how to nicely print the objects
        return f'Student name: {self.name}, ID: {self.student_id}, Current Grade: {self.grades}'


joey = Student('Joey Bob', 'bobj25', '3.8')
bob = Student('Bob McBob', 'mcbb12', '2.2')  ##Create student objects
print(bob.name)
print(bob.student_id)  ##Printing some object attributes
print(bob.grades)
print(bob)  ##Printing the objects
print(joey)

print()
print('*********************************************************************')
print()

##DATACLASS VERSION - Much simpler, doesn't require an init or str method, or self syntax
from dataclasses import dataclass  ##Import the dataclass from dataclasses


@dataclass  ##Syntax for the dataclass
class Student:  ##Parameters come when the class is created
    name: str
    student_id: str
    gpa: float


bryan = Student('Bryan M.', 'MB513', 3.8)
ted = Student('Ted Dojonovan', 'DT882', 2.70)  ##Make student objects with name, id, and GPA data
andy = Student('Andy Drazkowskigno Jr.', 'DA123', 4.0)

print(bryan)
print(andy)  ##Print the objects, no __str__ function needed
print(ted)