class Bank():

    def __init__(self,n,b=0):
        self.name = n
        self.balance = b

    def viewbalance(self):
     
        print("Your Balance is ",self.balance)

    def deposit(self,amount):
        self.balance = self.balance+amount
        print("You have successfully deposited")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Your withdrawel is successfull")


name = input("Enter Your name : ")
b = Bank(name,0)

print("1. Deposit\n2. Withdraw\n3. View Balance")    
while(True):
 option = int(input("Enter the Option (1/2/3) : "))    

 if option==1:
    amount = int(input("Enter the amount for Deposit : "))
    b.deposit(amount)
 elif option==2:
    amount = int(input("Enter the amount for Withdraw : "))
    b.withdraw(amount)    
 elif option==3:
    b.viewbalance()
 else:
    print("Invalid Option")    








        




