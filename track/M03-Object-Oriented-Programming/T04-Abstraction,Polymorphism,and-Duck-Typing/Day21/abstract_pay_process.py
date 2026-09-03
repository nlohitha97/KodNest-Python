#Build an Abstract PaymentProcessor
from abc import ABC,abstractmethod

class PaymentProcesser(ABC):
    @abstractmethod
    def process_payment(self):
        pass
class UPIPayment(PaymentProcesser):
    def __init__(self,amount):
        self.amount = amount
    #Implemrnt process_payment for upi
    def process_payment(self):
       return f"UPI Payment: {self.amount}"
amount = int(input())
#Create the object and process the payment
pay =UPIPayment(amount)
print(pay.process_payment())