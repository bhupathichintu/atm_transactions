class account():
    def __init__(self):
        amount = int(input("enter any amount:"))
        self.amount = amount
    def withdraw_amount(self):
        withdraw_amount = int(input("enter withdraw Amount:"))
        if withdraw_amount<=1000:
            if withdraw_amount%100==0:
                print("the withdrawn Amount Is:",withdraw_amount)
                print("The Reamining Amount Is",self.amount-withdraw_amount)
            else:
                print("your entered amount is not multiple of hundreds , please enter amount ,is multiple of hundred")
        else:
            print("your entered amount is  greater than available amount")
    def credit_amount(self):
        credit_amount = int(input("enter your  deposit Amount:"))
        print("Your Account Deposited With:",credit_amount)
        print("Total Available Amount IS:",credit_amount+self.amount)
account1=account()
account1.withdraw_amount()
account1.credit_amount()