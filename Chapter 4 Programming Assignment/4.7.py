#4.7
#Financial application: monetary units
#Abdullah Mohammad
#1/4/23


#Code Copied from Listing 3.4 (as this is what the instructions asks for)








numberOfQuarters = remainingAmount // 25





numberOfNickels = remainingAmount // 5


numberOfPennies = remainingAmount


#--------------------------#
 

print("Your amount", amount, "consists of")
print("\t", numberOfOneDollars, "dollar" if numberOfOneDollars == 1 else "dollars")
print("\t", numberOfQuarters, "quarter" if numberOfQuarters == 1 else "quarters")
print("\t", numberOfDimes, "dime" if numberOfDimes == 1 else "dimes")
print("\t", numberOfNickels, "nickel" if numberOfNickels == 1 else "nickels")
print("\t", numberOfPennies, "penny" if numberOfPennies == 1 else "pennies")