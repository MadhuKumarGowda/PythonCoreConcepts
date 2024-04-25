class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [ Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.66), Student("Sarah", 0.88)]

student_results = []
for student in students:
    student_results.append(f"{student.name} Passed") if student.score >= 0.7 else student_results.append(f"{student.name} Failed")

print(student_results)

map_results = list(map(lambda student: student.name,students))
map_result1 = list(map(lambda student: f"{student.name} Passed" if student.score >= 0.7 else f"{student.name} Failed",students))
print(map_results)
print(map_result1)