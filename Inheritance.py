#Inheritance
#type
# single
# multilevel
# multiple
# hybrid
# hierarchical



# single

class Person:
    def show(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("I am studying")
class TopperStudent(Student):
    def rank(self):
        print("rank 1")
t=TopperStudent()
t.show()
t.study()
t.rank()


# multilevel
class Father:
    def skills(self):
        print("coding")
class Mother:
    def talent(self):
        print("drawing")
class Child(Father,Mother):
    pass

c1=Child()
c1.skills()
c1.talent()


# hierarchical
class Person:
    def show(self):
        print("I am a person")
class Student(Person):
    pass
class Driver(Person):
    pass
class Teacher(Person):
    pass
class Driver(Person):
    pass
class Painter(Person):
    pass

# hybrid
# A mix(combination) of two inheritance


