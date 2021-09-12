class Person:
    def __init__(self, lname, fname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")

class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()

class Teacher(Person):
    def __init__(self, lname, fname):
        Person.__init__(self, fname, lname)
        super().__init__(fname, lname)