class customer:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Your current balance",self.balance)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("left balance : ",self.balance)
        else:

            print("insufficient Balance")

print("welcome to the AAPKAbank")
name=input("enter your name: ")
c=customer(name)
while True:
    print()
    print("Enter d for Deposit : ")
    print("Enter w for Withdraw : ")
    print("Enter e for Exit :")
    option=input("what do you want from the options : ")

    if option.lower()=='d':
        amount=int(input("enter amount you want to deposit"))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=int(input("enter amount you want to withdraw"))
        c.withdraw(amount)
    elif option.lower()=='e':
        break
    else:
        print("Please Try Again!")
    


    
    