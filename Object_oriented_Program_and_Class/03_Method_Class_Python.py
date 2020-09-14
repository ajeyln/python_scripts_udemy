# Simple account class with balance
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account is created for {}".format(self.name))
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
        else:
            print("You dont have sufficient balance to withdraw")
    
    def show_balance(self):
        print('Your current balance is {}'.format(self.balance))
    
if __name__ == "__main__":
    name=str(input("Please Enter Your name:\n"))
    act_balance = 100.0
    name1 = Account(name, act_balance)
    name1.show_balance()

    payment = float(input("Enter the ammount, which has to be deposited:\n"))
    name1.deposit(payment)
    name1.show_balance()

    payment = float(input("Enter the ammount, How much you need withdraw:\n"))
    name1.withdraw(payment)
    name1.show_balance()


