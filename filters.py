class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

students = [ Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.66), Student("Sarah", 0.88)]

failing_student = []
for student in students:
    if student.score < 0.7:
        failing_student.append(student)
print(failing_student)


filter_list = list(filter(lambda student: student.score < 0.7, students))
print(filter_list)