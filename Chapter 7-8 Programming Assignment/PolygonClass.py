#7.5 (Define the Class)
#Geometry: n-sided regular polygon 
#Abdullah Mohammad
#1/16/23

import math

class RegularPolygon:

    
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getN(self):
        return self.__n

    def setN(self, n):
        self.__n = n

    def getSide(self):
        return self.__side

    def setSide(self, side):
        self.__side = side

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y


    def getPerimeter(self):
        self.__perimeter = self.__n * self.__side
        return self.__perimeter

    def getArea(self):
        self.__area = (self.__n * (self.__side)**2) / (4 * math.tan(math.pi / self.__n))
        return self.__area
