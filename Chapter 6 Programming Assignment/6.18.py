#6.18
#Display matrix of 0s and 1s
#Abdullah Mohammad
#1/13/23

import random


def printMatrix(n):
   for row in range(n):
       for side in range(n):
           print(random.randint(0,1), end = ' ')
       print()

def main():
    n = eval(input("Enter a number: "))
    if n >= 0:
        printMatrix(n)
    else:
        print("Invalid Number")

main()
