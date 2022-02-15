class Course():
    def __init__(self,name,classroom,teacher,ETCS,grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade


if __name__ == '__main__':
    firstCourse = Course("",105,"Lars",15,7);
    print(firstCourse.grade)