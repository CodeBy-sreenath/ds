class Bank:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def getbalance(self):
        return self.__balance
acc=Bank()
acc.deposit(1000)
print(acc.getbalance())                
        