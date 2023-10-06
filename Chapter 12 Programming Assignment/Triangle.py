from GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()

        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    #Getters and Setters

    def getSide1(self):
        return self.__side1

    def setSide1(side1):
        self.__side1 = side1
    
    def getSide2(self):
        return self.__side2
    
    def setSide1(side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3
    
    def setSide3(side3):
        self.__side3 = side3

    #Methods

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    
    def getArea(self):
        #Using Heron's Formula

        self.__semiperimeter = (self.__side1 + self.__side2 + self.__side3) / 2

        self.__area = math.sqrt(self.__semiperimeter * (self.__semiperimeter - self.__side1) * (self.__semiperimeter - self.__side2) * (self.__semiperimeter - self.__side3))

        return self.__area

    def __str__(self):
        return "Triangle: side1 = " + str(side1) + " side2 = " + str(side2) + " side3 = " + str(side3)
