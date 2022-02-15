import Course
import DataSheet

class Student():
    def __init__(self,name,gender,imgUrl,datasheet):
        self.name = name
        self.gender = gender
        self.imgUrl = imgUrl
        self.datasheet = datasheet

    def get_avg_grade(self):
        grades = []
        for g in self.datasheet.courses:
            grades.append((g.grade))
  
        return sum(grades)/len(grades)
        


class Course():
    def __init__(self,name,classroom,teacher,ETCS,grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade



class DataSheet():
    def __init__(self, courses):
        self.courses = courses


    def get_grades_as_list(self):
        grades = []
        for g in self.courses:
            grades.append((g.name, g.grade))
        return grades


if __name__ == '__main__':

    firstCourse = Course("PYTHON",105,"Lars",15,7);
    secCourse = Course("MAAATS",105,"Lars",15,7);
    sheet = DataSheet([firstCourse,secCourse]);
    student1 = Student("Alex","Fluid","URL",sheet)
    #print(student1.datasheet.get_grades_as_list())
    print(student1.get_avg_grade())
