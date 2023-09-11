
class BankAccount():
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"Entered amount {amount} should be greater than 0")
        else:
            self.balance += amount
    
    def withdraw(self, amount):
        if (self.balance-amount < 0) or (amount < 0):
            raise ValueError(f"Entered amount {amount} is greater than current balance")
        else:
            self.balance -= amount
    
    def pay_interest(self):
        self.balance += self.interest_rate*self.balance

    def __repr__(self):
        instance_name = "".join([t.__name__ for t in type(self).__mro__[:-1]])
        return f"A {instance_name} with {self.balance} in it"
    

class Savings(BankAccount):
    def pay_interest(self):
        self.interest_rate = 0.0035
        return super().pay_interest()
    

class HighInterest(BankAccount):
    def __init__(self, withdrawal_fee=0):
        self.withdrawal_fee = withdrawal_fee
        super().__init__(initial_balance=0)

    def pay_interest(self):
        self.interest_rate = 0.007
        return super().pay_interest()
    
    def withdraw(self, amount):
        if (self.balance-amount-self.withdrawal_fee) < 0:
            raise ValueError(f"Entered amount {amount} is greater than current balance")
        else:
            self.balance -= amount+self.withdrawal_fee

    
class LockedIn(BankAccount):
    def pay_interest(self):
        self.interest_rate = 0.009
        return super().pay_interest()
    
    def withdraw(self, amount=0):
        print ("Can't make an early withdrawal from a Locked-in Savings account")

    
if __name__ == "__main__":

    b = BankAccount(initial_balance=100)
    b # A BankAccount with $100 in it.

    b.deposit(2) # Deposited $2.
    b

    b.withdraw(70) # Withdrew $70.
    b # A BankAccount with $32 in it.

    s = Savings(140)
    s.pay_interest() # Deposited $0.49.
    s # A SavingsBankAccount with $140.49 in it.

    hi = HighInterest(withdrawal_fee=3)
    hi # A HighInterestSavingsBankAccount with $0 in it.

    hi.deposit(140) # Deposited $140.
    hi

    hi.pay_interest() # Deposited $0.98.
    hi

    hi.withdraw(0.98) # Withdrew $0.98.
    hi # A HighInterestSavingsBankAccount with $137.0 in it.

    l = LockedIn(1000)
    l

    l.pay_interest() # Deposited $9.0.
    l

    l.withdraw(10) # "Can't make an early withdrawal from a Locked-in Savings account."
    l # A LockedInHighInterestSavingsBankAccount with $1009.0 in it.
