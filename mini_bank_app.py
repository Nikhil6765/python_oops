class customer:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(self.balance)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("left balance : ",self.balance)
        else:

            print("insufficient Balance")

print("welcome to the AAPKAbank")
