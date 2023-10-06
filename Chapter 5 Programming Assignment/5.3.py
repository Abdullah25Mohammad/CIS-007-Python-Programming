#5.3
#Conversion from kilograms to pounds
#Abdullah Mohammad
#1/5/23

print("Kilograms\tPounds")

for kg in range(1, 200, 2):
    lb = kg * 2.2
    print(kg, '\t\t', format(lb, "5.1f"))
