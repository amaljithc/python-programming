class account:
    def __init__(self,name,accno,typeacc,bal):
        self.name=name
        self.accountnumber=accno
        self.type=typeacc
        self.balance=bal
    def deposit(self):
        amt=int(input("enter an amount to deposit:"))
        self.balance+=amt
        print("NEW BALANCE:",self.balance)
    def withdraw(self):
        if(self.balance<500):
            print("insufficiant balance....!")
        else:
            amt=int(input("enter an amount to withdraw:"))
            self.balance-=amt
            print("NEW BALANCE:",self.balance)
    def disp(self):
            print("\nACCOUNT DETAILS")
            print("_______\n")
            print("Name of the Account holder:",self.name)
            print("Account number:",self.accountnumber)
            print("Type of account:",self.type)
            print("Balance:",self.balance)
s=account(input("enter account holder name:"),int(input("enter the account number:")),input("enter account type[CURRENT/SAVINGS]:"),int(input("enter balance:")))
print("\nBANKING")
print("____")
print("\n1.ACCOUNT DETAILS\n2.DEPOSIT\n3.WITHDRAW\n0.EXIT\n")
def bank():
    n=int(input("\nenter choice:"))
    if(n==1):
        s.disp()
        return bank()
    elif n==2:
        s.deposit()
        return bank()
    elif n==3:
        s.withdraw()
        return bank()
    elif n==0:
        print("THANK YOU")
        return 0
    else:
        print("INVALID ENTRY!")
        print("please enter valid choice\n")
        return bank()
bank()