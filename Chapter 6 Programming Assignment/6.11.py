#6.11
#Financial application: compute commissions
#Abdullah Mohammad
#1/13/23

def CalcCommission(sales):
    if sales >= 0.01 and sales < 5000:
        percent = 0.8
        
    elif sales >= 5000 and sales <= 10000:
        percent = 0.10

    elif sales > 10000:
        percent = 0.12

    if sales >= 0:                          #Detecting if the number is positive
        return sales * percent              #return commission
    else:
        print("Invalid Number")             #If negative number

def main():
    print("Sales Amount \t Commission \n")

    for sales in range(10000, 105000, 5000):
        print(sales, '\t\t', CalcCommission(sales))

main()
