# main class
# add student
# get all student
# get student by roll no
# update  student
# delete student


class Student:
    def __init__(self):
        self.student = {}

    def add_student(self, roll_no, name, age, city):
        if roll_no in self.student:
            print("Student Already Exists")
            return

        self.student[roll_no] = {
            "name": name,
            "age": age,
            "city": city
        }

        print(f"Student {name} added.")

        #Create a Method to get All Record

    def get_all_students(self):
        if not self.student:
            print("No student found")
            return

        for roll_no, details in self.student.items():
            print(f"""
Roll No : {roll_no}
Name    : {details['name']}
Age     : {details['age']}
City    : {details['city']}
""")

# Here get student by their student id/roll no
            
    def get_student_by_roll(self,roll_no):
        if roll_no in self.student:
            details=self.student[roll_no]
            print(f"""


Name    : {details['name']}
Age     : {details['age']}
City    : {details['city']}
""")

# Here update student details by roll_no

    def update_student(self,roll_no,name=None,age=None,city=None):
        if roll_no not in self.student:
            print("Student Not Found")
            return
        if name is not None:
            self.student[roll_no]["name"]=name
        if age is not None:
            self.student[roll_no]["age"]=age
        if city is not None:
            self.student[roll_no]["city"]=city  

        print("Student updated successfully!") 

        # Create a Method to delete Record by Roll Number
    def delete_student(self,roll_no):
        if roll_no not in self.student:
            print("Record Not Found")
            return
        del self.student[roll_no]
        print("Record delete successfully!")

s = Student()
print("==========HERE-ADD-STUDENT============")
s.add_student(100, "Rohit Pal", 27, "Meerut")
s.add_student(101, "Amit", 27, "GZB")
s.add_student(102, "Ravi Kumar", 27, "MZN")
print("==========HERE-GET-ALL-STUDENT-RECORD============")
s.get_all_students()
 
print("===========================================")
print("=============Get-Student-By-Roll-No")
s.get_student_by_roll(100)
print("=================update================")
s.update_student(100,city="Muzaffarnagar")
print("=========After Updated===============")
s.get_student_by_roll(100)
print("=====================================================")
s.delete_student(100)
print("============After-deleted-Record=================")
s.get_all_students()


    