
show_expected_result = False

class Student:
    scores = [65,75,85,95]    

    def average_score(self):
        total = 0
        average = 0
        for score in self.scores:
            total = total + score
        try:
            average = total / len(self.scores)
        except:
            print("Something went wrong")
        return average

student = Student()
print(student.average_score())