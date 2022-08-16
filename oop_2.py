class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100
        
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_student = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            
        return value / len(self.students)
    

student_1 = Student('Marius', 29, 80)
student_2 = Student('Paul', 28, 90)
student_3 = Student('Melanie', 24, 100)

course_1 = Course("Physics", 2)
course_1.add_student(student_1)
course_1.add_student(student_2)
print(course_1.get_average_grade())
