# what is constructor
# A Constructor is special method that run automatically the moment an object create
# __init__():constructor method

# class Student:
#     def __init__(self, name, age, roll_no, city):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
#         self.city = city

# stu1 = Student("Aman", 45, 7899, "Odisha")
# stu2 = Student("Rohit Pal", 27, 6634, "Meerut")

# print(stu1.name)
# print(stu1.age)
# print(stu1.roll_no)
# print(stu1.city)
#print(stu2.city)


class Student:
    def __init__(self, name, age, roll_no, city):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.city = city
        print("constructor call auto")

    def show_details(self):
        print(f"Student Name:{self.name}")
        print(f"Student Name:{self.age}")
        print(f"Student Name:{self.roll_no}")
        print(f"Student Name:{self.city}")


stu1 = Student("Aman", 45, 7899, "Odisha")
stu2 = Student("Rohit Pal", 27, 6634, "Meerut")
#stu3=Student("Ravi Kumar",26,567,"Muzaffarnagar")

stu1.show_details()
print("===============================================")
stu2.show_details()
print("===============================")
#stu3.show_details()

     