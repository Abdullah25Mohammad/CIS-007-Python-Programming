#7.3 (Define the Class)
#The Account class
#Abdullah Mohammad
#1/16/23

class Account:
    def __init__(self, ID=0, balance=100, annualInterestRate=0):
        self.__id = ID
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getID(self):
        return self.__id
    
    def setID(self, ID):
        self.__id = ID

    def getBalance(self):
        return self.__balance
    
    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate


    def getMonthlyInterestRate(self):
        self.__monthlyInterestRate = self.__annualInterestRate / 12
        return self.__monthlyInterestRate

    def getMonthlyInterest(self):
        self.__monthlyInterest = self.__balance * (self.__monthlyInterestRate / 100)
        return self.__monthlyInterest

    def withdraw(self, amount):
        if (self.__balance - amount) >= 0:
            self.__balance -= amount
            print("Amount successfully withdrawn")
        else:
            print("You do not have enough money to withdraw that amount")

    def deposit(self, amount):
        self.__balance += amount
        print("Amount successfully deposited")

    
