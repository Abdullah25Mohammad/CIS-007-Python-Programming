#7.3 (Using the Class)
#The Account class
#Abdullah Mohammad
#1/16/23

from AccountClass import Account


def main():
    testAccount = Account(1122, 20000, 4.5)

    testAccount.withdraw(2500)
    testAccount.deposit(3000)

    print("The ID is, ", testAccount.getID())
    print("The balance is, $", format(testAccount.getBalance(), '.2f'))
    print("The monthly interest rate is, ", format(testAccount.getMonthlyInterestRate(), '.2f'), "%")
    print("The monthly interest  is, ", format(testAccount.getMonthlyInterest(), '.2f'), "%")

main()
