class Student:
    math_marks = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student('Raghav', 17)
student1.math_marks = 50

student2 = Student('Raghav', 17)

print(student1.name, student1.age, student1.math_marks)
print(type(student1.name), end=' ')
print(type(student1.age), end= ' ')
print(type(student1.math_marks))
print(type(student1))
print(student2.name, student2.age, student2.math_marks)

s3 = student2
Student("Jayant", 24)
