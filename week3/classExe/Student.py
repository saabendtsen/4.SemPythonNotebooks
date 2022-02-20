import random
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

    def generateStudents(self,amount):
        names = ["Nils","Lars","Kresten","Peter","Anne","August"]
        genders = ["Male","Female","Fluid","trans"]
        students =[]
        for s in amount:
           
            students.append(Student(random.choice(names),  random.choice(genders),"URL"))
        return students
          

        


class Course():
    def __init__(self,name,classroom,teacher,ETCS,grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade
    
    def generateCourse():
        names = ["Pyton","Robot","GameDev"]
        classrooms =[195,105,50]
        teachers = ["Lars","Thomas"]
        ETCSs = [5,15,30]
        grades = [0,2,4,7,10,12]

        return Course(random.choice(names),random.choice(classrooms),random.choice(teachers),random.choice(ETCSs),random.choice(grades))




class DataSheet():
    def __init__(self, courses):
        self.courses = courses


    def get_grades_as_list(self):
        grades = []
        for g in self.courses:
            grades.append((g.name, g.grade))
        return grades

    def generateDatasheet(amount):
        list_of_courses = []
        for c in amount:
            list_of_courses.append(Course.generateCourse())

        return DataSheet(list_of_courses)

if __name__ == '__main__':

    firstCourse = Course("PYTHON",105,"Lars",15,7);
    secCourse = Course("MAAATS",105,"Lars",15,7);
    sheet = DataSheet([firstCourse,secCourse]);
    student1 = Student("Alex","Fluid","URL",sheet)
    #print(student1.datasheet.get_grades_as_list())
    #print(student1.get_avg_grade())
    print(Course.generateCourse())
