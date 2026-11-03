class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Ammount):
        self.Name = Name
        self.Ammount = Ammount
    def __init__(self):
        self.Name= ""
        self.Ammount = 0.0


    def Display(self):
        
        self.Name = str(input("Enter the Account Holder name : "))
        self.Ammount = float(input("Enter the Account Holder balance : "))

    def Deposit(self):
        Dammount = float(input("Enter the ammount that should be deposited : "))

        TAmmount = (self.Ammount + Dammount)
        print("now the total balance is : ",TAmmount)

    def Withdraw(self):
        print("Enter the withdraw ammount : ")
        Wammount = float(input())

        if(Wammount < self.Ammount):
            Wammount = self.Ammount - Wammount
            print("Withdrawal of money is succeed || And remaining balance is : ",Wammount)
        else :
            print("withdrawal of money is prohibited because of insufficient balance...")

    def CalculateIntrest(self):
        print("the rate of intreset and ammount  is ",BankAccount.ROI,self.Ammount)

        Intrest = self.Ammount * BankAccount.ROI / 100

        print("Calculated rate of intrest is : ",Intrest)

obj1 = BankAccount()
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateIntrest()

            
