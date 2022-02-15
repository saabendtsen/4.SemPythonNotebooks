import Course

class DataSheet():
    def __init__(self, courses):
        self.course = courses



    def get_grades_as_list(self):
        
        grades = []

        for g in self.courses:
            grades.append(g.grade)

        return grades