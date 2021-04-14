class Student(object):
    def __init__(self, full_name, undergraduate_programme):
        self.full_name = full_name
        self.undergraduate_programme = undergraduate_programme
    def stulist(self):
        return self.full_name + ': ' + self.undergraduate_programme
example = Student('Mao Xinjie', 'BMI')
print(example.stulist())

import re
def stud(data, name, programme):
    data.append(Student(name, programme))
    return data
Record = []
x = 'y'
while x == 'y':
    name = input('Enter the full name: ')
    programme = input('Enter the undergraduate programme: ')
    Record = stud(Record, name, programme)
    x = input('Add another student? y/n: ')
n = 1
for i in Record:
    print(n,'. ', i)
    n = n + 1
    print(i.stulist())