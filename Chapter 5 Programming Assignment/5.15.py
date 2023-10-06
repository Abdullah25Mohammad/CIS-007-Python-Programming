#5.15
#Find the largest n such that n^3 < 12,000
#Abdullah Mohammad
#1/5/23

n = 0
count=0

while count**3 < 12000:
    count +=1
    n = count-1

print(n, "is the largest integer where n^3 (", n**3,") is less than 12000")
