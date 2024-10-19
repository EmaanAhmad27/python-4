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
    def get_students(self):
        return [student.get_details() for student in self.students]
    def get_teachers(self):
        return [teacher.name for teacher in self.teachers]
math_department = Departments("Mathematics")
eng_department = Departments("English")
sci_department = Departments("Science")
cs_department = Departments("Computer")
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
class Students (Humans):
    def __init__(self, name, age, gender, student_id, section, department, courses_enrolled):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.section = section
        self.department = department
        self.courses_enrolled = courses_enrolled
    def get_details(self):
            return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'student_id': self.student_id,
            'section': self.section,
            'department': self.department,
            'courses_enrolled': self.courses_enrolled
        }
student1 = Students(name="Sara Atif", age=20, gender="Female", student_id="CS101", section="A", department="Computer Science", courses_enrolled=["Data Structures", "Algorithms"])
student2 = Students(name="Fawad Najam", age=22, gender="Male", student_id="ENG102", section="B", department="English", courses_enrolled=["American Literature", "Translation Studies"])
student3 = Students(name="Shahmir Salar", age=21, gender="Male", student_id="MATH201", section="A", department="Mathematics", courses_enrolled=["Calculus", "Linear Algebra"])
student4 = Students(name="Laiba Anjum", age= 23, gender = "Female", student_id= "SCI221", section= "B", department= "Science", courses_enrolled =["zoology", "Botany"])
student5 = Students(name="Ahmed Ali", age=19, gender="Male", student_id="CS102", section="B", department="Computer Science", courses_enrolled=["Operating Systems", "Machine Learning"])
student6 = Students(name="Hina Raza", age=24, gender="Female", student_id="ENG103", section="A", department="English", courses_enrolled=["Postcolonial Literature", "Creative Writing"])
student7 = Students(name="Ahsan Khalid", age=22, gender="Male", student_id="MATH202", section="B", department="Mathematics", courses_enrolled=["Differential Equations", "Probability"])
student8 = Students(name="Fatima Zia", age=21, gender="Female", student_id="SCI222", section="A", department="Science", courses_enrolled=["Chemistry", "Physics"])
cs_department.add_student(student1)
cs_department.add_student(student5)
eng_department.add_student(student2)
eng_department.add_student(student6)
math_department.add_student(student3)
math_department.add_student(student7)
sci_department.add_student(student4)
sci_department.add_student(student8)
print("\nComputer Science Department Students:")
for student in cs_department.get_students():
    print(f"  {student}")
print("\nMathematics Department Students:")
for student in math_department.get_students():
    print(f"  {student}")
print("\nEnglish Department Students:")
for student in eng_department.get_students():
    print(f"  {student}")   
print("\nScience Department Students:")
for student in sci_department.get_students():
    print(f"  {student}")    
class Teachers (Humans):
    def __init__(self, name, age, gender, teacher_id, section, department, courses_taught):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.section = section
        self.courses_taught = courses_taught
        self.department = department
    def get_details(self):
        return {
            'name': self.name,
            'age': self.age,
            'department': self.department,
            'gender': self.gender,   
            'teacher_id': self.teacher_id,
            'section': self.section,
            'courses_taught': self.courses_taught     
        }
teacher1 = Teachers(name="Dr. Sidra Bano", age=45, section= "A", gender="Female", teacher_id="T1001", department="Computer Science", courses_taught=["Data Structures", "Algorithms"])
teacher2 = Teachers(name="Mr. Numair Aslam", age=55, section= "B", gender="Male", teacher_id="T111", department="Computer Science", courses_taught=["Flow Chart", "Cyber Security"])
teacher3 = Teachers(name="Ms. Amna Shakeel", age=41, section= "A", gender="Female", teacher_id="T1002", department="Mathematics", courses_taught=["Calculus", "Linear Algebra"])
teacher4 = Teachers(name="Dr. Ahmad Riaz", age=50, section= "B", gender="Male", teacher_id="T1032", department="Mathematics", courses_taught=["Trignometry", "Geometry"])
teacher5 = Teachers(name="Ms. Hiba Sidiqui", age=35, section= "A", gender="Female", teacher_id="T1502", department="English", courses_taught=["American Literature", "Translation Studies"])
teacher6 = Teachers(name="Mr. Moeez Ahmad", age=37, section= "B", gender="Male", teacher_id="T1132", department="English", courses_taught=["Postcolonial Literature", "Creative Writing"])
teacher7 = Teachers(name="Dr. Saima Azhar", age=39, section= "A", gender="Female", teacher_id="T2802", department="Science", courses_taught=["zoology", "Botany"])
teacher8 = Teachers(name="Mr. Bilal Fiaz", age=42, section= "B", gender="Male", teacher_id="T3132", department="Science", courses_taught=["Chemistry", "Physics"])        
cs_department.add_teacher(teacher1)
cs_department.add_teacher(teacher2)
math_department.add_teacher(teacher3)
math_department.add_teacher(teacher4)
eng_department.add_teacher(teacher5)
eng_department.add_teacher(teacher6)
sci_department.add_teacher(teacher7)
sci_department.add_teacher(teacher8)
print("\nComputer Science Department Teachers:")
for teacher in cs_department.get_teachers():
    print(f"  {teacher}")

print("\nMathematics Department Teachers:")
for teacher in math_department.get_teachers():
    print(f"  {teacher}")
print("\nEnglish Department Teachers:")
for teacher in eng_department.get_teachers():
    print(f"  {teacher}")

print("\nScience Department Teachers:")
for teacher in sci_department.get_teachers():
    print(f"  {teacher}")
   
        