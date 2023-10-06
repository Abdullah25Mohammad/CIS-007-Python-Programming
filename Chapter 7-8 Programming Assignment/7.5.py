#7.5 (Using the Class)
#Geometry: n-sided regular polygon 
#Abdullah Mohammad
#1/16/23

from PolygonClass import RegularPolygon

def main():
    Polygon1 = RegularPolygon()
    Polygon2 = RegularPolygon(6, 4)
    Polygon3 = RegularPolygon(10, 4, 5.6, 7.8)

    print("Polygon 1 has an area of", format(Polygon1.getArea(), '.4f'),
          "and a perimeter of ", format(Polygon1.getPerimeter(), '.4f'))
    
    print("Polygon 2 has an area of", format(Polygon2.getArea(), '.4f'),
          "and a perimeter of ", format(Polygon2.getPerimeter(), '.4f'))
    
    print("Polygon 3 has an area of", format(Polygon3.getArea(), '.4f'),
          "and a perimeter of ", format(Polygon3.getPerimeter(), '.4f'))

main()
