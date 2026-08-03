class Payment_Mode:
    def process_payment(self, amount):
        pass
class CreditCardPayment(Payment_Mode):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Payment of {amount} processed using Credit Card {self.card_number}")


class UPIPayment(Payment_Mode):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        print(f"Payment of {amount} processed using UPI {self.upi_id}")


class WalletPayment(Payment_Mode):
    def __init__(self, balance):
        self.balance = balance

    def process_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Payment Successful: {amount}")
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

# create a list of all object,payments is a list object
payments = [
    CreditCardPayment("123456789"),
    UPIPayment("rohit@upi"),
    WalletPayment(1900)
]

#OR

# credit = CreditCardPayment("123456789")
# upi = UPIPayment("rohit@upi")
# wallet = WalletPayment(2100)

# payments = [credit, upi, wallet]

for payment in payments:
    payment.process_payment(2000)