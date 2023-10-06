#2.5
#Financial application: calculate tips
#Abdullah Mohammad
#1/4/23


subtotal, gratrate = eval(input("Enter the subtotal and the gratuity rate: "))

grat = gratrate/100 * subtotal
total = subtotal + grat

print("The Gratuity is ", grat, "and the total is ", total)
