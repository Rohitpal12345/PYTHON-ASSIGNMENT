# Abstraction is a process of hiding backgraound details and show essentials details to end-user.
# Achive Abstraction by using Abstraction Class.
# Create Abstract Method By @abstractmethod.
#@abstractmethod is a decorator provided by the abc module.
#  It is used to declare an abstract method, which must be implemented by every concrete child class.
# Syntax :
            # from abc import ABC,abstractmethod
            # class class_name(ABC):
            #     @abstractmethod
            #     def method_name():
            #         pass

            # Where:
            # abc is Module
            # ABC is Class
            # @abstractmethod is method/Decorator

#EXAMPLE:
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class Credit_card_payment(Payment):

    def pay(self, amount):
        print(f"paid{amount} using card")
            
class Upi_payment(Payment):
    def pay(self, amount):
        print(f"paid{amount} using UPI")
    
pymt=Upi_payment()
pymt.pay(400)