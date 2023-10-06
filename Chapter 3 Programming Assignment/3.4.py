#3.4
#Geometry: area of a pentagon
#Abdullah Mohammad
#1/4/23

import math

side = eval(input("Enter the side length: "))

area = (5 * side**2) / (4 * math.tan(math.pi / 5))
print(area)
