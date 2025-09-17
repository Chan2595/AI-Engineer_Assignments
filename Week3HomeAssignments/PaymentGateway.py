class creditCardPayment:
    def process_payment(self,amount):
        print(f"Processing credit card payment ${amount}")

class PayPalPayment:
    def process_payment(self,amount):
        print(f"Processing PayPalPayment card payment ${amount}")

class BankTransferPayment:
    def process_payment(self,amount):
        print(f"Processing BankTransferPayment card payment ${amount}")

def make_payment(payment_method,amount):
    payment_method.process_payment(amount)

if __name__ == "__main__":
    credit_card= creditCardPayment()
    pay_pal= PayPalPayment()
    bank_transfer= BankTransferPayment()

payment_methods = [credit_card, pay_pal, bank_transfer]
for method in payment_methods:
    make_payment(method,100)