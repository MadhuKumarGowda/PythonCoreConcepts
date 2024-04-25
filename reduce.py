class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

students = [ Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.66), Student("Sarah", 0.88)]

score_total= 0
for student in students:
    score_total += student.score
print(score_total / len(students))

from functools import reduce

reduce_value = reduce(lambda total, student: student.score + total, students, 0)

print(reduce_value /  len(students))
