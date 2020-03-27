class Student:
    def __init__(self, name, math_marks, chemistry_marks):
        self.name = name
        self.math_marks = math_marks
        self.chemistry_marks = chemistry_marks
    
    def total_marks(self):
        return self.math_marks + self.chemistry_marks

    def show(self):
        print(self.name, self.total_marks())

    def correction(self):
        self.math_marks += 1
        self.chemistry_marks += 1

student_list = [Student('Rajeev', 17, 17),
                Student('Raghav', 19, 19),
                Student('Jayant', 18, 18)]

student_list[0].correction()

student_sorted_list = sorted(student_list,
                             key = lambda s: s.total_marks(),
                             reverse = True)

for s in student_sorted_list:
    s.show()
