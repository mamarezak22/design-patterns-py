class OldPayment:
    #like 2335 cent
    def pay_in_cents(self,amount : int):
        print(f"paid {amount}")

class NewPayment:
    #like 23.35$
    def pay(self,amount : float):
        print(f"paid {amount}")

class OldPaymentAdapter:
    def __init__(self,payment : OldPayment):
        self.payment = payment
    
    def pay(self,amount : float):
        cent_amount = amount * 100
        self.payment.pay_in_cents(int(cent_amount))
