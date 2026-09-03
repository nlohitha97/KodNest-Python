# Build Different PAyment -Process Classess
from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class UPIPayment(PaymentProcessor):
    def __init__(self,amount):
        self.amount = amount
    #Implemrnt process_payment()
    def process_payment(self):
       return f"UPI Payment: {self.amount}"

class CardPayment(PaymentProcessor):
    def __init__(self,amount):
        self.amount = amount
    #Implemrnt process_payment()
    def process_payment(self):
       return f"Card Payment: {self.amount}"

class NetBankingPayment(PaymentProcessor):
    def __init__(self,amount):
        self.amount = amount
    #Implemrnt process_payment()
    def process_payment(self):
       return f"NetBanking Payment: {self.amount}"
upi_amount = int(input())
card_amount = int(input())
net_amount = int(input())

# Create the three objects

UPI = UPIPayment(upi_amount)
Card = CardPayment(card_amount)
NetBanking = NetBankingPayment(net_amount)

# Store them in one list

pay = [UPI,Card,NetBanking]

# Process them using one loop

for i in pay:
    print(i.process_payment())