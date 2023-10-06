#2.13
#Split digits
#Abdullah Mohammad
#1/4/23


Num = int(input("Enter a 4 digit integer: "))


ThouPlace = Num//1000
HundPlace = (Num % 1000)//100
TensPlace = (Num % 100)//10
OnesPlace = (Num % 10)

print(ThouPlace)
print(HundPlace)
print(TensPlace)
print(OnesPlace)

