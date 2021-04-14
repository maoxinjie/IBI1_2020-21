class Student(object):
    def __init__(self, name, code_portfolio,  poster_resentation, final_exam):
        self.name = name
        self.code_portfolio = code_portfolio * 0.4
        self.poster_resentation = poster_resentation * 0.3
        self.final_exam = final_exam * 0.3
    def grade(self):
        return (self.name, (self.code_portfolio + self.poster_resentation + self.final_exam))

name = input ('student name: ')
code = input ('the grade of code portfolio: ')
poster = input('the grade of poster resentation: ')
exam = input('the grade of final exam: ')
student_list = Student(name, float(code), float(poster), float(exam))
print(student_list.grade())
