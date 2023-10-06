#4.12
#Check a number
#Abdullah Mohammad
#1/5/23

number = eval(input("Enter an integer: "))

print("Is", number, "divisible by 5 and 6?", number%5==0 and number%6==0)
print("Is", number, "divisible by 5 or 6?", number%5==0 or number%6==0)
print("Is", number, "divisible by 5 or 6, but not both?", (number%5==0 or number%6==0) and not (number%5==0 and number%6==0))
