# Wrapping (bundling) class (data,attribute) and object in a single unit called encapsulation
# using getter,setter 


class Student:
    def __init__(self, name, marks):
        self.name = name          # Public variable
        self.__marks = marks      # Private variable

    # Display student details
    def student_result(self):
        print("Name :", self.name)
        print("Marks:", self.__marks)

    # Setter method
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    # Getter method
    def get_marks(self):
        return self.__marks


# Object Creation
s = Student("RP", 45)

print("Before Update:")
s.student_result()

# Update marks
s.set_marks(90)

print("\nAfter Update:")
s.student_result()

# Get marks using getter
print("\nMarks using Getter:", s.get_marks())
        