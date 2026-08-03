# polymorphism is a combination of two words poly+morphism
# poly means many
# morphism means forms 
#types of polymorphism
# There are two types
#1.Method Overloading(compile-time/static)-> Python does not support truly method overloading like c++ and java,
#It can be achieved by default arguments or *args

#Example:
            #  class Demo:
            #     def add(self, *args):
            #      print(sum(args))
            #     d = Demo()
            #     d.add(10)
            #     d.add(10, 20)
            #     d.add(10, 20, 30)

# 2. Method Overriding(Run-Time/Dynamic)-> In this concept we create more than one method with same name,
#But each method play a diffrent role or functionality.
#Python fully Support Method-Overriding.

#Example:
class Animal:
   
     def sound(self):
            print("Animal makes a  sound")
class Dog(Animal):
    def sound(self):
        print("Dog Bark")
class Cat(Animal):
    def sound(self):
        print("Cat Meow")

d=Dog()
c=Cat()
a=Animal()
d.sound()
c.sound()
a.sound()
        