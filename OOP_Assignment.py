class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []
    def add_department(self, department):
        self.departments.append(department)
    def uni (self):
        print(f"{self.name} is located in {self.location}")
    def display_departments(self):  
        print("Departments in the university:")
        for department in self.departments:  
            print(department.name)
u = University ("AI_univeristy", "Faisalabad")
u.uni()
class Departments:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_student(self, student):
        self.students.append(student)
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
cs_department = Departments("Computer Science")
math_department = Departments("Mathematics")
eng_department = Departments("English")
sci_department = Departments("Science")
u.add_department(cs_department)
u.add_department(math_department)
u.add_department(eng_department)
u.add_department(sci_department)
u.display_departments()
class Humans:
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self.age = age
    
   


   
        