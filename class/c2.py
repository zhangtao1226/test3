from c1 import People

class Student(People):
    print(People.__dict__)
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)
        # print(People.name)
    def aa(self):
        a = self.get_name()
        return a


student = Student('tao', 18)

print(student.name)
print(student.age)
print(student.get_age())
print(student.get_name())
print(student.aa())
