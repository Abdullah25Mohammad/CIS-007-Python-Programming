#12.1
#The Triangle class
#Abdullah Mohammad
#1/22/23

from GeometricObject import GeometricObject
from Triangle import Triangle

def main():
    side1 = eval(input("Enter length for side 1: "))
    side2 = eval(input("Enter length for side 2: "))
    side3 = eval(input("Enter length for side 3: "))

    color = input("Enter a color: ")

    while True: #Keep looping until a valid answer is given
        shouldFill = eval(input("Should the shape be filled (1 for yes, 0 for no): "))
        if shouldFill == 1:
            shouldFill = True
            break #End loop once valid answer given
        elif shouldFill == 0:
            shouldFill = False
            break #End loop once valid answer given


    testTriangle = Triangle(side1, side2, side3)
    testTriangle.setColor(color)
    testTriangle.setFilled(shouldFill)

    print()

    print("The triangle's area is", str(testTriangle.getArea()))
    print("The triangle's perimeter is", str(testTriangle.getPerimeter()))
    print("The triangle's color is", str(testTriangle.getColor()))
    print("The triangle's fill status is", str(testTriangle.isFilled()))

main()
